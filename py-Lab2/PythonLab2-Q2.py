try:
    string = input('Enter something: ')
    frequency = {}
    for i in string:
        count = string.count(i)
        frequency[i] = count
    print(frequency)

except:
    quit()