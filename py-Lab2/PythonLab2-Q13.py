from itertools import combinations
listA = [10, 20, 30, 40]
for i in range(1,len(listA)+1):
    for x in combinations(listA,i):
        print(list(x))
