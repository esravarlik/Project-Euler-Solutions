#ProjectEuler 14 

sum1 = 0 
sum2 = 0 
i = 1 

while i < 1000000: 
    n = i 
    t = 1 
    while 1: 
        if n % 2 == 0: 
            n = n / 2 
        else: 
            n = n * 3 + 1 
        t += 1 
        if n == 1: 
            break 
    if t > sum1: 
        sum1 = t 
        sum2 = i 
    i += 1 
    
print(sum2)
