
import re
from pysle import isletool

# 아래와 같이 비슷한 소리의 자음, 모음을 분류화 시키고, 유니코드 순서에 맞춰서 "A B C D E .." 타입으로 교체해 주었다.

jaumtype = {
    'ㄱ' : 'ja1', 'ㄷ' : 'ja1', 'ㅂ' : 'ja1', 'ㅋ' : 'ja1', 'ㅌ' : 'ja1',
    'ㅍ' : 'ja1', 'ㄲ' : 'ja1', 'ㄸ' : 'ja1', 'ㅃ' : 'ja1',
    'ㅅ' : 'ja2', 'ㅈ' : 'ja2', 'ㅊ' : 'ja2', 'ㅆ' : 'ja2', 'ㅉ' : 'ja2',
    'ㄴ' : 'ja3', 'ㄹ' : 'ja3', 'ㅁ' : 'ja3',
    'ㅇ' : 'ja4', 'ㅎ' : 'ja4'}
moumtype = {
    'mo1' : ['ㅏ', 'ㅑ', 'ㅘ'],
    'mo2' : ['ㅓ', 'ㅕ', 'ㅝ','ㅗ', 'ㅛ'],
    'mo3' : ['ㅜ', 'ㅠ', 'ㅡ'],
    'mo4' : ['ㅣ', 'ㅟ', 'ㅢ'],
    'mo5' : ['ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅙ', 'ㅚ', 'ㅞ']}

# 유니코드 순서에 맞춘 초성, 중성, 종성 모음

# CHOSUNG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
#                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# JUNGSUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
#                 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# JONGSUNG = ['_', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ',
#                 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
#                 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


# 타입별로 교체한 최종 결과

CHOSUNG = ['A', 'A', 'C', 'A', 'A', 'C', 'C', 'A', 'A', 'B',
                'B', 'D', 'B', 'B', 'B', 'A', 'A', 'A', 'D']
JUNGSUNG = ['A', 'E', 'A', 'E', 'B', 'E', 'B', 'E', 'B', 'A',
                'E', 'E', 'B', 'C', 'B', 'E', 'D', 'C', 'C', 'D', 'D']



# 사용자가 단어를 입력할 때 2글자 기준으로 초성이 BB, 중성이 BE인 글자를 입력했다면
# 다른 단어 중에 중성이 BE로 일치하는 단어가 존재한다면 그 단어는 "라임"으로 인식할 것이다.
# 초성이 BB, 중성이 BE인 모두 일치하는 단어가 있다면 best일 것임


def chosung(word) :
  result = ''
  for w in word :
    if 0xAC00 <= ord(w) <= 0xD79D:
      start_value = ord(w[0]) - 0xAC00
      jong = start_value % 28
      jung = int(((start_value - jong) / 28) % 21)
      cho = int((((start_value - jong) / 28) - jung) / 21)
      result += CHOSUNG[cho]
    elif ord(w) == 10: result += '\n'
    elif w == ' ': result += ' '
  return result

def jungsung(word) :
  result = ''
  for w in word :
    if 0xAC00 <= ord(w) <= 0xD79D:
      start_value = ord(w[0]) - 0xAC00
      jong = start_value % 28
      jung = int(((start_value - jong) / 28) % 21)
      result += JUNGSUNG[jung]
    elif ord(w) == 10: result += '\n'
    elif w == ' ': result += ' '
  return result

# def jongsung(word) :
#   result = ''
#   for w in word :
#     if 0xAC00 <= ord(w) <= 0xD79D:
#       start_value = ord(w[0]) - 0xAC00
#       jong = start_value % 28
#       result += JONGSUNG[jong]
#   return result
  
# print(chosung('세탁소'))
# print(jungsung('세탁소'))
# print(jongsung('김나단천재'))

