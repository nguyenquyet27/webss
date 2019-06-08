import math
from collections import defaultdict
import copy
import numpy as np


def compute_idf(corpus):
    num_docs = len(corpus)
    idf = defaultdict(lambda: 0)
    for doc in corpus:
        for word in doc.keys():
            idf[word] += 1

    for word, value in idf.items():
        idf[word] = 1 + math.log(num_docs / value)
    return idf


def compute_tf(corpus):
    tf = copy.deepcopy(corpus)
    for doc in tf:
        for word, value in doc.items():
            doc[word] = value / len(doc)

    return tf


def compute_weight(tf, idf, tf_query):
    weight = list()

    for doc in tf:
        weight_ = list()
        for term in tf_query:
            weight_.append(doc[term] * idf[term] if term in doc.keys() else 0)
        weight.append(weight_)
        #print(len(weight))

    weight_ = list()
    for key, value in tf_query.items():
        weight_.append(value * idf[key] if key in idf.keys() else 0)
    weight.append(weight_)

    return weight


def compute_tf_query(query):
    tf = {}
    for word, value in query.items():
        tf[word] = value / len(query)
    return tf
