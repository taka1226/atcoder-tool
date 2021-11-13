#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import shutil
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=dotenv_path)
load_dotenv()

login_url = "https://atcoder.jp/login"
question_url = input("question URL: ")

makefile_filepath = os.getenv('MAKEFILE_FILEPATH')
maincpp_filepath = os.getenv('MAINCPP_FILEPATH')


def get_sample():
    session = requests.session()
    res = session.get(login_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    #get csrf token
    csrf_token = soup.find('input', attrs={'name': 'csrf_token', 'type': 'hidden'})['value']


    session.post(
        login_url,
        data={
            'username': os.getenv('USERNAME'),
            'password': os.getenv('PASSWORD'),
            'csrf_token': csrf_token
        })

    res = session.get(question_url)

    soup = BeautifulSoup(res.text, 'html.parser')
    sample_soup = soup.select('.part > section > pre')

    os.makedirs("TestDir")
    for i in range(1, len(sample_soup)):
        if (sample_soup[0] == sample_soup[i]):
            break
        filename = (i - 1) // 2 + 1
        if (i % 2 == 1):
            filename = 'TestDir/' + str(filename) + '.test'
        else:
            filename = 'TestDir/' + str(filename) + '.out'
        with open(filename, 'w') as f:
            f.write(sample_soup[i].text)

def move_files():
    shutil.copyfile(makefile_filepath, "./Makefile")
    shutil.copyfile(maincpp_filepath, "./main.cpp")

if __name__ == '__main__':
    get_sample()
    move_files()
    print("Finished!")
