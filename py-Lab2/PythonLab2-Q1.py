import random
letters = ['a','e','i','o','u']
listA = []
for x in range(1,2000):
    random.shuffle(letters)
    word = ''.join(letters)
    if word not in listA:
        listA.append(word)
try:
    num = int(input('Enter no of words you want: '))
    if num>120:
        print('Maximum words is 120! Try number between 1 and 120')
    else:
        for i in range(0,num):
            print(listA[i])

except:
    print('Enter number between 1 and 120!')
    quit()