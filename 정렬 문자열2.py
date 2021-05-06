# 운동회에 4명의 친구가 참석한다
# 사전순으로 가장 먼저 출발하는 친구의 이름을 출력하시오
# [입력] 홍길동 김철수 김삿갓 이순신
# [출력] 김삿갓

friends = list(input().split())
friends.sort()
print(friends[0])

