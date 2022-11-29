#ProjectEuler21 

def sumlet(n): 
    sum=1 
    for i in range(2,n): 
        if n%i==0: 
            sum=sum+i 
    return sum
    
sum=0 
for i in range(1,10000): 
    a=sumlet(i) 
    if sumlet(a)==i and a!=i: 
        sum += i 
        
print(sum)
