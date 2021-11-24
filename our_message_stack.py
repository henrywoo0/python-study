msg = list(input())
stack = []

for i in range(0, len(msg)):
    if msg[i].isdigit():
        for j in range(0, int(msg[i])):
            print(stack.pop(), end='')
    else:
        stack.append(msg[i])
