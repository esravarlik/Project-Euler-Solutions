#ProjectEuler2
x = 1 
y = 2 
result = [] 
while y < 4000000: 
    x = x + y 
    y = x + y 
    if x % 2 == 0: 
        result.append(x) 
    if y  % 2 == 0: 
        result.append(y) 
answer = sum(result) 
print(answer + 2) # 2 initial y value
