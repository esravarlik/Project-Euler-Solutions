#ProjectEuler 7

sum = 0
for x in range(2,200000):
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        sum += 1
        if sum == 10001:
            print(x)
            break
