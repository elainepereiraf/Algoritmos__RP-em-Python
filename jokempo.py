#Crie uma função que simule o jogo do jokempô, isto é, dada a entrada de dois jogadores, retorne a indicação de qual deles venceu.

def Jokempo(jogador1, jogador2):
    if jogador1 == 'pedra':
        if jogador2 == 'tesoura':
            print('Jogador 1 ganhou')
        elif jogador2 == 'papel':
            print('Jogador 2 ganhou')
        else:
            print('Empate!')
    
    if jogador1 == 'tesoura':
        if jogador2 == 'papel':
            print('Jogador 1 ganhou')
        elif jogador2 == 'pedra':
            print('Jogador 2 ganhou')
        else:
            print('Empate!')
    
    if jogador1 == 'papel':
        if jogador2 == 'pedra':
            print('Jogador 1 ganhou')
        elif jogador2 == 'tesoura':
            print('Jogador 2 ganhou')
        else:
            print('Empate!')
