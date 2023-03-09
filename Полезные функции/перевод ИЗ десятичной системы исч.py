num10 = int(input())
p = int(input())
num = ''
while True:
    num = str(num10 % p) + num if (num10 %
              p) < 9 else chr((num10 % p) + 55) + num
    num10 //= p
    if num10 < p:
        num = str(num10) + num
        break
print(num)