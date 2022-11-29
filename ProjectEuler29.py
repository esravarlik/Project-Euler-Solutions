#ProjectEuler29

list1 = []
for i in range(2,101):
    for j in range(2,101):
         x = pow(i,j)
         list1.append(x)
list1.sort()

print(len(set(list1)))
