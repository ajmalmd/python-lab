file = open('sample.txt','r')
lines = 0
for i in file:
    lines = lines+1
file.close()
print('No.of lines in this file is: ',lines)