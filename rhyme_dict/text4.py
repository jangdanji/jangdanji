from typing import Text
import eng_to_ipa as ipa
text = ipa.convert("writer")
print(text)

text = ipa.get_rhymes('sex')
print(text)

s = 'sexy'

print(s[:-1])

def aa():
    asd = 'asd'
    dsa = 'dsa'
    return asd, dsa

print(aa()[0])

for i in range(0, 3):

    print(i)

from dp.phonemizer import Phonemizer

phonemizer = Phonemizer.from_checkpoint('rhyme_dict\\en_us_cmudict_ipa_forward.pt')
p = phonemizer('i don\'t want to ', lang='en_us')
print(p)

# ㅌ을 발음하기 빡시다 싶으면 ㄹ로 되는듯

# 첫글자 ㅌ 끝글자 ㅌ
# 모음이 앞에 있으면 ㄹ 발음 city party
# 자음이 앞에 있으면 ㅌ 발음 after
# 받침이면 받침으로 씀 catch
# th면 th로 발음

# button 벋:은
# better 베럴

# potato
# miste
# partition
# to
# tu

# flap t / d sound (party beautiful)
# 모음과 모음사이 or r과 모음사이

# potato는 애초에 발음이 pta로 시작해서 t소리나는거

# dropped t (interrupt exactly)
# n과 모음사이

# glottal T (mountain button certain)
# [ten]으로 끝나는 단어

# [t] [d]는 접두사의 시작 부분에 올 수 없습니다(~ 제외).
# 마지막 음절은 강세가 없다
# 앞에 모음이나 자식이 오고 뒤에 모음이 옵니다( [ən] 제외 ) .
# raɪɾər
