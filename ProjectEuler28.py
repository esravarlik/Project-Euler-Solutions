#ProjectEuler28 

list1 = [1] 
n = 2 
i= 0 
while len(list1) < (2*1001)-1: 
    temp = i 
    while i < (temp + 4): 
        list1.append(list1[i]+n) 
        i += 1 
    n += 2 
    
print(sum(list1))
