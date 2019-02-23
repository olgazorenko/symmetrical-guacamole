list = [1, 5, 7, 4, 6, 7, 9]
new_list = []

for x in list:
    if x % 2 == 0:
        new_list.append(x / 4)
    else:
        new_list.append(x*2)

print(new_list)