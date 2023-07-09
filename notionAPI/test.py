import requests
import pprint
import json

notionURL = 'https://api.notion.com/v1/databases/'
databaseID = '3c79de87e6274af69ca72efa3f9f1bfc'

DATABASE_URL = notionURL + databaseID

key = 'secret_xjdGY7ZHYhJfcT7PikV33Em1WrqcI9zXq44av9KfNb4'

payload = { "page_size": 100 }

# response = requests.post(DATABASE_URL + '/query', json=payload, headers={
#            'Authorization': f'Bearer {key}', "Notion-Version":'2022-06-28'})

inputData ={ "title": [
        {
            "text": {
                "content": "띵언 스크립트"
            }
        }
    ],
    "description": [
        {
            "text": {
                "content": "인생은 무엇인가.."
            }
        }
    ],
    "properties": {
        'sentance' : {
            "type" : "title",
            "title" : [{ "type": "text", "text": { "content": "Tomatoes" } }]
        }
    }       
}



response = requests.patch(
    DATABASE_URL,
    headers={
            'Authorization': f'Bearer {key}',
            "accept": "application/json",
            'Notion-Version' : '2022-06-28',
            'Content-Type' : 'application/json'},
    data=json.dumps(inputData))

if response.status_code == 200:
    jsonData = response.json()
else:
    print('호출 실패')
    print(response)
    pprint.pprint(response.json())
    exit()



""" 데이터 갯수 """
# dataLength = len(jsonData["results"])
# print(f"총 {dataLength}개의 데이터가 있습니다..")
print(response)
pprint.pprint(response.json())

# for i in jsonData["results"] :
#     pprint.pprint(i["properties"])

# ['sentance']['title'][0]['text']['content']

