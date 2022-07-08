import random


nome = input('** Qual seu nome: ')
print(f'** Jogador: {nome}')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("** Adivinhe os caracteres!")

palpites = ''
turnos = 12

while turnos > 0:
    falhas = 0

    for char in word:
        if char in palpites:
            print(f'** {char}')
        else:
            print(f'_')
            falhas += 1
    if falhas == 0:
        print('** Voçê Ganhou')
        print(f'** A palavra é {word}')
        break
    palpite = input('** Digite seu palpite:')
    palpites += palpite

    if palpite not in word:
        turnos -= 1
        print('** ERROU')
        print(f'Voçê tem {turnos} chances!')
        if turnos == 0:
            print(f'Voçê PERDEU')
