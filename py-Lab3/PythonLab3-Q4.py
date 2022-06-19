file = open('sample.txt','r')
lines = 0
for i in file:
    lines = lines+1
file.close()
nLine = int(input('Enter no.of lines: '))
lastnline = lines-nLine
if nLine >= lines :
    print('Enter no.of lines under ',lines)
else:
    file = open('sample.txt','r')
    for i in range(lines):
        if i >= lastnline:
            print(file.readline())
        else:
            file.readline()
    file.close()