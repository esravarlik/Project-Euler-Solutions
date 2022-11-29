#ProjectEuler34 

sum2 = 0 
for k in range(3,1000000): 
    y = list(str(k)) 
    sum = 0 
    for i in y: 
        t = 1 
        for j in range(1,int(i)+1): 
            t *= j 
        sum += t 
        if sum == k: 
            sum2 += sum 
            
print(sum2)
