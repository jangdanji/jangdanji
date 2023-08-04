import requests
import pprint
import json
import random

SCRIPT = []

notionURL = 'https://api.notion.com/v1/databases/'
databaseID = '3c79de87e6274af69ca72efa3f9f1bfc'

DATABASE_URL = notionURL + databaseID

key = 'secret_xjdGY7ZHYhJfcT7PikV33Em1WrqcI9zXq44av9KfNb4'

payload = { "page_size": 100 }

response = requests.post(DATABASE_URL + '/query', json=payload, headers={
        'Authorization': f'Bearer {key}', "Notion-Version":'2022-06-28'})

data = response.json()

for i in data["results"] :
    SCRIPT.append(i["properties"]['sentance']['title'][0]['text']['content'])

if data['has_more'] == True: 

    isMore = True

    while True:
        next = { "start_cursor": data['next_cursor'], "page_size": 100}

        response = requests.post(DATABASE_URL + '/query', json=next, headers={
        'Authorization': f'Bearer {key}', "Notion-Version":'2022-06-28'})

        nextData = response.json()

        for i in nextData["results"] :
            SCRIPT.append(i["properties"]['sentance']['title'][0]['text']['content'])
            # print(len(SCRIPT))
        
        if nextData['has_more'] == False: break

print(f'총 {len(SCRIPT)}개의 데이터가 있습니다..')
print(random.choice(SCRIPT))

