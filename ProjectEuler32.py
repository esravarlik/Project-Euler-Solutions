#ProjectEuler 32 

pandigital = set() 
for a in range(1, 100): 
    for b in range(1, 9999): 
        if ''.join(sorted("%d%d%d" % (a, b, a*b))) == '123456789': 
            pandigital.add(a * b) 
            
print(sum(pandigital))
