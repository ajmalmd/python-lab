file = open('sample.txt','r')
words = file.read().split()
wordlist = []
word = dict()
file.close()
for i in words:
    i = i.strip()
    i=i.lower()
    wordlist.append(i)
for i in wordlist:
    if i in word:
        word[i] = word[i] + 1
    else:
        word[i] = 1
for x,y in word.items():
    print('{} : {}'.format(x,y))