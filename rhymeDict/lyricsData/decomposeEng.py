

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
    #"l̩" : "ㅡㄹ", 이거 왜 안먹힘?
    #"n̩" : "ㅡㄴ", 이거 왜 안먹힘?

    "bl" : "ㅂl",
    "dl" : "ㄷl",
    "fl" : "ㅍl",
    "gl" : "ㄱl",
    "kl" : "ㅋl",
    "sl" : "ㅅl",
    "pl" : "ㅍl",

    "sk" : "sㅋ",
    "sp" : "sㅍ",
    "st" : "sㅌ",

    "pt" : "pㅌ",

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
    
    "h" : "", # 제일 발음이 약한 ㅇ,ㅎ 라서 그냥 생략함
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

weekJaum = {'ㅇ' : 'r',
            'ㅎ' : 'h',
            'ㄴ' : 'n',
            'ㅁ' : 'm',
            'ㄹ' : 'l',
            'ㅅ' : 's',
            'ㅈ' : 'dg',
            'ㅊ' : 'ch'}

RWchange = {
   'ㅏ' : 'ㅘ', # right
   'ㅓ' : 'ㅝ', # water
   'ㅗ' : 'ㅝ', # world
   'ㅜ' : 'ㅝ', # woman
   'ㅡ' : 'ㅝ', # won같은거 wn̩으로 취급되네
   'ㅣ' : 'ㅟ', # win
   'ㅐ' : 'ㅞ', # 이게 있나..?
   'ㅔ' : 'ㅞ', # ready
}

Ychange = {
   'ㅏ' : 'ㅑ',
   'ㅓ' : 'ㅕ',
   'ㅗ' : 'ㅛ',
   'ㅜ' : 'ㅠ',
   'ㅐ' : 'ㅒ',
   'ㅔ' : 'ㅖ',
}

# ㅐ, ㅒ, ㅔ, ㅖ, ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ 

def ipa_to_korean(input_string):
    result = ""

    i = 0  # 문자열 인덱스

    # 이거 왜 dict에서 안먹힘?
    input_string = input_string.replace('l̩', 'ㅡㄹ')
    input_string = input_string.replace('n̩', 'ㅡㄴ')

    while i < len(input_string):
        
        # 두 글자로 된 IPA 문자열 처리
        if i < len(input_string) - 1 and input_string[i:i+2] in ipa2k:
            result += ipa2k[input_string[i:i+2]]
            i += 2  # 두 글자를 처리했으므로 인덱스를 2 증가시킴
        else:
            # 한 글자로 된 IPA 문자열 처리
            if input_string[i] in ipa2k:
                result += ipa2k[input_string[i]]
            else:
                result += input_string[i]
            i += 1  # 한 글자를 처리했으므로 인덱스를 1 증가시킴
    return result

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

a = isle.findClosestPronunciation('maybe')
print(a)
exit()
"""
사전 수정 내역 :
  a 단독으로 있는거 ei -> ə
  to 발음 tou -> tu 
  next 발음 t가 빠져있음 ㄷㄷ -> n ˈɛ k s t
  once -> w ˈʌ n s 
  don't won't didn't shouldn't.. 같은 것들 끝소리 t 묵음처리함
  committed attitude mountain
  oneself 왜 wn̩sɛlf로 되어있노

  what where when why 같은거 h발음으로 시작하는거 다 바꿈

  here, every, really # r들어간 단어에 음절이 하나 더 들어가있는 것 주의

"""

"""
자음 + t,d + 자음이면 flap임

built in ㅂㅣㄹ[ㅌ ㅣ]ㄴ (X)
found ways ㅍㅏㄴ[ㄷ ㅔ]ㅣ (X)

that all ㄷㅐㅌ ㅏㄹ (O)
get it ㄱㅔㅌ ㅣㄴ (O)

예외 : 't는 강세 없는듯? don't work 같은건 또 flap됨

r이 껴있는 타입 : get ready
w가 껴있는 타입 : get well

"""

"""
단어 내 flap 연구소

됨
  abilities lady negative
안됨
  attention attractive determination
  ready bloody

  ^[a-z]+dy[(]

  ^[a-z_-]+dy

  dy, ty로 끝나는거 사전 수정해보기?

  body -> 전부 바리로 수정

  ipa를 정규표현식으로 만드셈 

  모음 + d/t + 모음 다찾아보셈


"""



# 가사 예외 경고 : 가끔 백보컬을 괄호안에 넣어놓는 경우가 있음 () 


# - 예외 저장소 



# 영어는 schwa 발음이 좀 많아서 라임을 좀 관대하게 설정해도될듯?
# ə 발음은 확실히 ㅓ랑 ㅏ랑 ㅡ가 공존한다 ㅗㅜㅣ이런건 아님

# ㅅ ㅈ ㅊ가 같은 카테고리 같음 (초성 제외)


# roadmap

# failed I, found ways 강세가 뒤에도 있다면 flap안됨
# that won't work 강세가 뒤에 없으면 flap됨
# ð로 끝나면 flap?? with a, moth and

# about reaching

# ㅣ와 r이 만나면 ㅕ발음이 남 (다른건 X)


# hot wing


lyrics ='''
first interrupt

'''

lyrics = re.sub('[?!"():;“”1234567890]', '', lyrics)
lyrics = re.sub('[,.][ ]?', '\n', lyrics)
lyrics = re.sub('[-—]', ' ', lyrics)
lyrics = re.sub('[\n]{2,}', '\n', lyrics)
lyrics = re.sub('[ ]{2,}', ' ', lyrics)
lyrics = lyrics.replace('in\' ', 'ing ')
lyrics = lyrics.replace('é', 'e')
lyrics = lyrics.replace('’', '\'')

print(lyrics)

lyricsList = lyrics.strip().split('\n')

for index, oneLine in enumerate(lyricsList):

  lineResult = ''

  print(oneLine) # 원본

  oneLine = isle.transcribe(oneLine)
  oneLine = re.sub('[˺ˌ.ˈ#]', '', oneLine)

  print(oneLine) # ipa 변환

  lineResult = ' ' + ipa_to_korean(oneLine) + ' '

  print(lineResult) # ipa to 한글

  # w는 뒤에오는 끝소리를 없앤다. (st같은 2중 자음 넘어오는 건 제외) 
  # bad way, give way, ground way같은건 끝소리 넘어오는데? referential way?
  lineResult = re.sub('[ㅏ-ㅣ]ㅌ [wr]', lambda match: match.group().replace('ㅌ', 'ㅇ'), lineResult)

  # flapping
  while True:
    # 삼항연산자 ([ㅌㄷ])중에서 ㅌ일 경우 ㅌ->ㄹ or ㅌ가 아닐경우 ㄷ->ㄴ
    # 하나씩 처리하는 이유는 겹칠 수 있기때문에.. get it on 같이 두개 동시에 있으면 게리톤으로 나옴
    lineResult = re.sub('[ㅏ-ㅣ]([ㅌㄷ]) [wr]?[ㅏ-ㅣ]',
        lambda match: match.group(0).replace('ㅌ', 'ㄹ') if match.group(1) == 'ㅌ' else match.group(0).replace('ㄷ', 'ㄴ'), lineResult, count = 1)
    if re.match('[ㅏ-ㅣ]([ㅌㄷ]) [wr]?[ㅏ-ㅣ]', lineResult) == None : break

  # t뒤에 y가 오면 ㅊ 발음이 난다.
  lineResult = lineResult.replace('ㅌ y', 'ㅊ')

  # ㄷ뒤에 y가 오면 ㅈ 발음이 난다.
  lineResult = lineResult.replace('ㄷ y', 'ㅈ')

  # 더이상 겹치는 걸로 변동은 없으니 띄어쓰기 없애기 (뒤에 올 기능을 위해)
  lineResult = lineResult.replace(' ', '')

  # y, w, r 발음 변동
  # ([ywr])중에 y라면 Ychange 사전에서 y변환 발음 갖고오기, ([ywr])중에 y가 아니라면 rw사전에서 rw변환발음 갖고오기...를 람다함수에 삼항연산자로 처리함
  lineResult = re.sub('([ywr])([ㅏ-ㅣ])', lambda match: Ychange[match.group(2)] if match.group(1) == 'y' else RWchange[match.group(2)], lineResult)

  # 잔챙이 발음 제거 후 결합
  lineResult = re.sub('[a-z]', '', lineResult)
  lineResult = join.join_jamos(lineResult)

  # 단독으로 있는 모음에 ㅇ 붙이고 결합 (잔챙이 발음 제거 후에 해야됨)
  lineResult = re.sub('[ㅏ-ㅣ]', lambda match: 'ㅇ' + match.group(), lineResult)
  lineResult = join.join_jamos(lineResult)
  
  # 마지막 잔챙이 제거
  lineResult = re.sub('[ㄱ-ㅎ]', '', lineResult)
  print(lineResult, end='\n\n')








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

