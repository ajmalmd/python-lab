from tokenize import Number


try:
    num = int(input('Enter a Number: '))
    x = []
    for a in range(1,num+1):
        if num%a == 0:
            x.append(a)
    print('Divisors of '+ str(num) + ' is: ' + str(x))
except:
    print('Number must be integer')
    quit()