import numpy as np
from . import tokenizing
from . import weight
import json
from collections import Counter

q = []
search = 0
stt = -1
more = 0


def sort_by_me(a):
    return a["cost"]


def sort_price(b):
    return b["Price1"]


def chuyen(st):
    xnew = st.split()[0]
    if (xnew == 'Unknow'):
        return 0
    x = ""
    for i in range(0, len(xnew)):
        if xnew[i] != '.':
            x = x + xnew[i]
    return int(x)


def process_search(p):
    q.append(p)
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
        terms = tokenizing.get_terms(name)
        # bow = Counter(terms)
        corpus.append(terms)

    # compute tf, idf of data
    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)

    # handling query
    query = tokenizing.get_terms(query)
    query_len = len(query)

    tf_query = weight.compute_tf([query])

    # compute TF-IDF for both data and query
    represent_tfidf = weight.compute_weight(tf, idf, tf_query)

    # compute cosine similarity
    k = len(represent_tfidf) - 1
    b = np.array(represent_tfidf[k])
    normb = np.linalg.norm(b)
    Get_data = []
    search = 1

    for i in range(0, k):
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        if (norma != 0):
            cos = dot / (norma * normb)
            if ((query_len == 1 and cos > 0) or (query_len > 1 and cos > 0.3)):
                Get_data.append({
                    "cost": cos,
                    "id":  data[i]["id"],
                    "ProductName":  data[i]["ProductName"],
                    "Price1":  chuyen(data[i]["Price"]),
                    "Price": data[i]["Price"],
                    "Company":  data[i]["Company"],
                    "Distributor":  data[i]["Distributor"],
                    "image":  data[i]["image"],
                    "link": data[i]["link"]
                })
    Get_data.sort(key=sort_by_me, reverse=True)
    number = 12
    y = len(Get_data)
    if (y > 12):
        more = 1
    else:
        more = 0
    page = 1
    result = {"item": [], "search": search, "stt": stt, "more": more, "page": page}
    for i in range(0, min(number, y)):
        result["item"].append(Get_data[i])
    #result["item"].sort(key=sort_price, reverse=False)
    return result

def process_searchpage1():
    n = len(q)
    p = q[n-1]
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
        terms = tokenizing.get_terms(name)
        # bow = Counter(terms)
        corpus.append(terms)

    # compute tf, idf of data
    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)

    # handling query
    query = tokenizing.get_terms(query)
    query_len = len(query)

    tf_query = weight.compute_tf([query])

    # compute TF-IDF for both data and query
    represent_tfidf = weight.compute_weight(tf, idf, tf_query)

    # compute cosine similarity
    k = len(represent_tfidf) - 1
    b = np.array(represent_tfidf[k])
    normb = np.linalg.norm(b)
    Get_data = []
    search = 1

    for i in range(0, k):
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        if (norma != 0):
            cos = dot / (norma * normb)
            if ((query_len == 1 and cos > 0) or (query_len > 1 and cos > 0.3)):
                Get_data.append({
                    "cost": cos,
                    "id":  data[i]["id"],
                    "ProductName":  data[i]["ProductName"],
                    "Price1":  chuyen(data[i]["Price"]),
                    "Price": data[i]["Price"],
                    "Company":  data[i]["Company"],
                    "Distributor":  data[i]["Distributor"],
                    "image":  data[i]["image"],
                    "link": data[i]["link"]
                })
    Get_data.sort(key=sort_by_me, reverse=True)
    number = 12
    y = len(Get_data)
    if (y > 12):
        more = 1
    else:
        more = 0
    page = 1
    result = {"item": [], "search": search, "stt": stt, "more": more, "page": page}
    for i in range(0, min(number, y)):
        result["item"].append(Get_data[i])
    #result["item"].sort(key=sort_price, reverse=False)
    return result

def process_searchpage2():
    n = len(q)
    p = q[n-1]
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
        terms = tokenizing.get_terms(name)
        # bow = Counter(terms)
        corpus.append(terms)

    # compute tf, idf of data
    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)

    # handling query
    query = tokenizing.get_terms(query)
    query_len = len(query)

    tf_query = weight.compute_tf([query])

    # compute TF-IDF for both data and query
    represent_tfidf = weight.compute_weight(tf, idf, tf_query)

    # compute cosine similarity
    k = len(represent_tfidf) - 1
    b = np.array(represent_tfidf[k])
    normb = np.linalg.norm(b)
    Get_data = []
    search = 1

    for i in range(0, k):
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        if (norma != 0):
            cos = dot / (norma * normb)
            if ((query_len == 1 and cos > 0) or (query_len > 1 and cos > 0.3)):
                Get_data.append({
                    "cost": cos,
                    "id":  data[i]["id"],
                    "ProductName":  data[i]["ProductName"],
                    "Price1":  chuyen(data[i]["Price"]),
                    "Price": data[i]["Price"],
                    "Company":  data[i]["Company"],
                    "Distributor":  data[i]["Distributor"],
                    "image":  data[i]["image"],
                    "link": data[i]["link"]
                })
    Get_data.sort(key=sort_by_me, reverse=True)
    y = len(Get_data)
    number = 24
    if (y > 12):
        more = 1
    else:
        more = 0
    page = 2
    result = {"item": [], "search": search, "stt": stt, "more": more, "page": page}
    for i in range(12, min(y,number)):
        result["item"].append(Get_data[i])
    #result["item"].sort(key=sort_price, reverse=False)
    return result


def sort_belon():
    n = len(q)
    p = q[n-1]
    result = process_search(p)
    result["stt"] = 0
    result["item"].sort(key=sort_price, reverse=False)
    return result


def sort_lonbe():
    n = len(q)
    p = q[n-1]
    result = process_search(p)
    result["stt"] = 1
    result["item"].sort(key=sort_price, reverse=True)
    return result

def sort_belon2():
    result = process_searchpage2()
    result["stt"] = 0
    result["item"].sort(key=sort_price, reverse=False)
    return result


def sort_lonbe2():
    result = process_searchpage2()
    result["stt"] = 1
    result["item"].sort(key=sort_price, reverse=True)
    return result

#distributor


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
