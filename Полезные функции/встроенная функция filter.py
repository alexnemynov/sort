numbers = list(filter(int, ['1', '2', '3', '4', '5']))
print(numbers)
numbers2 = list(filter(lambda x: type(x) == int, ['1', '2', '3', '4', '5']))
print(numbers2)

try:
    total = sum(numbers)
    print(total)
except:
    print('Произошла ошибка')
else:
    print('Ошибок не произошло')
finally:
    print('Завершение программы')

try:
    total = sum(numbers2)
    print(total)
except:
    print('Произошла ошибка')
else:
    print('Ошибок не произошло')
finally:
    print('Завершение программы')