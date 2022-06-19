color_dict = {
    'red':'#FF0000',
    'green':'#008000',
    'black':'#000000',
    'white':'#FFFFFF'}
sorted_dict = {}
sorted_color = sorted(color_dict)
for i in sorted_color:
    for x,y in color_dict.items():
        if i == x:
            sorted_dict[i] = y

print(sorted_dict)