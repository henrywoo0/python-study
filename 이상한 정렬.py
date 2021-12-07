# 참고로 이 문제는 구글 회사의 전화면접 문제를 쉽게 변형한 것이다.
#
# 정수 배열이 있다. 우리는 좀 특별한 방법으로 정렬을 할 것이다.
# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의 정수는 뒤쪽에 있어야 한다.
# 또한 양의 정수와 음의 정수의 순서에는 변함이 없어야 한다.
# 
# 입력
# -1 1 3 -2 2
# 
# 출력
# -1 -2 1 3 2

li = list(map(int, input().split()))
minus_li = []
plus_li = []

for i in li:
	if(i < 0):
		minus_li.append(i)
	else:
		plus_li.append(i)
		
print(*minus_li, end=' ')
print(*plus_li)
