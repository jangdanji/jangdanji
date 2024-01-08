
import time
import re

from konlpy.utils import pprint

from konlpy.tag import Okt

okt = Okt()

sentence = u'만 6세 이하의 초등학교 취학 전 자녀를 양육하기 위해서는 머리칼'
words = okt.nouns(sentence)

print(words)



# text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)
# text = text.replace('\n', ' ')



# 뒤쪽에 갖다 붙인다고 치면 이렇게 나오면 문법이 맛이감

# 	ex 말해줘 한 번만 -> 말해줘한, 번만

# 앞쪽에 갖다 붙인다고 치면 이런식으로 나오면 또 안됨

# 	ex 응가싼 채 넘어짐 -> 응가싼, 채넘어짐

# NCP	서술성명사
# NCN	비서술성명사
# NQ	고유명사
# NB	의존명사
# NN	수사
# NP	대명사
# PV	동사
# PA	형용사
# PX	보조 용언
# MM	관형사
# MA	부사
# II	감탄사
# JC	격조사
# JX	보조사
# JP	서술격 조사
# EP	선어말어미
# EF	종결 어미
# EC	연결 어미
# ET	전성 어미
# XP	접두사
# XSN	명사파생 접미사
# XSV	동사 파생 접미사
# XSM	형용사파생 접미사
# XSA	부사파생 접미사
# S	기호
# F	외국어
	