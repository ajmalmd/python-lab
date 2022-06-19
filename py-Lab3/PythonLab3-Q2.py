file = open('sample.txt','r')
nLine = int(input('Enter no.of lines: '))
for i in range(nLine):
    print(file.readline())
file.close()