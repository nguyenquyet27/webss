import json


def name_distributor():
    lis = ["The gioi di dong", "FPT shop", "Hoang Ha mobile", "Vien Thong A", "Mai Nguyen"]
    k = ["thegioididong","fptshop", "hoanghamobile", "vienthonga", "mainguyen"]
    dis = []
    for i in range(0,len(lis)):
        dis.append({
            "id_dist": k[i],
            "dis": lis[i]
        })
    y = len(dis)
    result = {"item": []}
    for i in range(0, y):
        result["item"].append(dis[i])
    return result
    

def find_distributor(distributor):
    #distributor = "Fpt shop"
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except FileNotFoundError:
        json_data = {"test": []}

    data = []
    for i in dataset:
        data.append(dataset[i])
    n = len(data)
    Get_data = []
    for i in range(0,n):
        if (data[i]["Distributor"] == distributor):
            Get_data.append({
                    "id":  data[i]["id"],
                    "ProductName":  data[i]["ProductName"],
                    "Price" : data[i]["Price"],
                    "Company":  data[i]["Company"],
                    "Distributor":  data[i]["Distributor"],
                    "image":  data[i]["image"],
                    "link": data[i]["link"]
                })
    
    result = {"item": []}
    y = len(Get_data)
    for i in range(0, y):
        result["item"].append(Get_data[i])
    return result


def find_masp(masp):
    try:
        with open('home/datas.json') as json_dataset:
            dataset = json.load(json_dataset)
    except FileNotFoundError:
        json_data = {"test": []}

    data = []
    for i in dataset:
        data.append(dataset[i])
    n = len(data)
    Get_data = []
    for i in range(0,n):
        if (data[i]["masp"] == masp):
            Get_data.append({
                    "id":  data[i]["id"],
                    "ProductName":  data[i]["ProductName"],
                    "Price" : data[i]["Price"],
                    "Company":  data[i]["Company"],
                    "Distributor":  data[i]["Distributor"],
                    "image":  data[i]["image"],
                    "link": data[i]["link"]
                })
    
    result = {"item": []}
    y = len(Get_data)
    for i in range(0, y):
        result["item"].append(Get_data[i])
    return result