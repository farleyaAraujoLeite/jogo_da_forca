from random import choice
import emoji
from playsound import playsound


def forca():
    music1 = '/home/farley/Documentos/jogo_da_forca/lees_point.mp3'
    music2 = '/home/farley/Documentos/jogo_da_forca/loose.mp3'
    music3 = '/home/farley/Documentos/jogo_da_forca/winner.mp3'

    frutas = ['melao', 'banana', 'abacaxi', 'uva', 'laranja', 'melancia', 'abacate', 'goiaba']
    print('===================================================================================')
    print(f'Tente adivinhar qual foi a fruta escolhida pelo sistema na lista a seguir:{frutas}')
    print('===================================================================================')
    escolhida = choice(frutas)
    erros = 0
    palpite = input('Digite o nome de uma fruta da lista para descobrir se acertou:')
    while palpite != escolhida and erros < 3:
        erros = erros + 1
        print(f'Total de erros: {erros}')
        playsound(music1)
        if erros == 3:
            print('Você não pode mais errar !')
        palpite = input('Tente novamente:')
        if palpite == escolhida:
            print('Parabéns, você acertou!', emoji.emojize(':party_popper:'))
            playsound(music3)
        elif erros == 3:
            print(f'Você errou {erros} vezes e foi para a forca.',emoji.emojize(':anxious_face_with_sweat:'))
            playsound(music2)
            break

forca()    
