import random


def get_word():
    with open('words.txt', 'r') as f:
        palavras = f.read().splitlines()
    return random.choice(palavras)


def check(myword, you_word, guess1):
    status = '\t'
    matches = 0

    for letter in myword:
        if letter in you_word:
            status += ' '+letter
        else:
            status += ' *'
        if letter == guess1:
            matches += 1
    if matches > 1:
        print(f'** {matches}, {guess1}')
    elif matches == 1:
        print(f'** {guess1}')
    return status


def game():
    cont = 0
    palpitado = False
    sua_palavra = []
    turnos = len(my_word) + 1
    turnos1 = turnos

    print(f'Total de Turnos: {turnos}')

    while True:
        palpite1 = input('** Seu palpite: ')
        if palpite1 not in my_word:
            turnos -= 1

        print(f'** Turnos restantes: {turnos}')
        if palpite1 in sua_palavra:
            print('** \tVoçê já adivinhou!')
        if len(palpite1) == 1:
            sua_palavra.append(palpite1)
            result = check(my_word, sua_palavra, palpite1)
            if result == my_word:
                palpitado = True
                print(f'** \tVoçê GANHOU: {nome}')
                print(f'** {my_word}')
                break
            else:
                print(f'** {result}')
        else:
            print(f'** Inválido')

        if turnos == 0:
            print(f'** Você perdeu')
            print(f'** A palavra é: {my_word}')
            break


if __name__ == '__main__':
    nome = input('** Qual seu nome: ')
    my_word = get_word()
    print('\t', end='')
    for letra in my_word:
        print('*', end=' ')

    l = len(my_word)
    print(f'\n** A palavra tem {l} letras.')
    game()
