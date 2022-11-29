#ProjectEuler30 

def up(x): 
    sum = 0 
    for i in range(2,1000000): 
        sum2 = 0 
        for j in str(i): 
            sum2 += pow(int(j),x) 
        if sum2 == i: 
            sum += sum2 
    print(sum) 
up(5)
