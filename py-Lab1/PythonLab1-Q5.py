A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#converting list to set
setA = set(A)
setB = set(B)

#take common elements from both sets and convert back to list
resList =list(setA & setB)

print(resList)