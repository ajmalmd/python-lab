from datetime import date

today = date.today()
curr_year = today.year
name = input('What is your name: ')
age = int(input('How old are you:'))
age100 = curr_year + 100 - age

print('Congratulations {}! You will turn 100 years old at {}'.format(name,age100))