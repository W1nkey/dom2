#import datetime

#now = datetime.datetime.now()

#print( now)

#print( now.year)
#print( now.month)
#print( now.day)


import datetime
# year = int(input("enter your year: "))
# month = int(input("enter your month: "))
# day = int(input("enter your day: "))
#
# birth_date = datetime.date(year, month, day)
# today = datetime.date.today()
#
# age = today.year - birth_date.year
#
# if (today.month, today.day) < (birth_date.month, birth_date.day):
#    age -= 1
#
# print("Вам", age, "лет.")


date1 = datetime.date(2024, 1, 1)
date2 = datetime.date(2025, 1, 1)

diff = date2 - date1

print(diff.days)