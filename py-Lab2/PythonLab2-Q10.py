my_tuple = ('h','e','l','l','o',' ','w','o','r','l','d')
rev_tuple = []
for i in range(-1,-len(my_tuple)-1,-1):
    rev_tuple.append(my_tuple[i])
rev_tuple = tuple(rev_tuple)
print(rev_tuple)