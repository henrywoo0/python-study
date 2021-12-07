# 텍스트 압축은 숫자가 없는 문자열에 유효하다.
# 가장 단순한 방법은 문자와 반복 횟수로 표현하는 것이다.
# 
# 입력
# AAAAAAABBCCCDEEEEFFFFFG
# 
# 출력
# A7B2C3D1E4F5G1

str = input()
str = str + ' '
cnt = 0
for i in range(len(str)):
	if str[i] == ' ':
		break
	if str[i] == str[i + 1]:
		cnt += 1
	else:
		cnt += 1
		print(str[i], cnt, sep='', end='')
		cnt = 0
