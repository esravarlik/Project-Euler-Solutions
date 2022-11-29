#ProjectEuler26 

max_cycle = 0 
y = 0 
for i in range(2,1000): 
    if i % 2 != 0 and i % 5 != 0: 
        x = 1 
        while (10 ** x) % i != 1: 
            x += 1 
        if x > max_cycle: 
            max_cycle = x 
            y = i 
            
print(y)
