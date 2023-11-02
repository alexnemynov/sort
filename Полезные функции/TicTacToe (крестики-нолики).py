# Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое поле из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки. Первый ход делает игрок, ставящий крестики:
#
# tictactoe = TicTacToe()
#
# tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
# tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)
# Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:
#
# tictactoe.mark(1, 1)         # Недоступная клетка
#
# tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
# tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
# tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
# tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
# tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)
# С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:
#
# символ X, если победил игрок, ставящий крестики
# символ O, если победил игрок, ставящий нолики
# строку Ничья, если произошла ничья
# значение None, если победитель еще не определен
# print(tictactoe.winner())    # X
# Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:
#
# tictactoe.mark(2, 1)         # Игра окончена
# С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено из символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe вызов tictactoe.show() должен вывести следующее:
#
# X|O|X
# -----
#  |O|X
# -----
# O| |X
class TicTacToe:
    def __init__(self):
        self._data = [[' '] * 3 for _ in range(3)]
        self._first = True
        self._game = True

    def mark(self, x: int, y: int):
        if self._game:
            if self._data[x - 1][y - 1] != ' ':
                print('Недоступная клетка')
            else:
                self._data[x - 1][y - 1] = 'X' if self._first else 'O'
                self._first = not self._first
                self.winner()
        else:
            print('Игра окончена')

    def winner(self):
        draw = 'Ничья'
        reference_matrix = [
            self._data[0],
            self._data[1],
            self._data[2],
            [col[0] for col in self._data],
            [col[1] for col in self._data],
            [col[2] for col in self._data],
            [self._data[0][0], self._data[1][1], self._data[2][2]],
            [self._data[0][2], self._data[1][1], self._data[2][0]]
        ]

        for item in reference_matrix:
            result = set(item)
            if ' ' in result:
                draw = None
            elif len(result) == 1:
                self._game = False
                return tuple(result)[0]

        if draw:
            self._game = False
            return draw

    def show(self):
        for i, row in enumerate(self._data):
            print(*row, sep='|')
            if i != len(self._data) - 1:
                print('-----')


# INPUT DATA:

# TEST_1:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()
print()

# TEST_2:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
print()

# TEST_3:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)
tictactoe.mark(2, 2)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print()

# TEST_4:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())

# OUTPUT DATA:

# TEST_1:
# Недоступная клетка
# X
# Игра окончена
# X|O|X
# -----
#  |O|X
# -----
# O| |X

# TEST_2:
# Недоступная клетка
# Игра окончена
# O
# X|O|X
# -----
#  |O|
# -----
#  |O|X

# TEST_3:
# X
# X|O|X
# -----
# O|X|O
# -----
# X|O|X
# Игра окончена

# TEST_4:
# None
# Ничья
# X|X|O
# -----
# O|O|X
# -----
# X|X|O
# Игра окончена
# Ничья