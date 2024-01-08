from g2p_en import G2p
import join
import re
import hgtk
# import quote_list as ql


# texts = ["I have $250 in my pocket." : '',
# # number -> spell-out
#          "popular pets : '',
# e.g. cats and dogs" : '',
# # e.g. -> for example
#          "I refuse to collect the refuse around here." : '',
# # homograph
#          "I'm an activationist."] # newly coined word

# 실제 발음을 추출하기보단 연음을 제거해서 대표발음만 추출하는거임
# black도 블랙으로 나오지않고 한 음절 단어인 뱈 으로 나올거임

symbols = {
'AA' : 'ㅏ',
'AA0' : 'ㅏ',
'AA1' : 'ㅏ', # frog block clock start
'AA2' : 'ㅏ',
'AE' : 'ㅐ',
'AE0' : 'ㅐ',
'AE1' : 'ㅐ', # crab flag
'AE2' : 'ㅐ',
'AH' : 'ㅏ',
'AH0' : 'ㅐ',
'AH1' : 'ㅓ', # club fuck suck u발음인듯
'AH2' : 'ㅐ',
'AO' : 'ㅗ',
'AO0' : 'ㅗ',
'AO1' : 'ㅗ',
'AO2' : 'ㅗ',
'AW' : 'ㅏ',
'AW0' : 'ㅏ',
'AW1' : 'ㅏ',
'AW2' : 'ㅏ',
'AY' : 'ㅏ',
'AY0' : 'ㅏ',
'AY1' : 'ㅏ',
'AY2' : 'ㅏ',
'B' : 'ㅂ',
'CH' : 'ㅊ',
'D' : 'ㄷ',
'DH' : 'ㄷ',
'EH' : 'ㅔ',
'EH0' : 'ㅔ',
'EH1' : 'ㅔ', # dress 
'EH2' : 'ㅔ',
'ER' : 'ㅓ',
'ER0' : 'ㅓ',
'ER1' : 'ㅓ',
'ER2' : 'ㅓ',
'EY' : 'ㅔ',
'EY0' : 'ㅔ',
'EY1' : 'ㅔ', # grape train snake spray 
'EY2' : 'ㅔ',
'F' : 'ㅍ',
'G' : 'ㄱ',
'HH' : 'ㅎ',
'IH' : 'ㅣ',
'IH0' : 'ㅣ',
'IH1' : 'ㅣ',
'IH2' : 'ㅣ',
'IY' : 'ㅣ',
'IY0' : 'ㅣ',
'IY1' : 'ㅣ', # sleep ski screen stream
'IY2' : 'ㅣ',
'JH' : 'ㅈ',
'K' : 'ㅋ',
'L' : 'ㄹ', # L은 연음때문에 애매함..  
'M' : 'ㅁ',
'N' : 'ㄴ',
'NG' : 'ㅇ',
'OW' : 'ㅗ',
'OW0' : 'ㅗ',
'OW1' : 'ㅗ',
'OW2' : 'ㅗ',
'OY' : 'ㅣ',
'OY0' : 'ㅣ',
'OY1' : 'ㅣ',
'OY2' : 'ㅣ',
'P' : 'ㅍ',
'R' : 'ㄹ', # R은 연음때문에 애매함..  L과 R은 다행히 ㄹ계열이라서 ㅇ으로 대체 가능 Absolutely
'S' : 'ㅅ',
'SH' : 'ㅅ',
'T' : 'ㅌ',
'TH' : 'ㄸ',
'UH' : 'ㅓ',
'UH0' : 'ㅓ',
'UH1' : 'ㅓ',
'UH2' : 'ㅓ',
'UW' : 'ㅜ',
'UW0' : 'ㅜ',
'UW1' : 'ㅜ',
'UW2' : 'ㅜ',
'V' : 'ㅂ',
'W' : 'ㅇ',
'Y' : '',
'Z' : 'ㅈ',
'ZH' : 'ㅈ',
' ' : ' ', # 끝소리 넘어가는 건 join 과정에서 공백때문에 방해됨
}

moum = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
jaum = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

result = ''

texts = ['express projects brush crab dress frog grape train block clock flag glove plug sleep ski snake start screen spray stream it\'s this']
# texts = ['No news is good news The pen is mightier than the sword Necessity is the mother of invention Good things come to those who wait Can not see the wood for the trees If you run after two hares you will catch neither Rome was not built in a day There\'s no place like home Two heads are better than one You can not judge a book by its cover It\'s no use crying over spilled milk Tomorrow is another day']
# texts = ['city pretty party water invention team button']
# texts = ['The second highest of the four castes or varnas in traditional Hindu society the warrior or military caste']
texts = ['computer']

# sen = ql.sentences



sen = texts

g2p = G2p()

for s in sen:

    # text = re.sub('[.,]', '\n', text)
    # texts = text.splitlines()

    eng = ''
    result = ''

    s = [s]

    for text in s:
        out = g2p(text)
        print(out)

    for ou in out:
        eng += ou

    # print(eng)

    for o in out:
        result += symbols[o]

    # print('정제 x : ' + result)
    rl = re.compile('.ㄹ').findall(result)
    if rl != []:
        result = re.compile('.ㄹ').sub('뷁', result)
        for b in rl:
            result = result.replace('뷁', b[0], 1)
        
    # print(result)

    result = join.join_jamos(result)

    # print(result)

    # com = re.compile('([ㄱ-ㅎ])([ㄱ-ㅎ])')
    # finds = re.finditer(com, result)

    # mod_words = []

    # for f in finds: # 
    #     mod_words.append(str(f.group(1))) # 그룹1 을 리스트화 시키고

    # word = re.sub(com, '뷁', result) # 뷁으로 일단 교체 (뷁은 뷁이지만 위치정보까지 포함되어 있는거임)

    # for i in range(0, len(mod_words)):
    #     word = word.replace('뷁', mod_words[i], 1) # 뷁을 다시 그룹1로 바꾸기

    # 끝소리 이동 : 자음 단독으로 나왔을 때 뒷소리가 ㅎ 이면 넘어가기 (ㅇ이면 자동으로 걍 넘어감)
    # 자음 두개가 동시에 나올 경우 뒤에 나오는 자음은 뺌 (앞에 나오는 자음이 대표발음임)




    for k in moum: # 이응 발음 생략된거 수정
        result = result.replace(k, 'ㅇ'+k)

    result = join.join_jamos(result)

    print(result)


    # print(texts)
    # print(result)

    # result = re.sub('[ㄱ-ㅎ]+ ', ' ', result) # 끝에 자음하나 덜렁있으면 지우기

    # if re.compile('[ㄱ-ㅎ]').match(result[-1]) != None: # 마지막은 공백이 없어서 위 코드가 안먹힘
    #     # print(re.compile('[ㄱ-ㅎ]').match(result[-1]))
    #     result = result[:-1]

    # result = re.sub(' ㅅ', ' ', result) # 초성이 ㅅ이라면 제거

    # if result[0] == 'ㅅ': # 처음엔 공백이 없어서 위 코드가 안먹힘
    #     result = result[1:]

    result = re.sub(' ', '', result)

    com = re.compile('[ㄱ-ㅎ]').search(result)
    print(com)
    
    # if re.compile('[ㄱ-ㅎ]').findall(result) != []:
    #     print('texts : ' + str(s))
    #     print(result)

    print('texts : ' + str(s))
    print(eng)
    print(result)
    print("")
    
    # ㅅ발음은 대표발음은 아닐테니 지우기 (sl은 뺄까?)

    # 우리나라는 모음이 많은데

    # 영어는 A E I O U 밖에 없으니까 모음기준 라임을 좀 유하게 할 필요성이 있지 않을까?
    """projects and
    프, 롸, 젝, 트, 스
    ㅍㄹㅏㅈㅔㅋㅌㅅㅐㄴ

    expression
    ㅇㅣㅋㅅㅍㄹㅔㅅㅐㄴ
    이것처럼 3~4개도 있을 수 있음

    단순히 자음 하나 단독으로 덜렁 있다고 바꾸는 건 위험함
    끝에 자음하나 덜렁있으면 지우기

    s 발음은 대표 발음이 아닐 수 있다

    black => ㅂ랰 => 뱈 일텐데
    skin => ㅅ킨 => 신 은 아님
    ㅅ이 단독으로 있을 경우에는 ㅅ을 빼버리기?

    ㅇ ㅎ 연음 적용?
    beautiful 뷰우태퍁
    use 유웃


    bless 는 b가 강한가?

    t 발음 ㄹ 로 되는 과정


    slice sl은 ㅅ 발음 ㄹ 발음 둘다 대표발음이 되는 따블현상이 벌어짐

    br cr dr fr gr tr bl cl fl gl pl sl sk sn st scr spr str
    ㅂ ㅋ ㄷ ㅍ ㄱ  ㅊ ㅂ ㅋ ㅍ ㄱ ㅍ 
    강세 = {
        'B' : '1',
        'C' : '1',
        'D' : '1',
        'F' : '1',
        'G' : '1',
        'H' : '1',
        'I' : '1',
        'J' : '1',
        'K' : '1',
        'L' : '1',
        'M' : '1',
        'M' : '1',
        'M' : '1',
        'M' : '1',
        'M' : '1',
    }


    """

