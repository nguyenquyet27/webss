import math
from collections import defaultdict
import copy
import numpy as np
from collections import Counter


def compute_idf(corpus):
    num_docs = len(corpus)
    idf = defaultdict(lambda: 0)
    for doc in corpus:
        bow = Counter(doc)
        for word in bow.keys():
            idf[word] += 1

    for word, value in idf.items():
        idf[word] = 1 + math.log(num_docs / value)

    return idf


def compute_tf(corpus):
    tf = []
    for doc in corpus:
        n = len(doc)
        bow = Counter(doc)
        tf_ = {}
        for word, value in bow.items():
            tf_[word] = value / n
        tf.append(tf_)
    return tf


def compute_weight(tf, idf, tf_query):
    weight = list()

    for doc in tf:
        weight_ = list()
        for term in tf_query[0].keys():
            weight_.append(doc[term] * idf[term] if term in doc.keys() else 0)
        weight.append(weight_)
        #print(len(weight))

    weight_ = list()
    for key, value in tf_query[0].items():
        weight_.append(value * idf[key] if key in idf.keys() else 0)
    
    weight.append(weight_)

    return weight
