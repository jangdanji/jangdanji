import re
import pprint
import json

from g2pk import G2p as g2pKo # g2p
from g2p_en import G2p as g2pEn
from decompose import chosung, jungsung

# 긁어온 가사들이 있는 JSON 파일을 읽기
with open(r'lyricsData/rawData.json', 'r', encoding='utf-8') as file:
    rawLyricsData = json.load(file)

g2p = g2pKo()

## 문제 1 : 영어 + 한글 조합에서 구개음화 발동이 안걸림

t = g2p('핏해')
print(t)
exit()

# 데이터 작업

for song in rawLyricsData :

  # 특수문자 제거, trim
  # originalText = re.sub(r'[^\w\s]', '', song['lyrics']).strip()
  originalText = re.sub(r'[^가-힣 ]+', 'X', song['lyrics']).strip()

  print(originalText)

  # 발음 텍스트 list, 초성 텍스트 list, 중성 텍스트 list
  nomalizedText = g2p(originalText)
  choText = chosung(nomalizedText)
  jungText = jungsung(nomalizedText)
  
  # allLyricsData에 가공해서 다시 담기
  song["lyrics"] = originalText.split('\n') # list에 가사 한 줄씩 
  song["chosung"] = choText.split('\n') # 초성 타입 데이터 한 줄씩
  song["jungsung"] = jungText.split('\n') # 중성 타입 데이터 한 줄씩

  # print('원본 텍스트 : ')
  # print(originalText); print()
  # print('발음 텍스트 : ')
  # print(nomalizedText); print()
  # print('자음 타입 : ')
  # print(choText); print()
  # print('모음 타입 : ')
  # print(jungText); print()

# pprint.pprint(rawLyricsData)

# # JSON 파일 읽고, 쓰기 (읽어온 데이터 + 지금 생성한 데이터)
# with open(r'lyricsData/processedData.json', 'r', encoding='utf-8') as file:
#     original = json.load(file)
# with open(r'lyricsData/processedData.json', 'w', encoding='utf-8') as file:
#     json.dump(original + rawLyricsData, file, ensure_ascii=False, indent=4)

