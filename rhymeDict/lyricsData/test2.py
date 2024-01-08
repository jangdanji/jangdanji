
import re

file_path = "lyricsData\ISLEdict.txt"

# 파일을 읽기 모드('r')로 엽니다.
with open(file_path, 'r', encoding='utf-8') as file:
    # 파일을 줄 단위로 읽어 리스트로 저장합니다.
    lines = file.readlines()

# print(lines)

prevWord = ''

for l in lines:
    word = re.search('^([0-9a-z_-]+)', l)
    
    if prevWord == word.group(0):
        print(word.group(0))
    
    prevWord = word.group(0)

    