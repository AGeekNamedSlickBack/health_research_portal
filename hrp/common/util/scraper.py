"""Create the web scraper."""
import requests
from bs4 import BeautifulSoup

from hrp.researches.models import Research


def scraper():
    """Scrape certified repositories."""
    URL_LIST = [
        'http://erepository.uonbi.ac.ke/discover?scope=%2F&query=cancer&submit=&rpp=10&sort_by=dc.date.issued_dt&order=desc',
        'http://erepository.uonbi.ac.ke/discover?scope=%2F&query=malaria&submit=&rpp=10&sort_by=dc.date.issued_dt&order=desc',
    ]

    for URL in URL_LIST:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='main-container')
    researches = results.find_all(class_='col-sm-9 artifact-description')
    for research in researches:
        url = 'http://erepository.uonbi.ac.ke' + research.find('a')['href']
        title = research.find('h4').text

        if None in (url, title):
            continue

        try:
            Research.objects.create(
                url=url,
                title=title,
            )
            print('{} - {} successfully added!'.format(title, url))
        except:
            print('Research already scraped in the Database')
