#Project Euler 19

from datetime import date 
sundays = 0 
mnth = 12 

for year in range(1901,2001): 
    for month in range(1,mnth+1): 
        if date(year,month,1).weekday()==6: 
            sundays += 1 
            
print(sundays)
