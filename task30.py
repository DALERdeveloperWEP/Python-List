ispalindrom = ['alla','test01','kiyik','non','test02']
palindrom_word = []

for i in ispalindrom:
    if i == i[::-1]:palindrom_word.append(i)

print(palindrom_word)