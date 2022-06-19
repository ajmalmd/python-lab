import string , random

up_alph = string.ascii_uppercase
lo_alph = string.ascii_lowercase
digits = string.digits
symbols = "!@#$%^&*"
password = []

for i in range(1):
    password.append(random.choice(symbols))
for i in range(2):
    password.append(random.choice(digits))
for i in range(2):
    password.append(random.choice(up_alph))
for i in range(3):
    password.append(random.choice(lo_alph))
random.shuffle(password)
print(''.join(password))