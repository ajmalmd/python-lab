try:
    num = int(input('Enter a number: '))
    if num%2 == 0:
        print('Even Number')
    else :
        print('Odd Number')
except:
    print('Wrong entered!!!\nNumber must be integer')
    quit()