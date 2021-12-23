import sys
import json

import requests
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os

trancerate_text = open('trancerate.txt', 'w')

# text の取得
def getText():
    with open(sys.argv[1], 'rb') as f:
        data = f.readlines()[1:5]
        return data

def getTransrateSentence(data):
        for sentence in data:
            print(sentence["text"])
            trancerate_text.write(sentence["text"])
            


url = os.getenv('URL')
auth_key = os.getenv('AUTH_KEY')
text = getText()

target_lang = 'JA'
data = {'auth_key': auth_key, 'text': text, 'target_lang': target_lang}
response = requests.post(url, data)
json_str = response.text
json_dict = json.loads(json_str)
print(json_dict["translations"])

getTransrateSentence(json_dict["translations"])

print(response.text)

