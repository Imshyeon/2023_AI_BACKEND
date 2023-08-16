import os
import sys
import urllib.request
import requests
from pymongo import MongoClient


def get_naver_data(query):
        url = "https://openapi.naver.com/v1/datalab/shopping/categories"
        headers = {
        "X-Naver-Client-Id":  "rFeMl0bo1eJokxWnlq4h",
        "X-Naver-Client-Secret": "7jwsOAo10K",
        "Content-Type" : "application/json"
        }
        body = {
            "startDate": "2017-08-01",
            "endDate": "2017-09-30",
            "timeUnit": "month",

            "category": [
                {"name": query, "param": ["50000000"]}
            ],
            "device": "pc",
            "ages": ["20", "30"],
            "gender": "f"
        }
        response =requests.post(url, headers=headers, json=body)
        if response.status_code ==200:
            return response.json()
        else:
            return None

def   save_naver_data_to_mongo(query):
    data = get_naver_data(query)
    print(type(data),data) #type : dict
    if data:
            client = MongoClient("mongodb://localhost:27017/")
            db = client['mydb']
            collection = db['naver']
            collection.insert_one(data)
            client.close()


if __name__ == '__main__':
    save_naver_data_to_mongo("패션의류" )
