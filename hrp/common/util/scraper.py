"""Create the web scraper."""
import urllib.request

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

from hrp.common.util import KEYWORDS, URL_LIST
from hrp.researches.models import Research


def scraper():
    """Scrape certified repositories."""
    category_list = []
    for URL in URL_LIST:
        page = urllib.request.urlopen(URL)
        soup = BeautifulSoup(page, "html.parser")

        results = soup.find(id="main-container")
        researches = results.find_all(class_="col-sm-9 artifact-description")

        # Fetch the categories from the urls
        category = URL.split("&")[1]
        category_list.append(category)

        for item in category_list:
            category = item.split("=")[1]

        for research in researches:
            url = "http://erepository.uonbi.ac.ke" + research.find("a")["href"]
            title = research.find("h4").text

            #  Get the keywords
            response = urllib.request.urlopen(url)
            html = response.read()
            text = BeautifulSoup(html, "html.parser")
            text = text.get_text()

            tokenized_text = [t for t in text.split()]

            # Remove stop words like 'a' 'the' 'an'
            gotten_stopwords = stopwords.words("english")
            clean_tokenized_text = tokenized_text[:]

            for stopword in tokenized_text:
                if stopword in gotten_stopwords:
                    clean_tokenized_text.remove(stopword)

            count_word_frequency = nltk.FreqDist(clean_tokenized_text)
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
