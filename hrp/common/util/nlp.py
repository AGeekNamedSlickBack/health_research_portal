"""Natural language processing module."""
import urllib.request

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

KEYWORDS = [
    ["plasmodium"],
    ["diagnosis"],
    ["diagnostic"],
    ["food"],
    ["laboratories"],
    ["treatment"],
    ["control"],
    ["location"],
    ["county"],
    ["isolates"],
    ["fever"],
    ["salmonella"],
    ["water"],
    ["climate",],
    ["hpv"],
]


def nlp():
    """Process researches abstracts for key words."""
    response = urllib.request.urlopen(
        "https://ir-library.ku.ac.ke/handle/123456789/4417"
    )  # TODO Fetch urls from db
    html = response.read()

    text = BeautifulSoup(html, "html.parser")
    # text = text.get_text()  # TODO parse just the abstract, not whole page
    #  print(text)
    import pdb; pdb.set_trace()
    abstract = text.find("div", class_="simple-item-view-description item-page-field-wrapper table").find("div")
    # Remove stop words like 'a' 'the' 'an'
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(str(abstract))

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
    get_keywords = [
        [j for j in i if type(j) == str] for i in count_word_frequency
    ]
    keyword = [
        _keyword for _keyword in KEYWORDS if _keyword in get_keywords
    ]  # Compares keywords with most_common words
    keyword = ",".join(keyword[0])  # Gets the intersect
    # keyword = "{}:{}".format(category, keyword)
    import pdb

    pdb.set_trace()

    print(count_word_frequency)


nlp()
