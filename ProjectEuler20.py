#Project Euler 20
number_list = 1
i = 100
while i > 1:
    number_list *= i
    i -= 1
number_list = list(str(number_list))
factorial_digit_sum = 0
for i in number_list:
    factorial_digit_sum += int(i)
print(factorial_digit_sum)