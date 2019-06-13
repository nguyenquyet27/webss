import numpy as np
from . import tokenizing
from . import weight
import json
from collections import Counter


def sort_by_me(a):
    return a["cost"]
def sort_price(b):
    return b["Price"]

def prepare():
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except FileNotFoundError:
        json_data = {"test": []}
    
    data = []
    for i in dataset:
        data.append(dataset[i])

    ProductName = list()
    for i in data:
        ProductName.append(i["ProductName"])

    corpus = list()
    for name in ProductName:
        terms = tokenizing.get_terms(name, lemmatize=False, stemming=False)
        bow = Counter(terms)
        corpus.append(bow)

    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)
    # return tf and idf

    return {
        "corpus": corpus
    }


def process_search(p):
    query = ""
    for i in p:
        query = query + i
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except FileNotFoundError:
        json_data = {"test": []}

    data = []
    for i in dataset:
        data.append(dataset[i])

    ProductName = list()
    for i in data:
        ProductName.append(i["ProductName"])

    corpus = list()
    for name in ProductName:
        terms = tokenizing.get_terms(name, lemmatize=False, stemming=False)
        bow = Counter(terms)
        corpus.append(bow)


    # compute tf, idf of data
    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)
     
    # delete code from line 49 to 70

    # handling query
    query_ = tokenizing.get_terms(query, lemmatize=False, stemming=False)
    bow_query = Counter(query_)
    query_len = len(bow_query)

    tf_query = weight.compute_tf_query(bow_query)


    # get tf, idf from prepare()
    # compute TF-IDF for both data and query
    represent_tfidf = weight.compute_weight(tf, idf, tf_query)


    # compute cosine similarity
    cosi = list()
    k = len(represent_tfidf) - 1
    b = np.array(represent_tfidf[k])
    normb = np.linalg.norm(b)
    ValueOfItem = []
    Get_data = []
    #dem = 0
    for i in range(0, k):
        #dem = dem + 1
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        cos = dot / (norma * normb)
        if ((query_len == 1 and cos > 0) or (query_len > 1 and cos > 0.3)):

            Get_data.append({
                "cost": cos,
                "id":  data[i]["id"],
                "ProductName":  data[i]["ProductName"],
                "Price":  data[i]["Price"],
                "Company":  data[i]["Company"],
                "Distributor":  data[i]["Distributor"],
                "image":  data[i]["image"],
                "link": data[i]["link"]
            })
    Get_data.sort(key=sort_price, reverse=False)
    Get_data.sort(key=sort_by_me, reverse=True)
    number = 10
    y = len(Get_data)
    result = {"item": []}
    for i in range(0, min(number, y)):
        result["item"].append(Get_data[i])
    result["item"].sort(key=sort_price, reverse=False)
    return result


def find_id(id_product):
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except FileNotFoundError:
        dataset = {"test": []}
    data = []
    dem = 0
    for i in dataset:
        dataset[i]["id"] = dem + 1
        data.append(dataset[i])

    for i in range(0, len(data)):
        if i+1 == id_product:
            return {
                "id":  id_product,
                "ProductName":  data[i]["ProductName"],
                "Price":  data[i]["Price"],
                "Company":  data[i]["Company"],
                "Distributor":  data[i]["Distributor"],
                "image":  data[i]["image"],
                "link": data[i]["link"]
            }
