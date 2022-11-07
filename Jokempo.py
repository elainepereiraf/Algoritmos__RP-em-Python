#Criar uma função que simule o jogo do jokempô, isto é, dada a entrada de dois jogadores, retornar a indicação de qual deles venceu.

def Jokempo(JogadorA, JogadorB):
    if JogadorA == 'Pedra':
        if JogadorB == 'Tesoura':
            print('Jogador A ganhou!')
        elif JogadorB == 'Papel':
            print('Jogador B ganhou!')
        else:
            print('Empate!')
    
    if JogadorA == 'Tesoura':
        if JogadorB == 'Papel':
            print('Jogador A ganhou!')
        elif JogadorB == 'Pedra':
            print('Jogador B ganhou!')
        else:
            print('Empate!')
    
    if JogadorA == 'Papel':
        if JogadorB == 'Pedra':
            print('Jogador A ganhou!')
        elif JogadorB == 'Tesoura':
            print('Jogador B ganhou!')
        else:
            print('Empate!')
