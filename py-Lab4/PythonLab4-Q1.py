from datetime import datetime
print('Current date & time:',datetime.now())
print('Current year:',datetime.now().year)
print('Month of year:',datetime.now().month)
print('Week number of the year:',datetime.now().strftime('%W'))
print('Weekday of the week:',datetime.now().strftime('%A'))
print('Day of year:',datetime.now().strftime('%j'))
print("Day of the month :",datetime.now().strftime('%d'))
print("Day of week: ",datetime.now().strftime('%w'))