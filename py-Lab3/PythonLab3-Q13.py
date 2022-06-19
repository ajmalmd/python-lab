file1 = open('sample.txt','r')
file2 = open('abc.txt','a')
for i in file1:
    file2.write(i)
file1.close()
file2.close()
file = open('abc.txt','r')
print(file.read())
file.close()