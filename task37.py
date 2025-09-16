# list1 = [1, 2, 3] 
# list2 = [4, 5, 6]

# print(f"oldingi list1: {list1}")
# print(f"oldingi list1: {list2}\n")

# list1_copy = list1.copy()
# list2_copy = list2.copy()

# list1.clear()
# list1 = list2_copy

# list2.clear()
# list2 = list1_copy

# print(f"keyingi list1: {list1}")
# print(f"keyingi list1: {list2}")


list1 = [1, 2, 3] 
list2 = [4, 5, 6]



for i in range(len(list1)):

    # temp1 = list1[i]
    # temp2 = list2[i]

    # list1[i] = temp2
    # list2[i] = temp1


    list1[i], list2[i] = list2[i], list1[i] # qisqa yozish usuli

print(f"keyingi list1: {list1}")
print(f"keyingi list1: {list2}")
