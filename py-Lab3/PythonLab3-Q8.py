file = open('sample.txt','r')
length = []
words = file.read().split()
for i in words:
    length.append(len(i))
maxLen = sorted(set(length),reverse=True)[0]
for i in words:
    if maxLen == len(i):
        print(i)
file.close()