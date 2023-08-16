from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver import Keys
from selenium import webdriver
import time

def fetch_image():
    service = webdriver.chrome.service.Service('C:/')
    browser = webdriver.Chrome(service=service)

if __name__ == '__main__':
    fetch_image()