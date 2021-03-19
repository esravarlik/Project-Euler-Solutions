#Project Euler 27
def prime(num):
    if num < 0 or num == 1:
        return False
    for i in range(2, int(pow(num,0.5))):
        if num % i == 0:
            return False
    return True

count = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 1
        while prime(pow(n,2) + a*n + b):
            n += 1
        if n > count:
            count = n
            result = a * b
print(result)