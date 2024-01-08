import pickle
import glob
import re
# from konlpy.tag import Kkma

# konlpy = Kkma()

# 데이터 마지막 문장에 \n을 집어넣어주자 (이유 : 마지막 단어가 한 글자라면 구분할 수 있는게 없음)
# 정규표현식 . 는 띄어쓰기는 포함안하는구나
# if 한글자 단어 + 줄 바꿈이면 그 이전 단어와 붙여도되나?

# 그냥 욕심내서 다 할려 하지말고 처음과 끝부분만 긁어서 ㄱ

def save_pickle(data, filename):

    with open(f"rhyme_dict\\lyrics\\{filename}.pickle", 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def open_lyrics():

    # ret = glob.glob(f'rhyme_dict\\lyrics\\rnb_lyrics.pickle')
    # with open(ret[0], 'rb') as f: rnb = pickle.load(f)
    # # rnb 19600곡 중 113개가 로드실패 (실패했으면 링크로 저장했음)
    # # 예) https://www.melon.com/song/detail.htm?songId=35059554

    ret = glob.glob(f'rhyme_dict\\lyrics\\bal_lyrics.pickle')
    with open(ret[0], 'rb') as f: bal = pickle.load(f)


    

    len0 = len(bal)

    all = ''

    for r in bal:
        
        print('가사 전처리중... : ' + str(bal.index(r)) + ' / ' + str(len0))

        r = '\n' + r[0:] + '\n'
        all += r

    sort1 = re.findall('\n[가-힣]+ [가-힣]+', all) # 첫마디 필터
    sort1 = list(set(sort1)) # 중복 제거
    len1 = len(sort1) # 최종 갯수

    for s1 in sort1:
        idx = sort1.index(s1)
        s1 = re.sub('[ \n]', '', s1)
        sort1[idx] = s1
        print(str(idx) + ' / ' + str(len1))

    print('멜론 한국어 첫 마디 데이터 로드 완')

    sort2 = re.findall('[가-힣]+ [가-힣]+\n', all) # 끝마디 필터
    sort2 = list(set(sort2)) # 중복제거
    len2 = len(sort2) # 최종 갯수

    for s2 in sort2:
        idx = sort2.index(s2)
        s2 = re.sub('[ \n]', '', s2)
        sort2[idx] = s2
        print(str(idx) + ' / ' + str(len2))

    print('멜론 한국어 끝 마디 데이터 로드 완 ')

    print(sort2)

    save_pickle(sort1, 'bal_lyrics_start')
    save_pickle(sort2, 'bal_lyrics_end')

    # sortEng1 = re.findall('\n[a-z]+ [a-z]+', all) # 첫마디
    # sortEng2 = re.findall('[a-z]+ [a-z]+\n', all) # 끝마디

    return sort1, sort2 #, sortEng1, sortEng2

open_lyrics()

# # 명사 뽑기
# all = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》[a-z][0-9]]', '', all)
# noun = konlpy.nouns(all)

# for n in noun:
#     if len(n) < 2:
#         noun.remove(n)

# noun = set(noun)

# print(noun)
# print(len(set(noun)))





# for r in rnb:

#     r = '\n' + r[0:] + '\n'

#     print(r)

#     findal = re.findall(' [가-힣]\n[가-힣] | [가-힣]\n|\n[가-힣] ', r)

#     print('자동 수정 : ' + str(findal))

#     for fin in findal:
#         fin2 = fin.replace(' ', '')
#         r = r.replace(fin, fin2)

#     # word = re.finditer('[ \n]([가-힣][ \n])+', r) # 줄바꿈or띄쓰 (한글자+공백or줄바꿈)반복
#     sentence = re.finditer('.+[ \n]([가-힣][ \n])+.+', r) # 줄바꿈or띄쓰 (한글자+공백or줄바꿈)반복

#     for s in sentence:
        
#         # 전처리
#         print('>>> ' + str(s))
#         s = ' ' + str(s.group()) + ' '

#         print()

#         word = re.finditer('[ \n]([가-힣][ \n])+', str(s))

#         for w in word:

#             print(w)

#             w = w.group()

#             if w in modi:
#                 print(w + ' : 이미 존재합니다. \n')
#                 continue
            

#             else:
#                 ip = input('수정본을 입력하세요 :')
#                 if ip == '': # 암것도 안쓰면 패스
#                     pass
#                 else:
#                     modi[w] = ip

#     for repl in modi:

#         r = r.replace(repl, modi[repl])

#     if re.findall('[ \n]([가-힣][ \n])+', r) != []:
#         print(r)
#         print('<<<하나짜리 발견>>>')

#     save_pickle(modi, 'modi_word')
    
