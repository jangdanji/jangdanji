import requests
import pprint
import time
from bs4 import BeautifulSoup 

txtPath = 'lyricsData\\lyrics\\balladID.txt'

for page in range(1, 1097):

  # 멜론 지니는 막아놓음 벅스는 뚫림
  url = f'https://music.bugs.co.kr/genre/kpop/ballad/total?tabtype=2&sort=default&nation=all&page={page}'

  # 발라드 1096페이지까지 있음

  response = requests.get(url)

  print(response.status_code)

  if response.status_code == 200:

    data = response.text
    
    # HTML 데이터를 BeautifulSoup 객체로 파싱
    soup = BeautifulSoup(data, 'html.parser')

    # pprint.pprint(soup)

    songs = soup.select('table.trackList tbody tr')

    print(len(songs))

    idList = []

    for song in songs :
      ID = song.get('trackid')
      idList.append(ID)

    print(idList)
    print(len(idList))
    print(str(page) + 'page 완료')

    with open(txtPath, 'a', encoding='utf-8') as file:
      for id in idList: file.write(id + '\n')
    
    time.sleep(5)

  else :
    print(response.json)
    print(str(page) + 'page 까지 완료')