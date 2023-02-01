
def display():
    print(f'\n {lst[6]}|{lst[7]}|{lst[8]}\n--|-|--\n {lst[3]}|{lst[4]}|{lst[5]}\n--|-|--\n {lst[0]}|{lst[1]}|{lst[2]}\n')

def check_victory():
    if lst[0] == X and lst[1] == X and lst[2] == X:
        return True
    elif lst[3] == X and lst[4] == X and lst[5] == X:
        return True
    elif lst[6] == X and lst[7] == X and lst[8] == X:
        return True
    elif lst[6] == X and lst[3] == X and lst[0] == X:
        return True
    elif lst[7] == X and lst[4] == X and lst[1] == X:
        return True
    elif lst[8] == X and lst[5] == X and lst[2] == X:
        return True
    elif lst[8] == X and lst[4] == X and lst[0] == X:
        return True
    elif lst[6] == X and lst[4] == X and lst[2] == X:
        return True
    elif lst[0] == O and lst[1] == O and lst[2] == O:
        return True
    elif lst[3] == O and lst[4] == O and lst[5] == O:
        return True
    elif lst[6] == O and lst[7] == O and lst[8] == O:
        return True
    elif lst[6] == O and lst[3] == O and lst[0] == O:
        return True
    elif lst[7] == O and lst[4] == O and lst[1] == O:
        return True
    elif lst[8] == O and lst[5] == O and lst[2] == O:
        return True
    elif lst[8] == O and lst[4] == O and lst[0] == O:
        return True
    elif lst[6] == O and lst[4] == O and lst[2] == O:
        return True
    else:
        return False

def symbol_choice1():
    x = input('(Jogador 1) Qual o seu símbolo? ')
    while len(x) != 1:
        print('Seu simbólo deve ser 1 caractere.')
        x = input('(Jogador 1) Qual o seu símbolo? ')
    return x

def symbol_choice2():
    o = input('(Jogador 2) Qual o seu símbolo? ')
    while len(o) != 1:
        print('Seu simbólo deve ser 1 caractere.')
        o = input('(Jogador 2) Qual o seu símbolo? ')
    return o

def change_symbol():
    change = input('Você quer mudar os simbólos (X e O)? [S/N] ')
    while change.lower() != 's' and change.lower() != 'n':
        print('S ou N??')
        change = input('Você quer mudar os simbólos? Padrão: X e O. [S/N] ')
    else:
        if change.lower() == 's':
            return True
        elif change.lower() == 'n':
            return False

def user_input():
    num_str = {'um':1,'dois':2,'tres':3,'quatro':4,'cinco':5,'seis':6,'sete':7,'oito':8,'nove':9}
    bool = False
    while not bool:
        pos = input('Qual posição vc quer (1-9)? ')
        if pos.lower() in num_str:
            bool = True
        elif not pos.isdigit():
                print('Tem que ser um número.')
        elif int(pos) not in range(1,10):
                print('O número tem que ser de 1 até 9.')
        else:
            bool = True
    if pos.lower() in num_str:
        return num_str[pos.lower()]
    else:

        return int(pos)

def start():
    global lst
    global picked
    global X
    global O
    global change
    global final

    final = False
    lst = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    picked = []
    X = 'X'
    O = 'O'
    change = change_symbol()

    if change:
        X = symbol_choice1()
        O = symbol_choice2()
    else:
        pass

def game():
    global final
    global picked
    global X
    global O
    global choice

    start()
    while not final:
        turn = True
        while turn:
            display()
            if check_victory():
                final = True
                print(f'Você ganhou! Parabéns Jogador 2!\nSeu simbólo foi o: {O}.\n')
                break
            elif len(picked) == 9:
                final = True
                print('Deu Velha!')
                break
            print(f'[{X}]Jogador 1:\n')
            choice = user_input()
            while choice in picked:
                display()
                print('Este espaço já foi ocupado!\n')
                choice = user_input()
            if choice not in picked:
                picked.append(choice)
                lst[choice-1] = X
                turn = False

        while not turn:
            display()
            if check_victory():
                final = True
                print(f'Você ganhou! Parabéns Jogador 1!\nSeu simbólo foi o: {X}.\n')
                break
            elif len(picked) == 9:
                final = True
                print('Deu Velha!\n')
                break
            print(f'[{O}]Jogador 2:\n')
            choice = user_input()
            while choice in picked:
                display()
                print('Este espaço já foi ocupado!\n')
                choice = user_input()
            if choice not in picked:
                picked.append(choice)
                lst[choice-1] = O
                turn = True

def retry():
    again = input('Você quer jogar de novo? [S/N]')
    while again.lower() != 's' and again.lower() != 'n':
        print('S ou N??')
        again = input('Você quer jogar de novo? [S/N]')
    else:
        if again.lower() == 's':
            return True
        elif again.lower() == 'n':
            return False

print('\nBem vindo ao whatsappGB tik tok toe!\n')
game()
while retry():
    game()
