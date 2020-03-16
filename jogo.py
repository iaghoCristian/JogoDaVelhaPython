#!/usr/bin/python3
#encode: utf-8

    #Implementação do Trabalho de redes Jogo da Velha
        #Alunos: Iagho Cristian
        #        Joseane Mansur
        #Esse arquivo controla o tabuleiro

import socket
from os import system

# Cria um tabuleiro vazio
def TabuleiroVazio():
    novoTabuleiro = []
    for i in range(3):
        novoTabuleiro.append([' ',' ',' ']) 
    return novoTabuleiro

# Imprime o tabuleiro
def imprimirTabuleiro(tabuleiro) :
    system("clear") # Limpa a tela (somente linux)
    
    # Imprime instruções
    print("( )~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("( )~~~~~~~~~~~~~~~~~~~~~~~~~ JOGO DA VELHA ~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("( )~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("( )                          ~INSTRUÇÕES~                           |")
    print("( )                                                                 |")
    print("( ) Quando for sua vez de jogar, digite uma jogada válida           |")
    print("( )                                                                 |")
    print("( ) O formato é LC, onde:                                          |")
    print("( ) L é a linha, e C é a coluna                                     |")
    print("( ) Exemplo de jogada: 0A (linha 0, coluna A)                      |")
    print("( )                                                                 |")
    print("( ) Você pode sair do jogo quando for sua vez de jogar, utilize o   |")
    print("( )    comando 'sair' para isso!                                    |")
    print("( )~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("( )~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("                           A       B       C"    )
    print("                       _________________________")
    print("                      0|   %c   |   %c   |   %c   |" % ( tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]) )
    print("                       -------------------------")
    print("                      1|   %c   |   %c   |   %c   |" % ( tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]) )
    print("                       -------------------------")
    print("                      2|   %c   |   %c   |   %c   |" % ( tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]) )
    print("                       ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
        

#verifica se foi empate
def empate(tabuleiro):
    
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True

# Verifica se o jogo terminou (vitoria/derrota ou empate)
# retorna:
#   0 - continua o jogo
#   1 - houve vitória
#   2 - empate
def fimDeJogo(tabuleiro):
    
    
    # verifica vitoria pelas linhas
    for linha in tabuleiro:
        if linha == ['X','X','X'] or linha == ['O','O','O']:
            return 1
    
    
    # verifica vitoria pelas colunas
    for i in range(3) :
        
        coluna = []
        
        for j in range(3):
            coluna.append(tabuleiro[j][i])
        
        if coluna == ['X','X','X'] or coluna == ['O','O','O']:
            return 1
        

    # verifica diagonal principal
    diagonal = []
    for i in range(3):
        diagonal.append(tabuleiro[i][i])
    if diagonal == ['X','X','X'] or diagonal == ['O','O','O']:
        return 1
    
    # verifica diagonal secundaria
    diagonal = []
    for i in range(3):
        diagonal.append(tabuleiro[i][2-i])
    if diagonal == ['X','X','X'] or diagonal == ['O','O','O']:
        return 1
    
    
    # Ninguém venceu, verifica empate
    if empate(tabuleiro):
        return 2
    
    # Não houve vitória/derrota ou empate, continua
    return 0

# traduz uma jogada
# deve ser chamado apos verificação de validade
def traduzJogada(jogada):
    c = 0
    if int(jogada[1] == 'B'):
        c = 1
    elif int(jogada[1] == 'C'):
        c = 2
    return (int(jogada[0]),c)


# Verifica se uma jogada é válida    
def validaJogada(tabuleiro, jogada) :
    
    # Comando de saída, é válido!
    if jogada == "sair" : 
        return True
    
    # jogada deve ser do tipo 'L,C'
    if len(jogada) != 2 :
        print("\tO formato correto é LC!") 
        return False
    
    # os números possuem intervalo definido entre 0 e 2 e A e C
    if (int(jogada[0]) < 0 or int(jogada[0]) > 2) or (jogada[1] not in ['A','B','C']): 
        print("\tAs coordenadas devem estar no intervalo 0 a 2 e A a C!")
        return False
    
    # Verifica se a jogada foi feita anteriormente
    jogada = traduzJogada(jogada)
    if tabuleiro[jogada[0]][jogada[1]] != ' ':
        print("\tjogada já foi feita!") 
        return False
    
    # É válida
    return True


