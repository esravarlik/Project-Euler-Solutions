#ProjectEuler15 
# 40! / (20!*20!) 

sum = 1 
i = 40 
while i > 1: 
    sum *= i 
    i -= 1 
sum1 = 1 
j = 20 
while j > 1: 
    sum1 *= j 
    j -= 1 
x = sum/(sum1*sum1) 
print(x)
