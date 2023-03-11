import random

def jogar():

    print('**********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('**********************************')

    numeroSecreto = random.randrange(1, 101)
    totalTentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade você deseja?')
    print('(1) Fácil  (2) Médio  (3) Difícil')

    nivel = int(input('Digite a dificuldade: '))

    if nivel == 1:
        totalTentativas = 20
    elif nivel == 2:
        totalTentativas = 10
    else:
        totalTentativas = 5

    for tentativa in range(1, totalTentativas+1):
        print(f"tentativa {tentativa} de {totalTentativas}")

        chute = int(input('Chute um número entre 1 e 100: '))

        acertou = numeroSecreto == chute
        maior = chute > numeroSecreto

        if chute < 1 or chute > 100:
            print("Número invalido: Digite um número entre 1 e 100")
            continue

        print('Você digitou', chute)

        if acertou:
            print(f'Você acertou e fez {pontos} pontos')
            break
        else:
            if maior:
                print('Você errou, seu chute foi maior do que o número secreto')
            else:
                print('Você errou, seu chute foi menor do que o número secreto')
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

        tentativa += 1

    print('FIM DO JOGO')

if __name__ == '__main__':
    jogar()
