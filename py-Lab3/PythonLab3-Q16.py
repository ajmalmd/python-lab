file = open('sample.txt','r')
lines = file.readlines()
print([i.strip() for i in lines])
file.close()