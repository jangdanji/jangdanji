from pysle import isletool
isle = isletool.Isle()
print(isle.lookup('little')[0].toList()[0]) # Get the first entry's pronunciation
# >> [[['k', 'ˌæ'], ['ɾ', 'ə'], ['t', 'ˈɑ'], ['n', 'ɪ', 'k']]]

char = { # ㄱㄷㅂㅈㅊㅋㅌㅍㄸ > ㄴㄹㅁㅎ > ㅅ ( sm sl sn 는 ㅅ가 약세인듯)
    "ɵ" : "ㄸ", # ㄸ
    "t" : "ㅌ", # ㅌ
    "tʃ" : "ㅊ", # ㅊ
    "ʒ" : "ㅈ", # ㅈ
    "b" : "ㅂ", # ㅂ
    "dʒ" : "ㅈ", # ㅈ
    "d" : "ㄷ", # ㄷ
    "f" : "ㅍ", # ㅍ
    "g" : "ㄱ", # ㄱ
    "v" : "ㅂ", # ㅂ
    "z" : "ㅈ", # ㅈ
    "ð" : "ㄷ", # ㄷ
    "k" : "ㅋ", # ㅋ
    "p" : "ㅍ", # ㅍ

    "h" : "ㅎ",
    "l" : "ㄹ", # ㄹ은 그냥 유음이라서 없는걸로 치고 나중에 초성칸이 비었으면 ㅇ으로 대체하도록 ㄱㄱ
    "m" : "ㅁ",
    "n" : "ㄴ",
    "r" : "ㄹ", # ㄹ유음 생략 이하동문

    "s" : "ㅅ",  
    "j" : "", # y
    "ʃ" : "ㅅ", # sh
    "w" : "ㅇ", # 생략
    "ɾ" : "ㅇ", # r

    "ɹ" : "r", 

    "ŋ" : "ㅇ",
    "æ" : "ㅔ",
    "u" : "ㅜ",
    "oʊ" : "ㅗ", 
    "i" : "ㅣ",
    "ei" : "ㅔ",
    "aʊ" : "ㅏ",
    "ɑ" : "ㅏ",
    "ɑɪ" : "ㅏ",
    "ɔ" : "ㅏ",
    "ɔi" : "ㅏ",
    "ə" : "ㅓ",
    "ɚ" : "ㅓ", # ~r
    "ɛ" : "ㅔ", # ~r
    "ɝ" : "ㅓ", # ~r
    "ɪ" : "ㅣ",
    "ʊ" : "ㅜ",
    "æ" : "ㅐ",
    "ʌ" : "ㅓ",
    "ae" : "ㅐ",
    "l̩" : "ㅡㄹ",
    "n̩" : "ㅡㄴ",
    "ɝ" : "ㅓ",
    "a" : "ㅏ",
    "e" : "ㅔ",
    "o" : "ㅗ",
    " " : " ",

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
}

texts = ['express projects brush crab dress frog grape train block clock flag glove plug sleep ski snake start screen spray stream it\'s this']
# texts = ['No news is good news The pen is mightier than the sword Necessity is the mother of invention Good things come to those who wait Can not see the wood for the trees If you run after two hares you will catch neither Rome was not built in a day There\'s no place like home Two heads are better than one You can not judge a book by its cover It\'s no use crying over spilled milk Tomorrow is another day']
# texts = ['city pretty party water invention team button']
# texts = ['The second highest of the four castes or varnas in traditional Hindu society the warrior or military caste']
texts = ['computer']

import re


lyrics = 'string interrupt'

# ain't Mr Ms
# night's one's woman's dante's 
# overrest toodles cretonnes gewgaws eyesores tarvia days’ smuts sewickley hells

# settlement of fifteen ???


lyrics = re.sub('[?!.,"():;“”1234567890]', '', lyrics)
lyrics = re.sub('[-—\n]', ' ', lyrics)
lyrics = re.sub('[ ]{2,}', ' ', lyrics)
lyrics = lyrics.replace('in\' ', 'ing ')
lyrics = lyrics.replace('é', 'e')
lyrics = lyrics.replace('’', '\'')


oneLine = isle.transcribe(lyrics, "shortest")
print(oneLine)

RWchange = {
   'ㅏ' : 'ㅘ', # right
   'ㅓ' : 'ㅝ', # water
   'ㅗ' : 'ㅝ', # world
   'ㅜ' : 'ㅘ', # woman
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
   'ㅔ' : 'ㅒ',
}

a = re.sub('([ywr])([ㅏ-ㅣ])', lambda match: match.group(0))

# nestedWords = []

# nested = re.finditer(' [gdðbvktfpɵzʒʃslɾmn̩n]{2,}', oneLine)
# for n in nested:
#   print(oneLine[n.start():n.start()+20])
#   nestedWords.append(n.group(0))

# nestedWords = set(nestedWords)

# print(nestedWords)

# index = 10289

# print(oneLine[index:index+10])