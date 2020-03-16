#!/usr/bin/python3
#encode: utf-8

    #Implementação do Trabalho de redes Jogo da Velha
    #Alunos: Iagho Cristian
    #        Joseane Mansur
    # Este arquivo controla o cliente que envia a requisição.

from jogo import * #importa todas as funções do arquivo do jogo da velha

## Endereço e porta do servidor ao qual se conectar
Host = '127.0.0.1'
Port = 4241

## Criacao do socket para comunicacao
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.connect((Host, Port))

tabuleiro = TabuleiroVazio() #tabuleiro

## loop para enviar mensagens
while True:

	imprimirTabuleiro(tabuleiro)
	print("Você é o X")
	
	
	jogada = input("\n\tJogada =>  ")

	
	while validaJogada(tabuleiro,jogada) == False : 
		jogada = input("Digite uma jogada válida =>  ")
	
	socket_tcp.send(jogada.encode())

	if jogada == "sair":
		print ('Aplicação foi encerrada pois o cliente saiu\n')
		break
	
	jogada = traduzJogada(jogada)
	tabuleiro[jogada[0]][jogada[1]] = "X"
	imprimirTabuleiro(tabuleiro)

	f = fimDeJogo(tabuleiro)
	if f > 0:
		if f == 1: 
			print("\n\t~~~~Você Ganhou! Parabéns!")
		else:
			print("\n~~~~~Jogo Empatado!")
		
		print ("\n\t~~Jogo Terminado! :D")
		break

	print("\n\t\t...Aguarde a jogada do servidor...")
	resposta = socket_tcp.recv(1024)
	resposta = resposta.decode()

	if not resposta or resposta == "sair":
		print ('\n\Servidor ', Host, ' desconectou-se.\n')
		break

	# aplica a resposta no tabuleiro
	resposta = traduzJogada(resposta)
	tabuleiro[resposta[0]][resposta[1]] = "O"
	imprimirTabuleiro(tabuleiro)

	f = fimDeJogo(tabuleiro)
	if f > 0:
		if f == 1: 
			print("\n\t~~~~Você Perdeu! :(")
		else:
			print("\n~~~~~Jogo Empatado!")
		
		print ("\n\t~~Jogo Terminado!")
		break


socket_tcp.close()
