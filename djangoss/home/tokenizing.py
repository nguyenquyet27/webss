from nltk.corpus import stopwords
import re
import contractions
import unicodedata
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


"""
    remove punctuation (and number) in string of text
"""


def remove_punctuation(text, remove_digit=False):
    if remove_digit:
        pattern = r'[^a-zA-z\s]'
    else:
        pattern = r'[^a-zA-z0-9\s]'

    text = re.sub(pattern, '', text)
    return text


"""
    remove non-ASCII characters from list of tokenized words
"""


def remove_non_ascii(words):
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


"""
    remove stop words from list of tokenized words
"""


# def remove_stopwords(words):
#     new_words = []
#     for word in words:
#         if word not in stopwords.words('english'):
#             new_words.append(word)
#     return new_words


def get_terms(text, expand_contraction=True, remove_punc=True, remove_digit=False, remove_non_ACSII=True):
    """ convert all characters to lowercase in string of text"""

    text = text.lower()

    """ replace contractions in string of text"""

    if expand_contraction:
        text = contractions.fix(text)

    if remove_punc:
        text = remove_punctuation(text, remove_digit=remove_digit)

    terms = nltk.word_tokenize(text)

    if remove_non_ACSII:
        terms = remove_non_ascii(terms)
    # terms = remove_stopwords(terms)

    return terms
