file = open('sample.txt','r')
lines = ''
for i in file:
    lines = lines+''.join(i.strip())+', '
print(lines)
file.close()