Duplicate_list = [3, 5, 3, 3, 3, 2, 5, 5, 1]
max_repeated = Duplicate_list.count(3)

for idx in Duplicate_list:
    if Duplicate_list.count(idx) > max_repeated:max_repeated = idx
    

print(max_repeated)