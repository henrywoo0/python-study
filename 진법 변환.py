# 양의 정수를 입력받아 진법 변환하는 코드를 완성하시오.
# 진법은 2진법, 8진법, 16진법이 나오도록 합니다.
#
# 입력
# 60
#
# 출력
# 0b111100
# 0o74
# 0x3c

num = int(input())
print(bin(num))
print(oct(num))
print(hex(num))
