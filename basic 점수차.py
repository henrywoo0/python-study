#5개~10개 사이의 숫자를 입력받을 때 1등과 꼴찌의 점수차 출력.
#[1,2,3,4,5,7,3,4,8]

num1=list(map(int,input().split()))
num1.sort(reverse=True)
print(num1[0] - num1[len(num1) - 1])