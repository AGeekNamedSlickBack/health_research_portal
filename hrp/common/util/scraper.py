"""Create the web scraper."""
import requests
from bs4 import BeautifulSoup

from hrp.researches.models import Research

URL_LIST = [
    "http://erepository.uonbi.ac.ke/discover?scope=%2F&query=cancer&submit=&rpp=40&sort_by=dc.date.issued_dt&order=desc",
    "http://erepository.uonbi.ac.ke/discover?scope=%2F&query=malaria&submit=&rpp=30&sort_by=dc.date.issued_dt&order=desc",
]


def scraper():
    """Scrape certified repositories."""
    for URL in URL_LIST:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="main-container")
    researches = results.find_all(class_="col-sm-9 artifact-description")

    category = categorize_the_researches()

    for research in researches:
        url = "http://erepository.uonbi.ac.ke" + research.find("a")["href"]
        title = research.find("h4").text

        if None in (url, title):
            continue

        try:
            Research.objects.create(url=url, title=title, category=category)
            print(
                "{} - {} successfully added in category {}!".format(
                    title, url, category
                )
            )
        except:
            print("Research already scraped in the Database")


# Add the categories form the urls
def categorize_the_researches():
    """Create dynamic categories from the urls."""
    category_list = []

    for url in URL_LIST:
        category = url.split("&")[1]
        category_list.append(category)

    for item in category_list:
        category = item.split("=")[1]

    return category
