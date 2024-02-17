import json
import re

with open('data\\kkutuWords.json', 'r', encoding='utf-8') as f:
  kkutuWords = json.load(f)

print(type(kkutuWords))

trashWords = []

for word in kkutuWords:
  
  check = re.search('[ㄱ-ㅎ]', word)

  if check:
    trashWords.append(word)
    print(word)

for word in trashWords:
  kkutuWords.remove(word)

print(kkutuWords)

# JSON 파일로 데이터를 저장합니다.
with open('kkutuWords.json', 'w', encoding='utf-8') as f:
    json.dump(kkutuWords, f, ensure_ascii=False, indent=4)