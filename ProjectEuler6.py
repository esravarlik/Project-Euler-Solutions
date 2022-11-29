#ProjectEuler 6

sum = 0 
sum2 = 0 
for i in range(1,101): 
    sum += i*i 
for j in range(1,101): 
    sum2 += j 
sum2 = sum2*sum2 
print(sum2 - sum)
