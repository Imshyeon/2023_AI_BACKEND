import os
import sys
import urllib.request
from pymongo import MongoClient
import requests

def get_naver_data(query1, query2):
    url = "https://openapi.naver.com/v1/datalab/shopping/categories"
    headers = {
        "X-Naver-Client-Id" : "rFeMl0bo1eJokxWnlq4h",
        "X-Naver-Client-Secret" : "7jwsOAo10K",
        "Content-Type" : "application/json"
    }

    body = {
        "startDate":"2017-08-01",
        "endDate":"2017-09-30",
        "timeUnit":"month",
        "category": [
                    {"name":query1,"param":["50000000"]},
                    {"name": query2, "param": ["50000002"]}
                    ],
        "device":"pc",
        "ages":["20","30"],
        "gender":"f"
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200 :
        return response.json()
    else:
        return None

def save_naver_data_to_mongo(query1,query2):
    data=get_naver_data(query1,query2)
    print(type(data),data)
    if data:
        client = MongoClient("mongodb://localhost:27017/")
        db = client['mydb']
        collection = db['my_naver']
        collection.insert_one(data)
        client.close()


if __name__ == '__main__':
    save_naver_data_to_mongo("패션의류","화장품/미용")


# {"name":query2, "param":["50000002"]}],