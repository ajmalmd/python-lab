file1 = open('sample.txt','r')
file2 = open('abc.txt','r')
for x,y in zip(file1,file2):
    x = x.strip()
    y = y.strip()
    print(x+' '+y)
file1.close()
file2.close()