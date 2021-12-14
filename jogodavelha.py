x = '         '
l1 = [x[0], x[1], x[2]]
l2 = [x[3], x[4], x[5]]
l3 = [x[6], x[7], x[8]]
matriz = [l1, l2, l3]


def tela():
    print(f"{9 * '-'}\n| {matriz[0][0]} {matriz[0][1]} {matriz[0][2]} | \
\n| {matriz[1][0]} {matriz[1][1]} {matriz[1][2]} |\n\
| {matriz[2][0]} {matriz[2][1]} {matriz[2][2]} |\n{9 * '-'}")


# Part of the program that analyze the state of the game
# Test 1 - Numbers of O-X in the game
num_x = x.count('X')  # Número de ocorências de X
num_o = x.count('O')  # Número de ocorrências de
num__ = x.count(' ')  # Número de espaços vagos


def attnum():
    global num_x
    global num_o
    global num__
    num_x = matriz[0][:].count('X') + matriz[1][:].count('X') + matriz[2][:].count('X')  # Número de ocorências de X
    num_o = matriz[1][:].count('O') + matriz[2][:].count('O') + matriz[0][:].count('O')  # Número de ocorrências de
    num__ = matriz[0][:].count(' ') + matriz[1][:].count(' ') + matriz[2][:].count(' ')  # Número de espaços vagos


def possibleimpossible(xe):
    if num_x + 1 < num_o or num_o + 1 < num_x:
        xe += 1
        return xe
    else:
        return xe
# 0 -- possible
# 1 -- impossible


def winorlose(xa):
    xw = 0
    ow = 0
    # Linhas
    for j in range(3):
        if matriz[j][0] == matriz[j][1] == matriz[j][2] == 'X':
            xw += 1
    for j in range(3):
        if matriz[j][0] == matriz[j][1] == matriz[j][2] == 'O':
            ow += 1
    # Colunas
    for j in range(3):
        if matriz[0][j] == matriz[1][j] == matriz[2][j] == 'X':
            xw += 1
    for j in range(3):
        if matriz[0][j] == matriz[1][j] == matriz[2][j] == 'O':
            ow += 1
    # Diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == 'X':
        xw += 1
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] == 'O':
        ow += 1
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == 'X':
        xw += 1
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == 'O':
        ow += 1
    if xw + ow > 1:
        xa += 1
        print('Impossible')
        return xa
    elif ow == 1:
        xa += 1
        print('O wins')
        return xa
    elif xw == 1:
        xa += 1
        print('X wins')
        return xa
    elif num__ == 0:
        xa += 1
        print('Draw')
        return xa
    else:
        return xa


def finished(xi):
    if num__ > 0:
        return xi
    elif num__ == 0:
        xi += 1
        return xi
    pass
# 0 -- not finished
# 1 -- finished


def stategame():
    if possibleimpossible(0) == 0:
        if finished(0) == 0:
            b = winorlose(0)
            return b
        elif finished(0) == 1:
            b = winorlose(0)
            return b
    elif possibleimpossible(0) == 1:
        print("Impossible")


#
# Entrada de dados
def entercoordinate(abacate):
    ativo = 10
    while ativo == 10:
        lin, c = input("Enter the coordinates: ").split(" ")
        cond1 = lin.isdigit()
        cond2 = c.isdigit()
        if cond1 and cond2:
            lin = int(lin)
            c = int(c)
            if 0 < lin < 4 and 0 < c < 4:
                if matriz[lin - 1][c - 1] == ' ':
                    matriz[lin - 1][c - 1] = abacate
                    return abacate
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


quadro = 1
tela()
stategame()

while True:
    if quadro == 1:
        entercoordinate('X')
        attnum()
        tela()
        if stategame() == 1:
            break
        stategame()
        quadro = 2
        continue
    if quadro == 2:
        entercoordinate('O')
        attnum()
        tela()
        if stategame() == 1:
            break
        stategame()
        quadro = 1
