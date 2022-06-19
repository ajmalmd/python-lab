import random
file = open('sample.txt','r')
lines = file.read().splitlines()
print(random.choice(lines))
file.close()