#ProjectEuler5

for i in range(1,300000000): 
    sum = 0 
    for j in range(1,21): 
        if i % j == 0: 
            sum += 1 
    if sum == 20: 
        print(i)
