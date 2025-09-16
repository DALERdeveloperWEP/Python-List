li = [1, 2, 3, 7, 8, 9]
output_li = []
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] + li[j] == 10:output_li.append((li[i], li[j]))
    
print(output_li)