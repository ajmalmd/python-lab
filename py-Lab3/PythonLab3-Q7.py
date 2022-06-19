file = open('sample.txt','r')
linesArray = []
for i in file:
    linesArray.append(i.strip())
print(linesArray)
file.close()