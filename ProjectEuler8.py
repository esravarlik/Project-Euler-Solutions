num = str("long number here")
max = 0
sum = 1
product_num = 13
num = num.replace('\n','')
for i in range(len(num)-product_num):
    for j in range(product_num):
        sum *= int(num[i+j])
    if sum > max:
        max = sum
    sum = 1
print(max)