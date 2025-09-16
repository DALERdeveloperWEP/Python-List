word = ["kitob", "dastur", "AI", "hello", "python"]
# ["dastur", "python"]

word_max_len = []

for i in word:
    if len(i) > 5:
        word_max_len.append(i)

print(word_max_len)
