import os.path
from os import path
import json
import requests
import re
from bs4 import BeautifulSoup

def fileExist(filename):
    return path.exists(filename)


def parserJson(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        return data

responce = requests.get("https://readmanga.me/19_days___one_day")

soup = BeautifulSoup(responce.text, 'lxml')
soup2= soup.find("div", class_="subject-actions").h4.a.text
print(soup2)
chepter = re.findall(r'\w+$', soup2)
print(chepter)
