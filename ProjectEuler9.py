#ProjectEuler 9 

for i in range(1,1000): 
    for j in range(1,1000): 
        for k in range(1,1000): 
            if (i>j>k and i + j + k ==1000 and k*k + j*j == i*i): 
                print("i:",i,"j:",j,"k:",k) 
                break 
product = i*j*k 
print(product)
