#ProjectEuler39

highest = 1 
highest_p = 0

for i in range(1000): 
    triples = 0 
    for j in range(i // 3): 
        for k in range(j, i // 2): 
            if k ** 2 + j ** 2 == (i - j - k) ** 2: 
                triples += 1
                
    if triples > highest: 
        highest = triples 
        highest_p = i 
        
print(highest_p)
