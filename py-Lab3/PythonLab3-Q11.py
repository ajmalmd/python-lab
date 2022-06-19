import os
file = 'abc.txt'
a = os.stat(file)
print(a.st_size)
file.close()