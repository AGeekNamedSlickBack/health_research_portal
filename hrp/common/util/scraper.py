"""Create the web scraper."""
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from hrp.common.util import KEYWORDS, URL_LIST
from hrp.researches.models import Research

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
)


def scraper():
    """Scrape certified repositories."""
    category_list = []
    for URL in URL_LIST:
        page = requests.get(URL, verify=False)  # Bypass untrusted SSL
        soup = BeautifulSoup(page.content, "html.parser")

        if "ir.jkuat.ac.ke" in URL:
            results = soup.find(id="ds-content-wrapper")
            researches = results.find_all(class_="ds-artifact-list")
        else:
            results = soup.find(id="main-container")
            researches = results.find_all(
                class_="col-sm-9 artifact-description"
            )

        # Fetch the categories from the urls
        category = URL.split("&")[1]
        category_list.append(category)

        for item in category_list:
            category = item.split("=")[1]

        for research in researches:
            if "ir-library.ku.ac.ke" in URL:
                url = (
                    "https://ir-library.ku.ac.ke" + research.find("a")["href"]
                )
                title = research.find("h4").text
            if "erepository.uonbi.ac.ke" in URL:
                url = (
                    "http://erepository.uonbi.ac.ke"
                    + research.find("a")["href"]
                )
                title = research.find("h4").text
            if "ir.jkuat.ac.ke" in URL:
                url = "http://ir.jkuat.ac.ke" + research.find("a")["href"]
                title = research.find(class_="artifact-title").text

            #  Get the keywords
            response = requests.get(url, verify=False)
            text = BeautifulSoup(response.content, "html.parser")
            text = text.get_text()

            # Remove stop words like 'a' 'the' 'an'
            stop_words = set(stopwords.words("english"))
            word_tokens = word_tokenize(text)

            # Remove punctuations and lower upper cases
            word_tokens = [
                word.lower() for word in word_tokens if word.isalpha()
            ]

            filtered_text = [w for w in word_tokens if not w in stop_words]
            filtered_text = []

            for w in word_tokens:
                if w not in stop_words:
                    filtered_text.append(w)

            count_word_frequency = nltk.FreqDist(filtered_text)
            count_word_frequency = count_word_frequency.most_common(
                20
            )  # Gets most frequent words

            # Parse them to get the key words
            get_keywords = [
                [j for j in i if type(j) == str] for i in count_word_frequency
            ]  # Gets keywords in alist
            try:
                keyword = [
                    _keyword
                    for _keyword in KEYWORDS
                    if _keyword in get_keywords
                ]  # Compares keywords with most_common words
                keyword = ",".join(keyword[0])  # Gets the intersect
                keyword = "{}:{}".format(category, keyword)

            except IndexError:
                continue

            if None in (url, title):
                continue

            try:
                Research.objects.create(
                    url=url, title=title, category=category, keyword=keyword
                )
                print(
                    "{} - {} successfully added in category {} - {}".format(
                        title, url, category, keyword
                    )
                )
            except:
                print("Research already scraped")
