import pandas as pd
import numpy as np
from . import tokenizing
from . import weight

import json
from collections import Counter
def sort_by_me(a):
    return a["cost"]

def process_search(p):
    x = ""
    for i in p:
        x = x + i
    #x = "iPhone Xs Max";
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except  FileNotFoundError:
        json_data = {"test":[]} 
    data=[]
    for i in dataset:
        data.append(dataset[i])
 
    ProductName = list()
    for i in data:
        ProductName.append(i["ProductName"])
    corpus = list()
    for name in ProductName:
        terms = tokenizing.get_terms(name,lemmatize=False, stemming=False)
        bag_of_words = Counter(terms)
        corpus.append(bag_of_words)

    #xu li input
    x_ = tokenizing.get_terms(x,lemmatize=False, stemming=False)
    bag = Counter(x_)
    corpus.append(bag)
    n = len(x_)
    #compute tf-idf
    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)

    represent_tfidf = weight.compute_weight(tf, idf)

    #compute cosi
    cosi = list()
    k = len(represent_tfidf) - 1
    b = np.array(represent_tfidf[k])
    normb = np.linalg.norm(b)
    ValueOfItem = []
    Get_data = []
    dem = 0
    for i in range(0,k):
        dem = dem + 1
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        cos = dot / (norma * normb)
        if ((n == 1 and cos > 0) or (n > 1 and cos > 0.3)) :
            
            Get_data.append({
                "cost" : cos,
                "id"            :  dem,
                "ProductName"   :  data[i]["ProductName"],
                "Price"         :  data[i]["Price"],
                "Company"       :  data[i]["Company"],
                "Distributor"   :  data[i]["Distributor"],
                "image"         :  data[i]["image"]
            })
    Get_data.sort(key=sort_by_me , reverse = True)
    number = 10
    y = len(Get_data) 
    result = {"item":[]}
    for i in range(0,min(number,y)):
        result["item"].append(Get_data[i])
    return result

def find_id(id_product):
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except  FileNotFoundError:
        dataset = {"test":[]} 
    data=[]
    dem = 0 
    for i in dataset:
        dataset[i]["id"] = dem + 1
        data.append(dataset[i])

    for i in range(0,len(data)):
        if i+1 == id_product:
            return {
                "id"            :  data[i]["id"],
                "ProductName"   :  data[i]["ProductName"],
                "Price"         :  data[i]["Price"],
                "Company"       :  data[i]["Company"],
                "Distributor"   :  data[i]["Distributor"],
                "image"         :  data[i]["image"]
        }