# доска - матрица
# ❌ ⚪

class Table:
    desk = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def draw(self, sym):
        row = int(input(f'Введите ряд {sym}: ')) - 1
        col = int(input(f'Введите столбик {sym}: ')) - 1
        while True:
            if self.desk[row][col] == '_':
                self.desk[row][col] = sym
                break
            else:
                print('Эта клеточка занята - выберете другое место')
                row = int(input(f'Введите ряд {sym}: ')) - 1
                col = int(input(f'Введите столбик {sym}: ')) - 1

    def print_table(self):
        for row in self.desk:
            for col in row:
                print(col, end=' ')
            print()

    def win_checker(self, sym):
        streak = 0
        for row in range(0, 3):
            if streak == 3:
                return True
            for col in range(0, 3):
                if self.desk[row][col] == sym:
                    streak += 1
                else:
                    streak = 0
                    break

        for col in range(0, 3):
            if streak == 3:
                return True
            for row in range(0, 3):
                if self.desk[row][col] == sym:
                    streak += 1
                else:
                    streak = 0
                    break

        for diagonal in range(0, 4):
            if streak == 3:
                return True
            if self.desk[diagonal][diagonal] == sym:
                streak += 1
            else:
                break

        if self.desk[0][2] == sym and self.desk[1][1] == sym and self.desk[2][0] == sym:
            return True
        return False


if __name__ == '__main__':
    table_1 = Table()
    while True:
        table_1.draw('❌')
        table_1.print_table()
        if table_1.win_checker('❌'):
            print('Победил первый игрок - ❌')
            break
        table_1.draw('⚪')
        table_1.print_table()
        if table_1.win_checker('⚪'):
            print('Победил второй игрок - ⚪')
            break
