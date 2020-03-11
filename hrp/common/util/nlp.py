"""Natural language processing module."""
import urllib.request

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


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
        "http://erepository.uonbi.ac.ke/handle/11295/104306"
    )  # TODO Fetch urls from db
    html = response.read()

    text = BeautifulSoup(html, "html.parser")
    text = text.get_text()  # TODO parse just the abstract, not whole page
    #  print(text)

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

    print(count_word_frequency)

    # for word in count_word_frequency:
    #     print(word)
    # word = [[j for j in i if type(j) == str]
    #                     for i in count_word_frequency]
    # print(','.join(str(word)))
    # print(word)
    # emp_list = []
    # for char in word:
    #     single = ','.join(char)
    #     # print(single)
    #     emp = emp_list.append(single)
    #     print(emp)
    # keywords = [['receptor'], ['diagnosis']]
    # val =[value for value in keywords if value in word]
    # print(','.join(val[0]))
    # for words in word:
    #     if 'malaria' in words:
    #         print('Ye')
    #     else:
    #         return
    # return count_word_frequency
    # for word, value in count_word_frequency.items():
    #     print('{} : {}'.format(word, value))

    # cat = count_word_frequency[0]
    # print(cat)
    # # Splitting the list
    # if 'Malaria' in cat:
    #     print('Yes')
    # else:
    #     print('Hell naw')


nlp()
