myList=[
    ('BTS', 2),
    ('TWICE', 4),
    ('아이유', 1),
    ('양다일', 3)
]
myList.sort()
print(myList)
myList.sort(key=lambda x:x[1])
print(myList)

myList=[
    ('BTS', 40000),
    ('TWICE', 20000),
    ('아이유', 100000),
    ('양다일', 30000)
]
myList.sort(key=lambda x:x[1], reverse=True)
print(myList)
print('가장 비싼 앨범의 가수는', myList[0][0])

# 튜플()은 바꿀 수가 없어서(상수), 더 빨리 처리된다.