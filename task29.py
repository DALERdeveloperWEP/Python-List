list_unique = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7] 
# output: [4, 5, 6, 7]
new_li = []

for idx in list_unique:
    if list_unique.count(idx) == 1:new_li.append(idx)

print(new_li)