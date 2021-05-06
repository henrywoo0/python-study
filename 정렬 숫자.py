#시험 점수를 입력받았을 때, 1등의 점수를 출력하는 프로그램을 작성하시오
numList=[15,22,8,79,10,8,56,89]
numList.sort() # 오름차순 정렬
print(numList)
print(numList[0]) # 꼴찌의 점수

numList.sort(reverse=True) # 내림차순 정렬
print(numList)
print('1등의 점수', numList[0]) # 1등의 점수

num1 = [1,2,3,4,5,7,3,4,8]

num1.sort(reverse=True)

print(num1[0] - num1[len(num1) - 1])