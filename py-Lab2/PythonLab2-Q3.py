try:
    string = str(input('Enter Something: '))
    print("Length of '{}' is '{}'".format(string,len(string)))
except:
    quit()