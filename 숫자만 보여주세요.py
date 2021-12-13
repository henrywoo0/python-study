# 문자열들 속에 암호 숫자가 있다
# 숫자만 뽑아 출력한 것에 5를 더한 것이 암호이다.
# 암호를 찾아보자.
#
# 입력
# a123b4
#
# 출력
# 1239

string = input()
num = 0
for i in range(len(string)):
	if string[i].isdigit():
		num *= 10
		num += int(string[i])
print(num + 5)
