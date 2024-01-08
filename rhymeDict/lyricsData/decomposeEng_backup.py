

jaumTypeEn = { 
    "t" : "A", # ㅌ
    "b" : "A", # ㅂ
    "d" : "A", # ㄷ
    "f" : "A", # ㅍ
    "g" : "A", # ㄱ
    "v" : "A", # ㅂ
    "ð" : "A", # ㄷ th
    "ɵ" : "A", # ㄸ th
    "k" : "A", # ㅋ
    "p" : "A", # ㅍ

    "z" : "B", # ㅈ로 알고있지만 ㅅ소리가 큰듯
    "ʒ" : "B", # ㅈ treasure, vision, genre
    "dʒ" : "B", # ㅈ judge, bridge, major
    "tʃ" : "B", # ㅊ cheese, watch
    "s" : "B", # ㅅ

    "l" : "C", # ㄹ은 그냥 유음이라서 없는걸로 치고 나중에 초성칸이 비었으면 ㅇ으로 대체하도록 ㄱㄱ
    "r" : "C", # 난 r발음이 ㄹ보단 ㅇ이라고 생각함.. 심지어 앞 단어에서 끝소리가 넘어올 수 있음 
    "ɹ" : "C", # 
    "m" : "C", # ㅁ
    "n" : "C", # ㄴ
    
    "h" : "D", # ㅎ
    "j" : "D", # y 는 모음과 필수로 붙어 다니기때문에 아무것도 아닌 취급을 받을거임
    "w" : "D", # w 는 모음과 필수로 붙어 다니기때문에 아무것도 아닌 취급을 받을거임
    "ɾ" : "D", # r ㅇ
    "ŋ" : "D", # ㅇ ng발음

    "aʊ" : "A", # ㅏ house, mouse, out, cloud, now
    "ɑ" : "A", # ㅏ father, balm, calm, park
    "ɑɪ" : "A", # ㅏ eye, night, time, price
    "a" : "A", # ㅏ

    "ɔi" : "B", # ㅗ boy, coin, enjoy, choice
    "ɔ" : "B", # ㅗ thought, call, saw, bought
    "o" : "B", # ㅗ
    "oʊ" : "B", # ㅗ go, boat, know, show
    "ɝ" : "B", # ~r ㅓ bird, word, hurt, learn
    "ɚ" : "B", # ~r ㅓ teacher, color, doctor, brother
    "ʌ" : "B", # ㅓ cup, luck, cut, bus
    "ə" : "B", # ㅓ 중성음임 schwa라고함 근데 "ㅓ"의 사례가 더 많은것 같아서 "ㅓ"로 하자 computer

    "u" : "C", # ㅜ food, blue 
    "ʊ" : "C", # ㅜ book, look, push, full
    "l̩" : "C", # ~ㅡㄹ bottle, battle, little
    "n̩" : "C", # ~ㅡㄴ button, certain, listen

    "i" : "D",
    "ɪ" : "D", # ㅣ ship, lip, hit

    "e" : "E", # ㅔ
    "ei" : "E", # ㅔㅣ eight, neighbor
    "ɛ" : "E", # ㅔ pen, bed, next, let
    "æ" : "E", # ㅐ cat, man, hat, trap
    "ae" : "E", # ㅐ æ랑 거의 유사하다함

    " " : " "
}

# 이중 모음이 존재하는 경우 알파벳 하나 더 붙였음.. 이중 모음이 영어 음운 변동에서 예외가 생길 수 있음..
ipa2k = { 

    "dʒ" : "ㅈ",
    "ae" : "ㅐ",
    "tʃ" : "ㅊ",
    "aʊ" : "ㅏ",
    "ɑɪ" : "ㅏ",
    "ɔi" : "ㅗ",
    "oʊ" : "ㅗ",
    "ei" : "ㅔ",
    "l̩" : "ㅡㄹ",
    "n̩" : "ㅡㄴ",

    "g" : "ㄱ",
    "d" : "ㄷ",
    "ð" : "ㄷ",
    "b" : "ㅂ",
    "v" : "ㅂ",
    "k" : "ㅋ",
    "t" : "ㅌ",
    "f" : "ㅍ",
    "p" : "ㅍ",
    "ɵ" : "ㄸ",

    "z" : "ㅅ",
    "ʒ" : "ㅈ",
    
    
    "ʃ" : "ㅅ",
    "s" : "ㅅ",

    "l" : "ㄹ",
    "ɾ" : "ㄹ",
    "m" : "ㅁ",
    "n" : "ㄴ",
    
    "h" : "h",
    "r" : "r",
    "ɹ" : "r",
    
    "ŋ" : "ㅇ",

    "j" : "y",
    "w" : "w", 

    "ɑ" : "ㅏ",
    "a" : "ㅏ",
    "ɔ" : "ㅗ",
    "o" : "ㅗ",
    "ɝ" : "ㅓ",
    "ɚ" : "ㅓr",
    "ʌ" : "ㅓ",
    "ə" : "ㅓ",
    "u" : "ㅜ", 
    "ʊ" : "ㅜ",
    "i" : "ㅣ",
    "ɪ" : "ㅣ",
    "e" : "ㅔ",
    "ɛ" : "ㅔ",
    "æ" : "ㅐ",
    " " : " "
}

"""
개발 일지 :
  단어 하나의 ipa만 추출하는 lookup말고, 문장 단위로 추출하는 transcribe 기능으로 해야함
  왜냐하면 인수에 shortest, longest를 설정할 수 있는데 shortest를 하면 가장 짧은 발음 음절로 추출해줌
  really같은 경우는 3음절도 될 수 있지만 보통 노래할땐 발음이 빠르니 2음절로 발음함
"""

from pysle import isletool
from pysle import phonetics
import re
import join

isle = isletool.Isle('lyricsData\ISLEdict.txt')
"""
사전 수정 내역 :
  a 단독으로 있는거 ei -> ə

"""



# 가사 예외 경고 : 가끔 백보컬을 괄호안에 넣어놓는 경우가 있음 () 
# you're haven't 등의 upperstrophy 어떻게 할거?
# s가 h를 만나면 ㅅ발음 끝소리 이동

# - 예외 저장소 

# r들어간 단어에 음절이 하나 더 들어가있음
# every : [['ˈɛ'], ['v', 'ɚ'], ['i']] 
# here, every, really 수정 완료

# burned in

# d와 y가 만나면 ㅈ발음


# 영어는 schwa 발음이 좀 많아서 라임을 좀 관대하게 설정해도될듯?

# a라던가 한글자면 알파벳 그대로 발음함;;;;

# holdin' 같은 경우는 in'을 ing로 바꾸는 작업이 필요한듯

# here's It's let's

# only stupid



# it은 t 끝소리가 안넘어가는 이유좀..?  앞에서 받아올때도 안넘어옴


weekJaum = {'ㅇ' : 'r',
            'ㅎ' : 'h',
            'ㄴ' : 'n',
            'ㅁ' : 'm',
            'ㄹ' : 'l',
            'ㅅ' : 's',
            'ㅈ' : 'dg',
            'ㅊ' : 'ch'}

lyrics = """
what a day
"""


# sentence = "i want a apple"
# phoneList = isle.transcribe(sentence, "shortest")
# print(phoneList)


lyrics = re.sub('[?!.,]', '', lyrics)
lyrics = lyrics.replace('in\'', 'ing')
# lyrics = lyrics.replace('\'', '')

# print(lyrics)

lyricsList = lyrics.strip().split('\n')

for index, oneLine in enumerate(lyricsList):

  lineResult = ''

  oneLine = isle.transcribe(oneLine, "shortest")
  print(oneLine)

  for oneWord in oneLine.split(' '):

    jamoWords = ''

    for word in oneWord:
      jamoWords += ipa2k[word]

    print(f'{jamoWords} : 원본')
    
    exit()

    
    # 쓸데없는 기호 제거하기
    for result in g2pResult:
      for r in result:
        r = re.sub('[˺ˌ.ˈ#]', '', r)
        jamoWords += ipa2k[r]
    
    # # 예외 처리 보관함
    # if sCheck: jamoWords += 'ㅅ'

    print(f'{jamoWords} : 원본')

    # 첫 음절, 중간, 마지막 음절 중복 체크
    
    # 첫
    chosungNesting = re.match('^[ㄱ-ㅎ]{2,}[ㅏ-ㅣ]', jamoWords)
    if chosungNesting != None:
      target = chosungNesting.group(0)
      # print(target)

      for w, value in weekJaum.items():
        if len(target) < 3: break # 2자가 되었다면 break
        target = target.replace(w, value)
        
      jamoWords = re.sub('^[ㄱ-ㅎ]{2,}[ㅏ-ㅣ]', target, jamoWords)

      # print(f'{jamoWords} : 초성 자음 중복 처리하기')

    # 중간
    jongsungNesting = re.search('[ㄱ-ㅎ]{2,}$', jamoWords)
    if jongsungNesting != None:
      target = jongsungNesting.group(0)

      for w, value in weekJaum.items():
        target = target.replace(w, value)
        jamoWords = re.sub('[ㄱ-ㅎ]{2,}$', target, jamoWords)

        if len(target) < 3: break # 2자가 되었다면 break

      # print(f'{jamoWords} : 종성 자음 중복 처리하기')
    
    # 마지막
    joongsungNesting = re.finditer('[ㄱ-ㅎ]{2,}', jamoWords)
    for j in joongsungNesting:

      target = j.group(0)

      # 만약 끝 글자라면 X
      if j.end() == len(jamoWords): continue

      for w, value in weekJaum.items():
        target = target.replace(w, value)
        jamoWords = re.sub('[ㄱ-ㅎ]{2,}', target, jamoWords, count=1)
        if len(target) < 3: break # 3개 이하 중첩이면 break

      # print(f'{jamoWords} : 중성 자음 중복 처리하기')  

    lineResult += jamoWords + ' '

  print(f'{lineResult} : 기본')

  # ㅌ -> ㄹ flapping 음운변동
  flap = re.findall('[ㅏ-ㅣ]{1}ㅌ [ㅏ-ㅣ]', lineResult)
  for f in flap:
    print(f)
    setFlap = f.replace('ㅌ', 'ㄹ')
    lineResult = lineResult.replace(f, setFlap)

  # w는 뒤에오는 끝소리를 없앤다.
  lineResult = re.sub('[ㄱ-ㅎ][w]', 'ㅇ', lineResult)
  # print(f'{lineResult} : w는 뒤에오는 끝소리를 없앤다.')

  # t뒤에 y가 오면 ㅊ 발음이 난다.
  lineResult = lineResult.replace('ㅌ y', 'ㅊ')
  # print(f'{lineResult} : t뒤에 y가 오면 ㅊ 발음이 난다.')



  print(f'{lineResult} : 음운 변동 수정')

  # 잔챙이 발음 제거
  lineResult = re.sub('[a-z ]', '', lineResult)

  # 결합
  lineResult = join.join_jamos(lineResult)
  print(lineResult)

  # 단독 모음에 ㅇ 넣고 다시 결합
  soloMoum = re.findall('[ㅏ-ㅣ]', lineResult)
  for s in soloMoum:
    lineResult = lineResult.replace(s, "ㅇ" + s)
  lineResult = join.join_jamos(lineResult)

  # 남은 잔챙이 제거
  lineResult = re.sub('[ㄱ-ㅎ]', '', lineResult)
  print(lineResult, end='\n\n')

  

  

  # soloMoum = re.finditer('[ㅏ-ㅣ]', combine)

  # combine = list(combine) # n번째에 있는 문자열만 딱 집어서 바꾸기가 안되는듯 list화 시켜서 나중에 str으로 바꿀거임

  # for s in soloMoum:
  #   if s.start() != 0:
  #     combine[s.start()] = 'ㅇ' + s.group()

  # combine = ''.join(combine)

  # print(combine) # 2단계 : 첫 글자가 아닌 중간에 고립된 모음에 "ㅇ"을 추가해준다 

  # combine = join.join_jamos(combine)

  # print(combine) # 3단계 : 띄어쓰기를 없애고 다시한번 조합한다.

  # lineResult += combine

#   lyricsList[index] = lineResult

# lyricsList = '\n'.join(lyricsList)

# print(lyricsList)



""" 
3개 중첩 예시
congratulations ㅋㅡㄴㄱㅇㅐㅊㅓㄹㅔㅅㅡㄴㅈ // ㄴㄱㅇ 받침, 끝소리, 뒤에꺼
prompter ㅍㅇㅏㅁㅍㅌㅓㅇ                   // ㅁㅍㅌ 받침, 끝소리, 뒤에꺼
transfigure ㅌㅇㅐㄴㅅㅍㅣㄱㅓㅇ            // ㄴㅅㅍ 받침, 끝소리, 뒤에꺼
hamstring ㅎㅐㅁㅅㅌㅇㅣㅇ                  // ㅁㅅㅌㅇ 받침, 끝소리 뒤에꺼 뒤에
toothbrush ㅌㅜㄸㅂㅇㅓㅅ



끝소리 넘어가는 경우 : 뒤에 나올 단어가 모음으로 시작
끝소리 안넘어가는 경우 : 뒤에 나오

전부다 약한 발음 제거로 결론이 남 => 무지성으로 약한 발음 제거하기

congratulations ㅋㅡㄴㄱㅇㅐㅊㅓㄹㅔㅅㅡㄴㅈ
prompter ㅍㅇㅏㅁㅍㅌㅓㅇ
transfigure ㅌㅇㅐㄴㅅㅍㅣㄱㅓㅇ
hamstring ㅎㅐㅁㅅㅌㅇㅣㅇ
toothbrush ㅌㅜㄸㅂㅇㅓㅅ
expressive ㅣㅋㅅㅍㅇㅔㅅㅣㅂ
unplug ㅓㄴㅍㄹㅓ

첫 단어가 모음으로 시작한다면?

끝 단어 남기기? 끝단어만 살리기?
jinx ㅈㅣㅇㅋㅅ
first ㅍㅓㅇㅅㅌ
interrupt

모음이 두개인 경우가 있네..?
interrupt ㅣㄴㅓㅓㅍㅌ

일단 리스트로 빼올때 영어 문장으로 단위로 빼온다.


ㅣㄴㅓㅓㅍㅌ ㅏㅇㅌ

1단계 : 일단 조합 가능한 것만 붙인다
ㅣ너ㅓㅍㅌ ㅏㅇㅌ

2단계 : 첫 글자가 아닌 중간에 고립된 모음에 "ㅇ"을 추가해준다 
ㅣ너엎ㅌ ㅏㅇㅌ

3단계 : 띄어쓰기를 없애고 다시한번 조합한다. (첫째 단어 끝소리가 다음 단어와 조합이 가능할 수 있음)
ㅣ너엎탕ㅌ

4단계 : 홀로 있는 모음에 "ㅇ"을 추가해주고 다시 조합한다.
이너엎탕

 """

# # 첫 단어 음절은 강한 발음이 살아남음 (1개가 될 때 까지 약한 발음을 제거)
# chosungNestingCheck = re.match('^[ㄱ-ㅎ]{2,}[ㅏ-ㅣ]', jamoWords)
# print(chosungNestingCheck)

# # 가운데에 있는 음절들은 끝소리때문에 3~4개가 중첩될 수 있음 (2개가 될 때까지 약한 발음을 제거해야됨)
# middleNestingCheck = re.findall('[ㅏ-ㅣ][ㄱ-ㅎ]{3,}[ㅏ-ㅣ]', jamoWords)
# print(middleNestingCheck)

# # 끝 단어 음절은 끝소리를 살려야됨 (끝발음만 남기기)
# lastNestingCheck = re.search('[ㄱ-ㅎ]{2,}$', jamoWords)
# print(lastNestingCheck)

exit()

print(nestingCheck)

weekJaum = ['ㅇ', 'ㅎ', 'ㄴ', 'ㅁ', 'ㄹ', 'ㅅ', 'ㅈ', 'ㅊ']

for i in nestingCheck: 
   
  print(f'{i.start()}~{i.end()}번째에 있는 {i.group()}')

  separation = i.group()

  for w in weekJaum:
    separation = separation.replace(w, '')

  if len(separation) > 1: separation = separation[:-1]

  jamoWords = jamoWords.replace(i.group(), separation)

  ### 내일 할거 
  ### ! 근데 이거 종성은 끝음을 살려야할거같은데...? 끝소리가 넘어가야됨
  ### 초성부터 모음이 들어온다면 ㅇ을 넣어줘야함 !!
  ### 그리고 자음 모음을 합친 한글 결과물을 가사에 있는 영어와 교체 후 g2p 돌리면 완성

print(jamoWords)


# 

# for w in weekJaum: # 약한 발음의 자음을 하나씩 줄여나가기
#   jamoWords = jamoWords.replace(w, '')
#   if len(jamoWords) == 1: break

# # if len(jamoWords) > 1: jamoWords = jamoWords.replace(jamoWords[-1], '') # 강한 발음만 남았을 경우 마지막 발음 제거

# print(jamoWords)


# 중첩 자음 중에서 대표 발음 고르기


# for syl in engG2P:
#   for s in syl:
#     if 'ˈ' in s : s = s.replace('ˈ', '')
#     print(jaumTypeEn[s])

# [['k', 'ə', 'm'], ['p', 'j', 'ˈu'], ['ɾ', 'ɚ']] # computer

# re.sub('[˺ˈˌ#.]', '', text)

# 자음 찾기, 모음 찾기

# 1 : 제일 먼저 오는 것은 자음이다
# 2 : ipa 기호를 통해 찾아야할듯?



# 변수 1 : strange같은 자음이 중첩되는 단어
# ㄱㄷㅂㅈㅊㅋㅌㅍㄸ > ㄴㄹㅁㅎ > ㅅ ( sm sl sn 는 ㅅ가 약세인듯)

# 변수 2 : 구개음화 ex) did you [디쥬]

