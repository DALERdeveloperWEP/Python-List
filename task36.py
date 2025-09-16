word = ['salom', 'world', 'apple', 'macbook', 'uzb', 'non', 'kitop', 'notbook']
result = []
max_word = word[0]

for i in range(1,len(word)):
    if len(word[i]) > len(max_word):max_word = word[i]

result.append(max_word)

print(result)