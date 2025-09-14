li = [[1, 2, 3], ["a", "b", "c"]]

count = 0

li_1 = ""
li_2 = ""

for i in li:
    for index in i:
        count += 1
        if count <= len(li[0]):
            li_1 += str(index) + " "
        if count > len(li[0]):
            li_2 += index + " "

print(li_1)
print(li_2)
