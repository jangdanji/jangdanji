# -*- coding: utf-8 -*-

# pip install hgtk


'''
g2p.py
~~~~~~~~~~

This script converts Korean graphemes to romanized phones and then to pronunciation.

    (1) graph2phone: convert Korean graphemes to romanized phones
    (2) phone2prono: convert romanized phones to pronunciation
    (3) graph2phone: convert Korean graphemes to pronunciation

Usage:  $ python g2p.py '스물 여덟째 사람'
        (NB. Please check 'rulebook_path' before usage.)

Yejin Cho (ycho@utexas.edu)
Jaegu Kang (jaekoo.jk@gmail.com)
Hyungwon Yang (hyung8758@gmail.com)
Yeonjung Hong (yvonne.yj.hong@gmail.com)

Created: 2016-08-11
Last updated: 2019-01-31 Yejin Cho

* Key updates made:
    - Executable in both Python 2 and 3.
    - G2P Performance test available ($ python g2p.py test)
    - G2P verbosity control available

'''

import datetime as dt
import re
import math
import sys
import optparse
from unittest import result
from mappings import dic, jaum, jaumtype, moumtype, moumtype_rev
from dataLoader import lyricDataLoader




# Option
parser = optparse.OptionParser()
parser.add_option("-v", action="store_true", dest="verbose", default="False",
                  help="This option prints the detail information of g2p process.")

(options,args) = parser.parse_args()
verbose = options.verbose

# Check Python version
ver_info = sys.version_info

if ver_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')


def readfileUTF8(fname):
    f = open(fname, 'r')
    corpus = []

    while True:
        line = f.readline()
        line = line.encode("utf-8")
        line = re.sub(u'\n', u'', line)
        if line != u'':
            corpus.append(line)
        if not line: break

    f.close()
    return corpus


def writefile(body, fname):
    out = open(fname, 'w')
    for line in body:
        out.write('{}\n'.format(line))
    out.close()


def readRules(pver, rule_book):
    if pver == 2:
        f = open(rule_book, 'r')
    elif pver == 3:
         f = open(rule_book, 'r',encoding="utf-8")
         
    rule_in = []
    rule_out = []

    while True:
        line = f.readline()
        if pver == 2:
            line = unicode(line.encode("utf-8"))
            line = re.sub(u'\n', u'', line)
        elif pver == 3:
            line = re.sub('\n', '', line)

        if line != u'':
            if line[0] != u'#':
                IOlist = line.split('\t')
                rule_in.append(IOlist[0])
                if IOlist[1]:
                    rule_out.append(IOlist[1])
                else:   # If output is empty (i.e. deletion rule)
                    rule_out.append(u'')
        if not line: break
    f.close()

    return rule_in, rule_out


def isHangul(charint):
    hangul_init = 44032
    hangul_fin = 55203
    return charint >= hangul_init and charint <= hangul_fin


def checkCharType(var_list):
    #  1: whitespace
    #  0: hangul
    # -1: non-hangul
    checked = []
    for i in range(len(var_list)):
        if var_list[i] == 32:   # whitespace
            checked.append(1)
        elif isHangul(var_list[i]): # Hangul character
            checked.append(0)
        else:   # Non-hangul character
            checked.append(-1)
    return checked


def graph2phone(graphs):
    # Encode graphemes as utf8
    try:
        graphs = graphs.decode('utf8')
    except AttributeError:
        pass

    integers = []
    for i in range(len(graphs)):
        integers.append(ord(graphs[i]))

    # Romanization (according to Korean Spontaneous Speech corpus; 성인자유발화코퍼스)
    phones = ''
    ONS = ['k0', 'kk', 'nn', 't0', 'tt', 'rr', 'mm', 'p0', 'pp',
           's0', 'ss', 'oh', 'c0', 'cc', 'ch', 'kh', 'th', 'ph', 'h0']
    NUC = ['aa', 'qq', 'ya', 'yq', 'vv', 'ee', 'yv', 'ye', 'oo', 'wa',
           'wq', 'wo', 'yo', 'uu', 'wv', 'we', 'wi', 'yu', 'xx', 'xi', 'ii']
    COD = ['', 'kf', 'kk', 'ks', 'nf', 'nc', 'nh', 'tf',
           'll', 'lk', 'lm', 'lb', 'ls', 'lt', 'lp', 'lh',
           'mf', 'pf', 'ps', 's0', 'ss', 'oh', 'c0', 'ch',
           'kh', 'th', 'ph', 'h0']

    # Pronunciation
    idx = checkCharType(integers)
    iElement = 0
    while iElement < len(integers):
        if idx[iElement] == 0:  # not space characters
            base = 44032
            df = int(integers[iElement]) - base
            iONS = int(math.floor(df / 588)) + 1
            iNUC = int(math.floor((df % 588) / 28)) + 1
            iCOD = int((df % 588) % 28) + 1

            s1 = '-' + ONS[iONS - 1]  # onset
            s2 = NUC[iNUC - 1]  # nucleus

            if COD[iCOD - 1]:  # coda
                s3 = COD[iCOD - 1]
            else:
                s3 = ''
            tmp = s1 + s2 + s3
            phones = phones + tmp

        elif idx[iElement] == 1:  # space character
            tmp = '#'
            phones = phones + tmp

        phones = re.sub('-(oh)', '-', phones)
        iElement += 1
        tmp = ''

    # 초성 이응 삭제
    phones = re.sub('^oh', '', phones)
    phones = re.sub('-(oh)', '', phones)

    # 받침 이응 'ng'으로 처리 (Velar nasal in coda position)
    phones = re.sub('oh-', 'ng-', phones)
    phones = re.sub('oh([# ]|$)', 'ng', phones)

    # Remove all characters except Hangul and syllable delimiter (hyphen; '-')
    phones = re.sub('(\W+)\-', '\\1', phones)
    phones = re.sub('\W+$', '', phones)
    phones = re.sub('^\-', '', phones)
    return phones


def phone2prono(phones, rule_in, rule_out):
    # Apply g2p rules
    for pattern, replacement in zip(rule_in, rule_out):
        # print pattern
        phones = re.sub(pattern, replacement, phones)
        prono = phones
    return prono


def addPhoneBoundary(phones):
    # Add a comma (,) after every second alphabets to mark phone boundaries
    ipos = 0
    newphones = ''
    while ipos + 2 <= len(phones):
        if phones[ipos] == u'-':
            newphones = newphones + phones[ipos]
            ipos += 1
        elif phones[ipos] == u' ':
            ipos += 1
        elif phones[ipos] == u'#':
            newphones = newphones + phones[ipos]
            ipos += 1

        newphones = newphones + phones[ipos] + phones[ipos+1] + u','
        ipos += 2

    return newphones


def addSpace(phones):
    ipos = 0
    newphones = ''
    while ipos < len(phones):
        if ipos == 0:
            newphones = newphones + phones[ipos] + phones[ipos + 1]
        else:
            newphones = newphones + ' ' + phones[ipos] + phones[ipos + 1]
        ipos += 2

    return newphones


def graph2prono(graphs, rule_in, rule_out):

    romanized = graph2phone(graphs)
    romanized_bd = addPhoneBoundary(romanized)
    prono = phone2prono(romanized_bd, rule_in, rule_out)

    prono = re.sub(u',', u' ', prono)
    prono = re.sub(u' $', u'', prono)
    prono = re.sub(u'#', u'-', prono)
    prono = re.sub(u'-+', u'-', prono)

    prono_prev = prono
    identical = False
    loop_cnt = 1

    if verbose == True:
        print ('=> Romanized: ' + romanized)
        print ('=> Romanized with boundaries: ' + romanized_bd)
        print ('=> Initial output: ' + prono)

    while not identical:
        prono_new = phone2prono(re.sub(u' ', u',', prono_prev + u','), rule_in, rule_out)
        prono_new = re.sub(u',', u' ', prono_new)
        prono_new = re.sub(u' $', u'', prono_new)

        if re.sub(u'-', u'', prono_prev) == re.sub(u'-', u'', prono_new):
            identical = True
            prono_new = re.sub(u'-', u'', prono_new)
            if verbose == True:
                print('\n=> Exhaustive rule application completed!')
                print('=> Total loop count: ' + str(loop_cnt))
                print('=> Output: ' + prono_new)
        else:
            if verbose == True:
                print('\n=> Rule applied for more than once')
                print('cmp1: ' + re.sub(u'-', u'', prono_prev))
                print('cmp2: ' + re.sub(u'-', u'', prono_new))
            loop_cnt += 1
            prono_prev = prono_new

    return prono_new


def testG2P(rulebook, testset):
    [testin, testout] = readRules(ver_info[0], testset)
    cnt = 0
    body = []
    for idx in range(0, len(testin)):
        print('Test item #: ' + str(idx+1) + '/' + str(len(testin)))
        item_in = testin[idx]
        item_out = testout[idx]
        ans = graph2phone(item_out)
        ans = re.sub(u'-', u'', ans)
        ans = addSpace(ans)

        [rule_in, rule_out] = readRules(ver_info[0], rulebook)
        pred = graph2prono(item_in, rule_in, rule_out)

        if pred != ans:
            print('G2P ERROR:  [result] ' + pred + '\t\t\t[ans] ' + item_in + ' [' + item_out + '] ' + ans)
            cnt += 1
        else:
            body.append('[result] ' + pred + '\t\t\t[ans] ' + item_in + ' [' + item_out + '] ' + ans)

    print('Total error item #: ' + str(cnt))
    writefile(body,'good.txt')


def runKoG2P(graph, rulebook):
    [rule_in, rule_out] = readRules(ver_info[0], rulebook)
    if ver_info[0] == 2:
        prono = graph2prono(unicode(graph), rule_in, rule_out)
    elif ver_info[0] == 3:
        prono = graph2prono(graph, rule_in, rule_out)

    return prono


def runTest(rulebook, testset):
    print('[ G2P Performance Test ]')
    beg = dt.datetime.now()
    
    testG2P(rulebook, testset)
    
    end = dt.datetime.now()
    print('Total time: ')
    print(end - beg)

def wordToPron(oneWord):

    pron = runKoG2P(oneWord, 'data\\rulebook.txt') # 발음
    pron = pron.split(sep=' ')

    word = ''
    
    for j in pron:
        word += dic[j][0]

    word = join.join_jamos(word)

    for k in jaum: # 이응 발음 생략된거 수정
        word = word.replace(k, 'ㅇ'+k)

    word = join.join_jamos(word)

    print(f'=> : {word}', end='\n\n') # 최종 발음

    return word

import join
import re
import hgtk
import pprint

titles = lyricDataLoader()

def g2pRHYME(word , filterWord=''):

    userWords = word.split()

    result = []

    # filterWord = '말도 라도 라고 냐고 말고 나도 나고 랐고 않고 마도'

    for oneWord in userWords:

        word = wordToPron(oneWord)

        chos = []
        jungs = []
        jongs = []

        for l in range(0, len(word)):
            a = hgtk.letter.decompose(word[l])
            chos.append(a[0])
            jungs.append(a[1])
            jongs.append(a[2])

        
        print(f'초성 : {chos}\n중성 : {jungs}\n종성 : {jongs}', end='\n\n')

        userMoum = {}

        # item = moumtype.get('mo1')

        print('모음 타입 : ' + str(jungs), end='\n\n') # 예시 : <트레이서> 의 각각 모음 타입 [ㅡ, ㅔ, ㅣ, ㅓ]

        for ju in enumerate(jungs):
            userMoum[ju[0]] = moumtype_rev[moumtype[ju[1]]]

        print('허용 모음 : ')
        pprint.pprint(userMoum)

        for i in titles: # 나무위키 특수문자, 영어 처리

            # 아직 단어 발음 처리 안함
    
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
            i = hangul.sub('', i) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
            i = i.replace(' ', '')

            if len(i) < len(chos): # 글자 수 초과되는 단어 제외
                continue

            compareMoum = []

            # 문자(i)의 모음을 compareMoum에 추가함
            for leng in range(len(i), 0, -1): 
                compareMoum.append(hgtk.letter.decompose(i[-leng])[1])

            # print(f'자음 추출 : {compareMoum}')

            # # 마지막 두 글자만 자음까지 분석할거임
            # word1 = hgtk.letter.decompose(i[-2])
            # word2 = hgtk.letter.decompose(i[-1])

            
            def check_rhyme_ultimate(userWords, compareWords, length=None): # 발음 그대로 넣어야됨

                # 단어 라임 자음까지 일치, 분석할 끝 글자 갯수 length로 제어가능

                wordLength = len(userWords)

                wordLength if length == None else wordLength # length 안넣었으면 글자 길이만큼

                if length == None: pass
                else : wordLength = length

                for uw, cw in zip(userWords, compareWords[-wordLength::]):

                    userWordDecompose = hgtk.letter.decompose(uw)
                    compareWordDecompose = hgtk.letter.decompose(cw)

                    # print(f'{userWordDecompose} / {compareWordDecompose}')
                    
                    check_jaum = jaumtype[userWordDecompose[0]] == jaumtype[compareWordDecompose[0]]
                    check_moum = moumtype[userWordDecompose[1]] == moumtype[compareWordDecompose[1]]

                    # print(f'check_jaum : {check_jaum}, check_moum : {check_moum}')
                    # print(f'{check_jaum} : {userWordDecompose[0]} / {compareWordDecompose[0]}')
                    # print(f'{check_moum} : {userWordDecompose[1]} / {compareWordDecompose[1]}')

                    if check_jaum == False or check_moum == False:
                        return False
                    
                return True
            
            def check_rhyme(userMoum, compareMoum, length):

                # 모든 단어 모음 일치 (length로 끝 글자 제어 가능)

                compareMoum = compareMoum[-length:] # 마지막 x글자만 뽑기

                for index, (key, value) in enumerate(userMoum.items()):

                    if (compareMoum[index] in value) == False:
                        return False
                    
                return True
            
                        
            # 끝 글자 두개만 받침빼고 초중성 일치 (100%)
            # rhyme_1 = chos[-2] == word1[0] and jungs[-2] == word1[1] and chos[-1] == word2[0] and jungs[-1] == word2[1]

            # 끝 글자 두개만 고급 라임 일치 (70%)
            # rhyme_2 = jaumtype[chos[-2]] == jaumtype[word1[0]] and moumtype[jungs[-2]] == moumtype[word1[1]] and \
            #             jaumtype[chos[-1]] == jaumtype[word2[0]] and moumtype[jungs[-1]] == moumtype[word2[1]]

            # # 끝 글자 두개만 고급 라임 일치 (80&)
            # rhyme_2 = check_rhyme_ultimate(word, i, 2)
            
            # # 전부 모음 라임 일치 (50%)
            # rhyme_3 = check_rhyme(userMoum, compareMoum, len(word))

            # 전부 고급 라임 일치 (95%)
            rhyme_4 = check_rhyme_ultimate(word, i)
            
            if rhyme_4 :
                print(f'{i} : {rhyme_4}')
                result.append(i)
    
    return result

a = g2pRHYME('병신') # 발음 나는 그대로 사용을 권장 : 식혜(X) 시켸(O)

print(a)




# 1티어 : 맨 끝 초성은 동일하고 나머지 초성은 유사발음, 모음 유사발음,
# 2티어 : 전부 유사발음

# 말장난ver 1티어 : 끝 두 글자가 똑같음 ex) 솜브라 뽕브라 지브라
# 말장난ver 2티어 : 끝 글자가 똑같음 ex) 렛잇고 알파고

# 여기서 한국인 사용 빈도수 높은 수로 정렬시키기?





# ja1 = ['ㄱ', 'ㄷ', 'ㅂ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㄲ', 'ㄸ', 'ㅃ']
# ja2 = ['ㅅ', 'ㅈ', 'ㅊ', 'ㅆ', 'ㅉ']
# ja3 = ['ㄴ', 'ㄹ', 'ㅁ']
# ja4 = ['ㅇ', 'ㅎ']
# mo1 = ['ㅏ', 'ㅑ', 'ㅘ']
# mo2 = ['ㅓ', 'ㅕ', 'ㅝ', 'ㅗ', 'ㅛ']
# mo3 = ['ㅜ', 'ㅠ', 'ㅡ']
# mo4 = ['ㅣ', 'ㅟ', 'ㅢ']
# mo5 = ['ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅙ', 'ㅚ', 'ㅞ']


