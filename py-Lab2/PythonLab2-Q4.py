try:
    string = input('Enter something: ')
    frequency = {}
    for i in string:
        count = string.count(i)
        frequency[i] = count
    for i,j in frequency.items():
        if j > 1:
            print('{}:{}'.format(i,j))

except:
    quit()