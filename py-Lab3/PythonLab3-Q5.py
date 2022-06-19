file = open('sample.txt','r')
linesList = []
for i in file:
    linesList.append(i.strip())
print(linesList)
file.close()