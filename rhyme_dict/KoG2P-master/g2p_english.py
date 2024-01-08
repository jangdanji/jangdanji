# -*- coding: utf-8 -*-
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

import en_kr




dic = {
    'p0' : 'ㅂ', 'ph' : 'ㅍ', 'pp' : 'ㅃ', 't0' : 'ㄷ', 'th' : 'ㅌ', 'tt' : 'ㄸ', 'k0' : 'ㄱ',
    'kh' : 'ㅋ', 'kk' : 'ㄲ', 's0' : 'ㅅ', 'ss' : 'ㅆ', 'h0' : 'ㅎ', 'c0' : 'ㅈ', 'ch' : 'ㅊ',
    'cc' : 'ㅉ', 'mm' : 'ㅁ', 'nn' : 'ㄴ', 'rr' : 'ㄹ', 'pf' : 'ㅂ', 'ph' : 'ㅍ', 'tf' : 'ㄷ',
    'th' : 'ㅌ', 'kf' : 'ㄱ', 'kh' : 'ㅋ', 'kk' : 'ㄲ', 's0' : 'ㅅ', 'ss' : 'ㅆ', 'h0' : 'ㅎ',
    'c0' : 'ㅈ', 'ch' : 'ㅊ', 'mf' : 'ㅁ', 'nf' : 'ㄴ', 'ng' : 'ㅇ', 'll' : 'ㄹ', 'ks' : 'ㄳ',
    'nc' : 'ㄵ', 'nh' : 'ㄶ', 'lk' : 'ㄺ', 'lm' : 'ㄻ', 'lb' : 'ㄼ', 'ls' : 'ㄽ', 'lt' : 'ㄾ',
    'lp' : 'ㄿ', 'lh' : 'ㅀ', 'ps' : 'ㅄ', 'ii' : 'ㅣ', 'ee' : 'ㅔ', 'qq' : 'ㅐ', 'aa' : 'ㅏ',
    'xx' : 'ㅡ', 'vv' : 'ㅓ', 'uu' : 'ㅜ', 'oo' : 'ㅗ', 'ye' : 'ㅖ', 'yq' : 'ㅒ', 'ya' : 'ㅑ',
    'yv' : 'ㅕ', 'yu' : 'ㅠ', 'yo' : 'ㅛ', 'wi' : 'ㅟ', 'wo' : 'ㅚ', 'wq' : 'ㅙ', 'we' : 'ㅞ',
    'wa' : 'ㅘ', 'wv' : 'ㅝ', 'xi' : 'ㅢ'
}

jaumtype = {
    'ㄱ' : 'ja1', 'ㄷ' : 'ja1', 'ㅂ' : 'ja1', 'ㅋ' : 'ja1',
    'ㅍ' : 'ja1', 'ㄲ' : 'ja1', 'ㄸ' : 'ja1', 'ㅃ' : 'ja1',
    'ㅅ' : 'ja2', 'ㅈ' : 'ja2', 'ㅊ' : 'ja2', 'ㅆ' : 'ja2', 'ㅉ' : 'ja2',  'ㅌ' : 'ja2', # 영어 한정 허용 ㅌ
    'ㄴ' : 'ja3', 'ㄹ' : 'ja3', 'ㅁ' : 'ja3',
    'ㅇ' : 'ja4', 'ㅎ' : 'ja4'
}

moumtype = {
    'ㅏ' : 'mo1', 'ㅑ' : 'mo1', 'ㅘ' : 'mo1',
    'ㅓ' : 'mo2', 'ㅕ' : 'mo2', 'ㅝ' : 'mo2',
    'ㅗ' : 'mo1', 'ㅛ' : 'mo1', 'ㅗ' : 'mo2', 'ㅛ' : 'mo2', # 영어 한정 허용 ㅗ ㅛ
    'ㅜ' : 'mo3', 'ㅠ' : 'mo3', 'ㅡ' : 'mo3',
    'ㅣ' : 'mo4', 'ㅟ' : 'mo4', 'ㅢ' : 'mo4',
    'ㅐ' : 'mo5', 'ㅒ' : 'mo5', 'ㅔ' : 'mo5', 'ㅖ' : 'mo5', 'ㅙ' : 'mo5', 'ㅚ' : 'mo5', 'ㅞ' : 'mo5'
}

moumtype_rev = {
    'mo1' : ['ㅏ', 'ㅑ', 'ㅘ'],
    'mo2' : ['ㅓ', 'ㅕ', 'ㅝ'],
    'mo2.5' : ['ㅗ', 'ㅛ'],
    'mo3' : ['ㅜ', 'ㅠ', 'ㅡ'],
    'mo4' : ['ㅣ', 'ㅟ', 'ㅢ'],
    'mo5' : ['ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅙ', 'ㅚ', 'ㅞ']
}

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

import join
import glob
import pickle
import re
import hgtk

jaum = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']

titles = en_kr.en_kr_start()



def g2pEng(word):
    print("단어를 입력하세요.")
    inputword = word
    inputword = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', inputword)
    inputword = inputword.replace('\n', ' ')
    inputword_list = inputword.split()

    result = []

    for i in inputword_list:

        pron = runKoG2P(i, 'rhyme_dict\\KoG2P-master\\rulebook.txt') # 발음
        pron = pron.split(sep=' ')

        # print(pron)

        word = ''
        
        for j in pron:
            word += dic[j][0]

        word = join.join_jamos(word)

        for k in jaum: # 이응 발음 생략된거 수정
            word = word.replace(k, 'ㅇ'+k)

        word = join.join_jamos(word)

        # print('-> ' + word) # 최종 발음

        chos = []
        jungs = []
        jongs = []

        for l in range(0, len(word)):
            a = hgtk.letter.decompose(word[l])
            chos.append(a[0])
            jungs.append(a[1])
            jongs.append(a[2])

        

        jungs_club = {

        }

        # item = moumtype.get('mo1')

        # print('모음 타입 : ' + str(jungs))

        # <트레이서> 의 각각 모음 타입 [ㅡ, ㅔ, ㅣ, ㅓ] 의 

        for ju in enumerate(jungs):
            jungs_club[ju[0]] = moumtype_rev[moumtype[ju[1]]]

        # print(jungs_club)
    
        for i in titles: # 나무위키 특수문자, 영어 처리

            original = i
            
            i = re.sub('[ㄱ-ㅎ]', '', i)

            reg = re.findall('[[가-힣]+]', i)[0]
            i = reg.replace('[', '').replace(']', '')
            
            # 발음 처리까지 하면 너무 코드가 느리므로 미리 발음 전처리를 해야됨

            # pron = runKoG2P(i, 'KoG2P-master\\rulebook.txt') # 발음
            # pron = pron.split(sep=' ')

            # word = ''
            
            # for j in pron:
            #     word += dic[j][0]

            # word = join.join_jamos(word)

            # for k in jaum: # 이응 발음 생략된거 수정
            #     word = word.replace(k, 'ㅇ'+k)

            # word = join.join_jamos(word)

            # # print(i + ' [' + word + ']') # 최종 발음

            
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
            i = hangul.sub('', i) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
            i = i.replace(' ', '')

            if len(i) < len(chos):
                continue

            word1 = hgtk.letter.decompose(i[-2])
            word2 = hgtk.letter.decompose(i[-1])

            word_moum = []

            for leng in range(len(i), 0, -1):
                word_moum.append(hgtk.letter.decompose(i[-leng])[1])

            # print(i)
            # print(word_moum)

            count = 0


            # # 끝 글자 두개 초성 중성과 inputword의 초성 중성 정확히 일치 (받침만 다름)
            # if chos[-2] == word1[0] and \
            #     jungs[-2] == word1[1] and \
            #     chos[-1] == word2[0] and \
            #     jungs[-1] == word2[1]:
            #     print(i)
            
            # # # 끝 글자 두개 초성 중성과 inputword의 초성 중성이 같은 유사발음
            # if jaumtype[chos[-2]] == jaumtype[word1[0]] and \
            #     moumtype[jungs[-2]] == moumtype[word1[1]] and \
            #     jaumtype[chos[-1]] == jaumtype[word2[0]] and \
            #     moumtype[jungs[-1]] == moumtype[word2[1]]:
            #     print(i)
            #     # print(i + ' [' + word + ']')

            # 끝 글자 두개 초성 중성과 inputword의 초성 중성이 같은 유사발음이고, 나머지 단어들의 모음또한 유사발음
            if jaumtype[chos[-2]] == jaumtype[word1[0]] and \
                jaumtype[chos[-1]] == jaumtype[word2[0]]:
                    for x in range(-1, -len(word)-1, -1):
                        # print(i)
                        # print(word_moum[-x])
                        # print(jungs_club[-x])
                        # print(word_moum)
                        # print(jungs_club)
                        if word_moum[x] in jungs_club[len(word)+x]: #word_moum[-1-2-3-4] in jungs_club[3-2-1-0]
                            count += 1
                        if count == len(word):
                            # print(original)
                            result.append(original)
                            continue
    return result
                        

# r = g2pEng('이어')

# print(r)

            


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

