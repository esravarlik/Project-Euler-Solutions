#ProjectEuler25 

a = 1 
b = 1 
c = a + b 
sum = 3 
while len(str(c)) < 1000: 
    a = b 
    b = c 
    c = a + b 
    sum += 1 
    
print(sum)
