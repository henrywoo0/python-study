def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def LCM(a, b):
    return (a * b) / GCD(a, b)

print(GCD(10, 12))
print(LCM(10, 12))
