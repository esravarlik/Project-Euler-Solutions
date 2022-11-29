#ProjectEuler23 

list1 = [] 
for j in range(1,28123): 
    list1.append(j) 
    
list2 = [] 
for x in range(1,28123): 
    sum1 = 0 
    for i in range(1,x): 
        if x % i == 0: 
            sum1 += i 
    if x < sum1: 
        list2.append(x) 
        
list3 = [] 
for bol in list2: 
    for bolsum in list2: 
        sum2 = bol + bolsum 
        list3.append(sum2) 
        
difference = set(list1) - set(list3) 
list_difference = list(difference)

print(sum(list_difference))
