#ProjectEuler 10

sum = 0 
for x in range(2,2000000): 
    for i in range(2,x): 
        if x % i == 0: 
            break 
    else: 
        sum += x 
print(sum)
