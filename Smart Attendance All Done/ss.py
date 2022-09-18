from datetime import date  
import holidays  
# Select country  
# printing all the holiday of USA year 2020  
for p in holidays.IND(years = 2021).items():  
    print(p[0])  
