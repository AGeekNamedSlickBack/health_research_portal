"""Natural language processing module."""
import urllib.request

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def nlp():
    """Process researches abstracts for key words."""
    response = urllib.request.urlopen(
        # 'http://erepository.uonbi.ac.ke/handle/11295/106481'
        # 'http://ir.jkuat.ac.ke/handle/123456789/2126'
        # 'http://ir.jkuat.ac.ke/handle/123456789/5130'
        # 'https://www.cdc.gov/malaria/diagnosis_treatment/diagnosis.html'
        # 'http://erepository.uonbi.ac.ke/handle/11295/106526'
        # 'http://erepository.uonbi.ac.ke/handle/11295/107224'
        # 'http://erepository.uonbi.ac.ke/handle/11295/107202'
        # 'http://erepository.uonbi.ac.ke/handle/11295/107761'
        # "http://erepository.uonbi.ac.ke/handle/11295/104306"
        # "http://erepository.uonbi.ac.ke/handle/11295/109257"
        "http://erepository.uonbi.ac.ke/handle/11295/106481"
    )  # TODO Fetch urls from db
    html = response.read()

    text = BeautifulSoup(html, "html.parser")
    text = text.get_text()  # TODO parse just the abstract, not whole page
    #  print(text)

    # Remove stop words like 'a' 'the' 'an'
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)

    # Remove punctuations and lower upper cases
    word_tokens = [word.lower() for word in word_tokens if word.isalpha()]

    filtered_text = [w for w in word_tokens if not w in stop_words]
    filtered_text = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_text.append(w)

    count_word_frequency = nltk.FreqDist(filtered_text)
    count_word_frequency = count_word_frequency.most_common(
        10
    )  # Gets most frequent words

    print(count_word_frequency)

nlp()
