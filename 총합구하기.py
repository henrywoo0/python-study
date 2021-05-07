# 숫자를 입력받아 총 합을 구하는 프로그램을 작성하시오
# 1 2 3 4
# 10

num = list(input().split())
new_num = [int(x) for x in num]
print(sum(new_num))

# num = list(map(int, input().split()))
# sum = 0
# print('length :', len(num))
# for i in range(len(num)):
#     sum = sum + num[i]
#
# print(sum)