
import hgtk

jaumtype = {
    'ㄱ' : 'ja1', 'ㄷ' : 'ja1', 'ㅂ' : 'ja1', 'ㅋ' : 'ja1', 'ㅌ' : 'ja1',
    'ㅍ' : 'ja1', 'ㄲ' : 'ja1', 'ㄸ' : 'ja1', 'ㅃ' : 'ja1',
    'ㅅ' : 'ja2', 'ㅈ' : 'ja2', 'ㅊ' : 'ja2', 'ㅆ' : 'ja2', 'ㅉ' : 'ja2',
    'ㄴ' : 'ja3', 'ㄹ' : 'ja3', 'ㅁ' : 'ja3',
    'ㅇ' : 'ja4', 'ㅎ' : 'ja4'
}

moumtype = {
    'ㅏ' : 'mo1', 'ㅑ' : 'mo1', 'ㅘ' : 'mo1',
    'ㅓ' : 'mo2', 'ㅕ' : 'mo2', 'ㅝ' : 'mo2', 'ㅗ' : 'mo2', 'ㅛ' : 'mo2',
    'ㅜ' : 'mo3', 'ㅠ' : 'mo3', 'ㅡ' : 'mo3',
    'ㅣ' : 'mo4', 'ㅟ' : 'mo4', 'ㅢ' : 'mo4',
    'ㅐ' : 'mo5', 'ㅒ' : 'mo5', 'ㅔ' : 'mo5', 'ㅖ' : 'mo5', 'ㅙ' : 'mo5', 'ㅚ' : 'mo5', 'ㅞ' : 'mo5'
}

def check_rhyme_ultimate(userWords, compareWords, length=None): # 발음 그대로 넣어야됨

    wordLength = len(userWords)

    wordLength if length == None else 2 # length 안넣었으면 2

    for uw, cw in zip(userWords, compareWords[-wordLength::]):

        userWordDecompose = hgtk.letter.decompose(uw)
        compareWordDecompose = hgtk.letter.decompose(cw)

        # print(f'{userWordDecompose} / {compareWordDecompose}')
        
        check_jaum = jaumtype[userWordDecompose[0]] == jaumtype[compareWordDecompose[0]]
        check_moum = moumtype[userWordDecompose[1]] == moumtype[compareWordDecompose[1]]

        # print(f'{check_jaum} : {userWordDecompose[0]} / {compareWordDecompose[0]}')
        # print(f'{check_moum} : {userWordDecompose[1]} / {compareWordDecompose[1]}')

        if check_jaum or check_moum == False:
            return False
        
    return True

        
check_rhyme_ultimate('섹스', '텍즈', 2)

