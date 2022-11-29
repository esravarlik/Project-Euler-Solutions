#Project Euler 36
result = 0
for i in range(1,1000000):
    if str(i) == str(i)[::-1]:
        binary = bin(int(i)).replace("0b","")
        if str(binary) == str(binary)[::-1]:
            result += i
print(result)
