#ProjectEuler24 

from itertools import permutations 
x = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])) 
print("".join(x[1000000-1]))
