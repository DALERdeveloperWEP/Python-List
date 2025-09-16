word = ['salom', 'world', 'apple', 'macbook', 'uzb', 'non']
word_three = []
word_medium = []
word_long = []


for i in word:
    if len(i) <= 3:
        word_three.append(i)
    elif 4 <= len(i) <= 6:
        word_medium.append(i)
    elif len(i) > 6:
        word_long.append(i)

print(word_three, "<=3 harfli")
print(word_medium, "4-6 harfli")
print(word_long, ">6 harfli")
