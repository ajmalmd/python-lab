import math

word = input('Enter word: ')

wordLen =len(word)-1
halfLen = math.floor(len(word)/2)

a = ''
b = ''

for i in range(0,halfLen):
    a = a+word[i]

if wordLen%2 == 0:
    for i in range(wordLen,halfLen,-1):
        b = b+word[i]

else:
    for i in range(wordLen,halfLen-1,-1):
        b = b+word[i]

a = a.lower()
b = b.lower()

if a == b:
    print(word + ' is a Palindrome')
else:
    print(word + ' is not a palindrome')