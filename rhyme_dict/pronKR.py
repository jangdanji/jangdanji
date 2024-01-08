"""
라임 전용 발음 변환기
발음 변환기이지만 라임에 영향을 주지 않는 발음 변화는 무시함


라임에 영향을 주는 음운변동
1. 구개음화 (같이 -> 가치)

2. ㅎ 격음화 : ㄱㄷㅂㅈ 가 ㅋㅌㅍㅊ 로 됨
	ㄱㄷㅂㅈ + 초성 ㅎ
	국화 -> 구콰


3. 소리의 중화 (있어 -> 이써, 믿어 -> 미더)
	예외 : ㅇ, ㅎ
	잉어는 잉어고 닿아는 다아임 라임에 영향 안줌

4. 소리의 탈락 (밟아 -> 발바)

5. ㄳ ㄵ ㄼ ㄽ ㄾ ㅄ 이건 앞에꺼로 발음함

6. ㄺ ㄻ ㄿ 이건 뒤에꺼로 발음함-  닭 삶 읊다

7. 비음화


생각해보니 받침은 전혀 중요하지 않은 거 아님?
생각해보니 아닌거같다 발음하기 힘든 단어도 걸러내야됨
ex 급락률


"""


"""
이중포문으로 경우의 수를 전부 구하고 진행했다
탈락이 되는 경우 띄어쓰기로 공백을 메꿈

한 글자의 경우 문법이 맞지않아도 뒤 쪽에 그냥 갖다붙이는 걸로 하자 (가사의 시작부터 첫글자면 오류..)
ex) 그런 적 없다 -> 그런적, 없다
ex) 당신이 할 일이나 하쇼 -> 

한 글자 단어 어떡함?

뒤쪽에 갖다 붙인다고 치면 이렇게 나오면 문법이 맛이감

	ex 말해줘 한 번만 -> 말해줘한, 번만

앞쪽에 갖다 붙인다고 치면 이런식으로 나오면 또 안됨

	ex 응가싼 채 넘어짐 -> 응가싼, 채넘어짐


"""

endrule = {
	'ㄱ' : 'ㄱ',
	'ㄲ' : 'ㄱ',
	'ㅋ' : 'ㄱ',
	'ㄴ' : 'ㄴ',
	'ㄷ' : 'ㄷ',
	'ㅌ' : 'ㄷ',
	'ㅅ' : 'ㄷ',
	'ㅆ' : 'ㄷ',
	'ㅈ' : 'ㄷ',
	'ㅊ' : 'ㄷ',
	'ㅎ' : 'ㄷ',
	'ㄹ' : 'ㄹ',
	'ㅁ' : 'ㅁ',
	'ㅂ' : 'ㅂ',
	'ㅍ' : 'ㅂ',
	'ㅇ' : 'ㅇ'
}
# ㅎ 격음화되는 자음

gyuk = {
		'ㄱ' : 'ㅋ',
		'ㄺ' : 'ㅋ',
		'ㄷ' : 'ㅌ',
		'ㅂ' : 'ㅍ',
		'ㄼ' : 'ㅍ',
		'ㅈ' : 'ㅊ',
		'ㄵ' : 'ㅊ'
		}

# 겹받침
gyup = {
	'ㄳ' : ['ㄱ', 'ㅅ'],
	'ㄵ' : ['ㄴ', 'ㅈ'],
	'ㄼ' : ['ㄹ', 'ㅂ'],
	'ㄽ' : ['ㄹ', 'ㅅ'],
	'ㄾ' : ['ㄹ', 'ㅌ'],
	'ㅄ' : ['ㅂ', 'ㅅ'],
	'ㄺ' : ['ㄹ', 'ㄱ'],
	'ㄻ' : ['ㄹ', 'ㅁ'],
	'ㄿ' : ['ㄹ', 'ㅍ']
	}



# from konlpy.tag import Okt
import hgtk
import join

import re

while True:

	inputword = input()

	# konlpy = Okt()
	# result = konlpy.pos(inputword, 9)

	# print(result)


	if len(inputword) > 0:

		inputword = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', inputword)
		inputword = inputword.replace('\n', ' ')

		inputword_list = inputword.split()


		print(inputword_list)

		for i in inputword_list:
			if len(i) == 1:
				pass

		for w in inputword_list:

			print(w)

			if len(w) == 2:
				pass
			else:
				pass

			w = hgtk.letter.decompose(w[-2]) + hgtk.letter.decompose(w[-1])

			word = ''

			for i in range(0, len(w)) : word += w[i]

			mix = word[2] + word[3]

			if len(word) == 4:
				pass

			elif mix in 'ㄱㄴ ㄱㅁ ㄱㄹ ㄲㄴ ㄲㅁ ㄲㄹ ㅋㄴ ㅋㅁ ㅋㄹ ㄳㄴ ㄳㅁ ㄳㄹ ㄺㄴ ㄺㅁ ㄺㄹ':
				mix = 'ㅇ' + mix[-1]

			elif mix in 'ㄷㄴ ㄷㅁ ㄷㄹ ㅅㄴ ㅅㅁ ㅅㄹ ㅆㄴ ㅆㅁ ㅆㄹ ㅈㄴ ㅈㅁ ㅈㄹ ㅊㄴ ㅊㅁ ㅊㄹ ㅌㄴ ㅌㅁ ㅌㄹ ㅎㄴ ㅎㅁ ㅎㄹ':
				mix = 'ㄴ' + mix[-1]

			elif mix in 'ㅂㄴ ㅂㅁ ㅂㄹ ㅍㄴ ㅍㅁ ㅍㄹ ㄼㄴ ㄼㅁ ㄼㄹ ㄹㄴ ㄹㅁ ㄹㄹ ㅊㄴ ㅊㅁ ㅊㄹ ㅄㄴ ㅄㅁ ㅄㄹ':
				mix = 'ㅁ' + mix[-1]

			elif mix in 'ㅎㄱ ㅀㄱ ㄶㄱ ㅎㄷ ㅀㄷ ㄶㄷ ㅎㅈ ㅀㅈ ㄶㅈ': # ex : 않고 쌓고 
				mix = mix.replace('ㄱ', 'ㅋ').strip('ㅎ') \
						.replace('ㄷ', 'ㅌ').strip('ㅎ') \
						.replace('ㅈ', 'ㅊ').strip('ㅎ')

			elif mix[0] in 'ㄱㄲㅋㄳㄺ' and mix[1] == 'ㅎ' and word[4] not in 'ㅣㅕ':
					mix = mix.replace(mix[1], 'ㅋ').strip('ㅎ')  # ex : 국화 약함
			elif mix[0] in 'ㄷㅆㅈㄵㅊㅌㅎㅂㅍㄼㄿㅄ' and mix[1] == 'ㅎ' and word[4] not in 'ㅣㅕ':
					mix = mix.replace(mix[1], 'ㅌ').strip('ㅎ') # ex : 꽃향
			elif mix[0] in 'ㅂㅍㄼㄿㅄ' and mix[1] == 'ㅎ' and word[4]:
					mix = mix.replace(mix[1], 'ㅍ').strip('ㅎ')  # ex :

			elif mix in 'ㅎㄴ':
				mix = mix.replace('ㅎ', 'ㄴ')

			elif mix in 'ㄶㄴ ㅀㄴ': 
				mix = mix.replace('ㄶ', 'ㄴ').replace('ㅀ', 'ㄹ')

			elif mix+word[4] in 'ㄷㅇㅣ': # 구개음화
				mix = mix.replace('ㄷ', 'ㅈ').replace('ㅇ', '')

			elif mix+word[4] in 'ㄷㅎㅣ ㄷㅎㅕ ㅌㅇㅣ ㅌㅎㅕ': # 구개음화
				mix = mix.replace('ㄷ', 'ㅊ').replace('ㅌ', 'ㅊ').replace('ㅎ', '').replace('ㅇ', '')
				

			elif mix[1] == 'ㅇ':

				if mix in "ㅇㅇ ㅎㅇ ㄶㅇ ㅀㅇ" : # 예외 ex) 잉어 낳아 중요
					
					if mix == 'ㅎㅇ': 
						mix = 'ㅇ'
					elif mix == 'ㄶㅇ': 
						mix = 'ㄴ'
					elif mix == 'ㅀㅇ': 
						mix = 'ㄹ'
					else:
						pass

				elif mix[0] in 'ㄳㄵㄼㄽㄾㅄㄺㄻㄿ':
					mix = gyup[mix[0]][0] + gyup[mix[0]][1]
					
				else:
					mix = mix.replace('ㅇ', '')
			
			if len(mix) == 1:
				pass
			else:
				if mix[0] in 'ㄲㅋㄳㄺ':
					mix = 'ㄱ' + mix[1]
				elif mix[0] in 'ㄵㄶ':
					mix = 'ㄴ' + mix[1]
				elif mix[0] in 'ㅌㅅㅆㅈㅊㅎ':
					mix = 'ㄷ' + mix[1]
				elif mix[0] in 'ㄾㄻㅀㄽㄼ':
					mix = 'ㄹ' + mix[1]
				elif mix[0] in 'ㅍㅄㄿ':
					mix = 'ㅂ' + mix[1]

			# 끝글자도 끝소리 규칙 적용시키기

			# 띄어쓰기가 된 첫글자 단어는


			result = word.replace(word[2:4], mix)

			result = join.join_jamos(result)

			print('->' + result)

			mix = ''
			word = ''

		"""
		ㄱ계 : ㄱㄲㅋㄳㄺ
		ㄴ계 : ㄴㄵ
		ㄷ계 : ㄷㅌㅅㅆㅈㅊㅎ
		ㄹ계 : ㄹㄾㄻ
		ㅁ계 : ㅁ   
		ㅂ계 : ㅂㅍㅄㄿ
		ㅇ계 : ㅇ
		"""

