#ProjectEuler 35 

import math 
def rotate(l, n): 
    return l[n:] + l[:n] 
  
def isPrime(n): 
    for i in range(2, int(math.sqrt(n)+1)): 
        if n % i == 0: 
            return False; 
    return n>1; 
  
count=1; 
for n in range(3, 1000000): 
    if isPrime(n): 
        test=1; 
        for i in range(1,len(str(n))): 
            if not isPrime(int(rotate(str(n),i))): 
                test=0 
                break 
        if test: 
            count+=1 
            #print(n)
            
print(count)
