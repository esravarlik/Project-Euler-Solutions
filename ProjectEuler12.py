#ProjectEuler 12

list1 = []
sum1 = 0
sum2 = 0
for i in range(1,76576503):
    sum1 += i
    list1.append(sum1)
    for j in range(1,sum1+1):
        if sum1 % j == 0:
            sum2 += 1
            if sum2 == 500:
                print(i)
                break
