num = list(input())
p = int(input())
num10 = 0

for i in range(len(num)):
    if num[i] not in "0123456789":
        num[i] = ord(num[i]) - 55
    else:
        num[i] = int(num[i])
    num10 += num[i] * p ** (len(num) - 1 - i)

print(num10)


# num = int(input))
# p = int(input())
# num10 = 0
# for i in range(len(num)):
#    num10 += int(num[i]) * p ** (len(num) - 1 - i)
# print(num10)

