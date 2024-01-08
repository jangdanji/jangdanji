
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

def check_rhyme_ultimate(userWords, compareWords): # 발음 그대로 넣어야됨

    userChosung = []
    userJungsung = []

    compareChosung = []
    comparejungsung = []

    # compareWordDecompose = hgtk.letter.decompose(word)

    for word in userWords:
        
        userWordDecompose = hgtk.letter.decompose(word)

        userChosung.append(
            userWordDecompose[0]
        )

        userJungsung.append(
            userWordDecompose[1]
        )
    
    wordLength = len(userWords)

    for word in compareWords[-wordLength::]:
        
        compareWordDecompose = hgtk.letter.decompose(word)

        compareChosung.append(
            compareWordDecompose[0]
        )

        comparejungsung.append(
            compareWordDecompose[1]
        )

    print(userChosung)
    print(userJungsung)
    print(compareChosung)
    print(comparejungsung)


        
check_rhyme_ultimate('섹스', '항문쇳스')

