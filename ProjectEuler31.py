#ProjectEuler31 
coins = [200,100,50,20,10,5,2] 
counter = 0 
for x in range(2): 
    for a in range(3): 
        if coins[0]*x + coins[1]*a > 200: 
            break 
        for b in range(5): 
            if coins[0]*x +coins[1]*a+b*coins[2] > 200: 
                break 
            for c in range(11): 
                if coins[0]*x +coins[1]*a + b*coins[2] +coins[3]*c > 200: 
                    break 
                for d in range(21): 
                    if coins[0]*x +coins[1]*a + b*coins[2] +coins[3]*c + coins[4]*d > 200: 
                        break 
                    for e in range(41): 
                        if coins[0]*x+coins[1]*a+b*coins[2] + coins[3]*c +coins[4]*d +coins[5]*e > 200: 
                            break 
                        for f in range(101): 
                            if coins[0]*x + coins[1]*a + coins[2]*b+ coins[3]*c + coins[4]*d + coins[5]*e + coins[6]*f <= 200: 
                                counter += 1 
                                
print(counter)
