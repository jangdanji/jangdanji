# from numpy import result_type
# from pysle import isletool
# from pysle import pronunciationtools
# from g2p_en import G2p
import join
import re

from os.path import join as j

from pysle import isletool

def en_kr_start():

    englishWords = []

    # You can specify a custom dictionary to search through.
    # By default, the LexicalTool will load the original ISLEdict
    root = j(".", "files")
    import getpass
    isle = isletool.Isle(j (root, f'C:\\Users\\{getpass.getuser()}\\Documents\\GitHub\\jonathan\\rhyme_dict\\KoG2P-master\\ISLEdict.txt'))


    # g2p = G2p()

    char = { # ㄱㄷㅂㅈㅊㅋㅌㅍㄸ > ㄴㄹㅁㅎ > ㅅ ( sm sl sn 는 ㅅ가 약세인듯)
        "ɵ" : ["ㄸ", "ja", 1],
        "t" : ["ㅌ", "ja", 1],
        "tʃ" : ["ㅊ", "ja", 1],
        "ʒ" : ["ㅈ", "ja", 1],
        "b" : ["ㅂ", "ja", 1],
        "dʒ" : ["ㅈ", "ja", 1],
        "d" : ["ㄷ", "ja", 1],
        "f" : ["ㅍ", "ja", 1],
        "g" : ["ㄱ", "ja", 1], 
        "v" : ["ㅂ", "ja", 1],
        "z" : ["ㅈ", "ja", 1], 
        "ð" : ["ㄷ", "ja", 1], # the
        "k" : ["ㅋ", "ja", 1],
        "p" : ["ㅍ", "ja", 1],

        "h" : ["ㅎ", "ja", 2],
        "l" : ["ㄹ", "ja", 2], # ㄹ은 그냥 유음이라서 없는걸로 치고 나중에 초성칸이 비었으면 ㅇ으로 대체하도록 ㄱㄱ
        "m" : ["ㅁ", "ja", 2],
        "n" : ["ㄴ", "ja", 2],
        "r" : ["ㄹ", "ja", 2], # ㄹ유음 생략 이하동문

        "s" : ["ㅅ", "ja", 3],  
        "j" : ["", "ja", 3], # y
        "ʃ" : ["ㅅ", "ja", 3], # sh
        "w" : ["ㅇ", "ja", 3], # 생략
        "ɾ" : ["ㅇ", "ja", 3], # r

        "ɹ" : ["ㄹ", "ja", 3], 

        "ŋ" : ["ㅇ", "mo"],
        "æ" : ["ㅔ", "mo"],
        "u" : ["ㅜ", "mo"],
        "oʊ" : ["ㅗ", "mo"], 
        "i" : ["ㅣ", "mo"],
        "ei" : ["ㅔ", "mo"],
        "aʊ" : ["ㅏ", "mo"],
        "ɑ" : ["ㅏ", "mo"],
        "ɑɪ" : ["ㅏ", "mo"],
        "ɔ" : ["ㅏ", "mo"],
        "ɔi" : ["ㅏ", "mo"],
        "ə" : ["ㅓ", "mo"],
        "ɚ" : ["ㅓ", "mo"], # ~r
        "ɛ" : ["ㅔ", "mo"], # ~r
        "ɝ" : ["ㅓ", "mo"], # ~r
        "ɪ" : ["ㅣ", "mo"],
        "ʊ" : ["ㅜ", "mo"],
        "æ" : ["ㅐ", "mo"],
        "ʌ" : ["ㅓ", "mo"],
        "ae" : ["ㅐ", "mo"],
        "l̩" : ["ㅡㄹ", "mo"],
        "n̩" : ["ㅡㄴ", "mo"],
        "ɝ" : ["ㅓ", "mo"],
        "a" : ["ㅏ", "mo"],
        "e" : ["ㅔ", "mo"],
        "o" : ["ㅗ", "mo"],
        " " : [" ", " "]
    }



    moum = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
    jaum = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']


    import quote_list as ql

    phrases = ql.sentences

    meaning = ql.meaning

    for idx, p in enumerate(phrases):

        # print(p)

        p = p.split(' ')
        
        result = ''
        word = ' ' # 일부러 남겨둠
        ipa = [' ', ' ', ' ']

        for p1 in p:

            # if isle.contains(p1) != True:
            #     continue

            try:
                text = isle.lookup(p1)[0].toList()[0]
            except:
                p1 = p1.replace('\'s', '')
                text = isle.lookup(p1)[0].toList()[0]

            # print(text)
            
        

            for t1 in text: # [[ ... ]] # 각각 음절에서 자+모 형식 띄어서 분리 (자음 단독일 경우 냅둠), 이중자음 따로 분리, 첫음절 모+자면 붙임

                # print(t1)

                for t2 in t1: # [  ..  ]
                    
                    t2 = re.sub('[˺ˈˌ#.]', '', t2)
                    ipa.append(t2)

                    # if char[ipa[-2]][1] == 'ja' and char[ipa[-1]][1] == 'ja':
                    #     ipa.append(' ')
                    if char[ipa[-2]][1] == 'ja' and char[ipa[-1]][1] == 'mo': 
                        ipa.append(' ')
                    elif char[ipa[-2]][1] == 'mo' and char[ipa[-1]][1] == 'ja':
                        ipa.append(' ')
                    elif char[ipa[-2]][1] == 'mo' and char[ipa[-1]][1] == 'mo':
                        ipa.append(' ')
                    elif ipa[-2] == ' ' and char[ipa[-1]][1] == 'mo':
                        ipa.append(' ')

                ipa.append(' ')

            for r in range(1, len(ipa)-2): # 첫 자음은 x

                if re.search('[bcdflnps]t mo', ipa[r-1] + ipa[r] + ipa[r+1] + char[ipa[r+2]][1]):
                    pass
                elif ipa[r] + ipa[r+1] + char[ipa[r+2]][1] == 't mo':
                    ipa[r] = 'l'



            while True: # 처음 공백 제거
                if ipa[0] == ' ':
                    del ipa[0]
                else:
                    break
            while True: # 마지막 공백 제거
                if ipa[-1] == ' ':
                    del ipa[-1]
                else:
                    break

            # print(ipa)

            pos = []

            if ' ' not in ipa:
                first = 0
                last = 0
            else:
                for i in range(len(ipa)):
                    if ipa[i] == ' ':
                        pos.append(i)

                first = pos[0] # ~ 첫음절 위치
                last = pos[-1] # 마지막 음절 ~ 위치


            for i in range(0, last): # if 이중자음 : 강세만 남기고 제거 (끝음이 이중자음이면 걍 냅둠)

                # print('검사 : ' + ipa[-i-1] + ' ' + ipa[-i])

                # print(str(char[ipa[i]][2]) + ' ' + str(char[ipa[i+1]][2]))
                

                if char[ipa[i]][1] == 'ja' and char[ipa[i+1]][1] == 'ja':
                    
                    # print(ipa[i] + ipa[i+1])
                    if char[ipa[i]][2] > char[ipa[i+1]][2]:
                        ipa[i] = ' '
                    elif char[ipa[i]][2] == char[ipa[i+1]][2]:
                        pass
                    else:
                        ipa[i+1] = ' '
            
            # print(ipa)

            first_noun = False

            for i in range(first, len(ipa)): # 첫 음절, 마지막 음절 제외 초성 유음 제거

                if first_noun == True and ipa[i] != ' ':
                    if ipa[i] in 'ɹɾw':
                        # print(ipa[i])
                        ipa[i] = ' '
                    
                
                if ipa[i] == ' ':
                    first_noun = True
                else: first_noun = False
            
            ipa.append(' ')

            # print(ipa)

        
        # print(ipa)
        
        for ip in ipa:
            result += char[ip][0]

        result = join.join_jamos(result.replace(' ', ''))

        for m in moum: # 이응 발음 생략된거 수정
            result = result.replace(m, 'ㅇ'+m)

        result = join.join_jamos(result)
        # if re.search('e t', phrases[idx]):
        if True:
            englishWords.append(phrases[idx] + ' [' + result + '] : ' + meaning[idx])
            # print(phrases[idx] + ' [' + result + '] : ' + meaning[idx]) # 뜻 아직 없으면 meaning 각주 ㄱ
            # print('')

    return englishWords


# script = en_kr_start()




    # fin = re.findall('[ㄱㄴㄷㄹㅁㅂㅅㅈㅊㅋㅌㅍㅎㄸ] [ㅏㅔㅣㅗㅜㅓㅡㅐ]+[ㄱ-ㅎ]{0,1}', word)

    # for f in fin:
    #     f_mod = join.join_jamos(f.replace(' ', ''))
    #     word = word.replace(f, f_mod)
    
    # # print(word)

    # word = word.replace(' ', '')

    # word = join.join_jamos(word)

    # # print(word)

    # for m in moum: # 이응 발음 생략된거 수정
    #     word = word.replace(m, 'ㅇ'+m)

    # word = join.join_jamos(word)
    
    
    # print(' [' + word + '] : ' + meaning[idx])
    # print('')
            

        


    # for pron in p:
    #     result += char[pron]












# # result.append(' ')
# print(phrase)
# print(result)

# result = join.join_jamos(result)
        
# for m in moum: # 이응 발음 생략된거 수정
#     result = result.replace(m, 'ㅇ'+m)

# result = join.join_jamos(result)

# print(result)
