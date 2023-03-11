import forca
import adivinhacao

def escolheJogo():
    print('**********************************')
    print('********Escolha o seu jogo********')
    print('**********************************')

    print('(1) Forca  (2) Adivinhação')

    jogo = int(input('Qual jogo?'))

    if jogo == 1:
        print('joga forca')
        forca.jogar()
    elif jogo == 2:
        print('jogo adv')
        adivinhacao.jogar()

if __name__ == '__main__':
    escolheJogo()
