n = int(input('Num?: '))
x = 0
sum = n
for i in range(n):
    x = x+2
    if n-x  >= 0:        
        sum = sum + n - x
print('Sum is:',sum)