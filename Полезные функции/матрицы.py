# Транспонировать матрицу
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(*map(list, zip(*a)))
# [1, 4, 7] [2, 5, 8] [3, 6, 9]
# zip() преобразует в кортежи, поэтому и нужно преобразование в список
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(*zip(*a))
# (1, 4, 7) (2, 5, 8) (3, 6, 9)

n = int(input())  # размерность
matrix = [input().split() for _ in range(n)]
matrix2 = [[0] * n for _ in range(n)]
print()
n, m = [int(num) for num in input().split()]  # число строк, столбцов
matrix1 = [[int(num) for num in input().split()] for _ in range(n)]

# поменять местами строки и столбцы способ 1
for r in range(n):
    for c in range(n):
        matrix2[r][c] = matrix[c][r]

for row in matrix2:
    print(*row)
print()

matrix3 = matrix[::-1]  # обратный порядок строк cпособ 1
for row in matrix3:
    print(*row)
print()

matrix.reverse()  # обратный порядок строк cпособ 2
for row in matrix:
    print(*row)
print()

# поменять местами строки и столбцы способ 2
import numpy as np  # нужно еще установить библиотек NumPy будет
np.transpose(matrix)
for row in matrix:
    print(*row)

