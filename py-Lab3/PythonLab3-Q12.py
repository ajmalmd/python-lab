fruits = ['Apple', 'Mango', 'Grape', 'Orange']
file = open('abc.txt','w')
for i in fruits:
    file.write(i + "\n")
file.close()
file = open('abc.txt','r')
print(file.read())
file.close()