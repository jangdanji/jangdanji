from decompose import chosung, jungsung

yourText = "굳이"

CHO = chosung(yourText)
JUNG = jungsung(yourText)

print(yourText + f' : {len(yourText)}글자 단위마다 검사합니다.'); print()
print(f'"{yourText}" 의 초성타입은 {CHO}, 중성타입은 {JUNG} 입니다.')
