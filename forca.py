from random import choice
import emoji
from playsound import playsound
            
def forca():
        
    music_less_point = '/home/farley/Documentos/jogo_da_forca/songs/lees_point.mp3'
    music_looser = '/home/farley/Documentos/jogo_da_forca/songs/loose.mp3'
    music_winner = '/home/farley/Documentos/jogo_da_forca/songs/winner.mp3'
    #lista
    frutas = ['melao', 'banana', 'abacaxi', 'uva', 'laranja', 'melancia', 'abacate', 'goiaba']
    print('===================================================================================')
    print(f'Tente adivinhar qual foi a fruta escolhida pelo sistema na lista a seguir em 3 tentativas:{frutas}')
    print('===================================================================================')
    escolhida = choice(frutas)
    erros = 0
    palpite = input('Digite o nome de uma fruta da lista para descobrir se acertou:')
    while palpite != escolhida and erros < 3:
        erros = erros + 1
        print(f'Total de erros: {erros}')
        playsound(music_less_point)
        if erros == 3:
            print('Agora não pode mais errar !')
        palpite = input('Tente novamente:')
        if palpite == escolhida:
            print('Parabéns, você acertou e venceu!', emoji.emojize(':party_popper:'))
            playsound(music_winner)
        elif erros == 3:
            print(f'Você errou {erros} vezes e foi para a forca.',emoji.emojize(':anxious_face_with_sweat:'))
            playsound(music_looser)
            break
forca() 
