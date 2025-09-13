num = [0,1,2,3,4,5,6,7,8,9,10]
length = len(num) - 1

start = int(input("start num: "))
end = int(input("end num: "))

if start > length or start <= (length - (length + length)):
    print(f'0 dan { length } gacha son kirita olasiz')
elif end > length or end <= (length - (length + length)):
    print(f'0 dan { length } gacha son kirita olasiz')
elif start > end:
    print('start raqam kichik bo\'lishi kerak')
else:
    print(num[start:end+1])