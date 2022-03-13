# TicTacToe - The Game

# current results of the game
result = [["-" for i in range(3)] for j in range(3)]

crosses = "Крестики"
noughts = "Нолики"
WIN = "WIN"
DRAW = "DRAW"
is_crosses = True

# output
def print_field():
    field = [
        [" ", "1", "2", "3"],
        ["1"],
        ["2"],
        ["3"]
        ]
    field[1].extend(result[0])
    field[2].extend(result[1])
    field[3].extend(result[2])

    for row in field:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
    print("")

def set_result(x, y):
    for i in range(len(result)):
        if i==y:
            result[i][x] = "x" if is_crosses else "o"

def game_end():
    draw_rows = True
    draw_cols = True
    draw_diags = True

    # check result for any filled ROWS
    for row in result:
        if all(elem == row[0] and elem != "-" for elem in row):
            return WIN
        draw_rows = draw_rows and (row.count("x")>0 and row.count("o")>0)

    # check result for any filled COLUMNS by matrix transposing
    t_result = zip(*result)
    for row in t_result:
        if all(elem == row[0] and elem != "-" for elem in row):
            return WIN
        draw_cols = draw_cols and (row.count("x")>0 and row.count("o")>0)

    # check result for any filled DIAGONALS
    d_result = [[result[0][0], result[1][1], result[2][2]],
        [result[0][2], result[1][1], result[2][0]]]
    for row in d_result:
        if all(elem == row[0] and elem != "-" for elem in row):
            return WIN
        draw_diags = draw_diags and (row.count("x")>0 and row.count("o")>0)

    # check for a draw
    if all([draw_rows, draw_cols, draw_diags]):
        return DRAW

def is_error(x, y):
    if x is None and y is None:
        return False

    try:
        x = int(x) - 1
        y = int(y) - 1
    except:
        print("Упс, неправильный формат. Надо ввести номер столбца, а потом номер строки")
        print("Попробуйте еще раз")
        return False

    if not(x in range(3) and y in range(3)):
        print("Ой, таких номеров колонок или рядов на поле нет.")
        print("Попробуйте еще раз:")
        return False

    if result[y][x] != "-":
        print("Не-е-е, эта ячейка уже заполнена")
        print("Попробуйте еще раз:")
        return False

    return True

print("\nДа начнется битва!\n")
print_field()
print("Вводите номер колонки и строчки по очереди\n")

for i in range(9):
    x_coord = None
    y_coord = None
    is_crosses = i%2 == 0
    print(f"{crosses if is_crosses else noughts}, ваш ход")
    while not is_error(x_coord, y_coord):
        x_coord = input("Номер колонки: ")
        y_coord = input("Номер строки: ")
        print("")
    set_result(int(x_coord)-1, int(y_coord)-1)
    print_field()
    if game_end() == WIN:
        print(f"Победили {crosses if is_crosses else noughts}! Поздравляем!\n")
        break
    elif game_end() == DRAW:
        print("Ничья!\n")
        break
