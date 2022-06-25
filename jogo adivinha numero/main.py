import random
import math

# obten as entradas do usuário
menor = int(input('** Digite o valor MENOR do intervalo: '))
maior = int(input('** Digite o valor MAIOR intervalo: '))

# gera um número aleatório
x = random.randint(menor, maior)

# calcula as chances com base nos intervalos
chances = round(math.log(maior - menor + 1, 2))
print(f'Você tem {chances}!')

cont = 0
while cont < chances:  # loop do jogo
    cont += 1
    entrada_usuario = int(input('** Numero:\n** '))
    if entrada_usuario == x:
        print('** Parabéns, GANHOU **')
        break
    elif x > entrada_usuario:
        print('** Seu palpite foi muito baixo')
    elif x < entrada_usuario:
        print('** Seu palpite foi muito alto')
if cont > chances:
    print('** O número é: {x}')
    print('** Melhor na proxima1')
