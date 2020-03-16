#!/usr/bin/python3
#encode: utf-8

	#Implementação do Trabalho de redes Jogo da Velha
    #Alunos: Iagho Cristian
    #        Joseane Mansur
	# Este arquivo controla o servidor que espera a requisição.


#importa todas as funções do arquivo do jogo da velha
#incluindo a biblioteca de socket
from jogo import * 

## Informações do servidor: Host e porta para conexao
Host = ''
Port = 4241

## Criação do socket TCP e início de escuta
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_tcp.bind((Host, Port))
socket_tcp.listen(5)

sair = False

tabuleiro = [] #tabuleiro

print ('Bem vindo ao Jogo da Velha!!')
# repetição para receber conexoes
while not sair:
	print ("\n\n\tEsperando novo participante solicitar conexão...")
	conn, cliente_host = socket_tcp.accept()
	
	
	tabuleiro = TabuleiroVazio()
	imprimirTabuleiro(tabuleiro)
	
	print ('\n\n\tParticipante ', cliente_host, ' conectou.')

	# repetição para receber mensagens...
	while True:
		
		print("\n\t\t...Aguarde a jogada do", cliente_host, "...")    
		data = conn.recv(1024) 
		resposta = data.decode()
		
		if not data or resposta == "sair":
			print ('Participante ', cliente_host, ' desconectou.')
			break
		
		# aplica a resposta no tabuleiro
		resposta = traduzJogada(resposta)
		tabuleiro[resposta[0]][resposta[1]] = "X"
		imprimirTabuleiro(tabuleiro)

		f = fimDeJogo(tabuleiro)
		if f > 0:
			if f == 1: 
				print("\n\t~~~~Você Perdeu! :(")
			else:
				print("\n~~~~~Jogo Empatado!")
			
			print ("\n\t~~Jogo Terminado!")
			break
			
		print("Você é o O")

		# lendo a jogada para enviar
		jogada = input("\n\tJogada =>  ")


		while validaJogada(tabuleiro, jogada) == False: 
			jogada = input("\tDigite uma jogada válida =>  ")

		# Envia a resposta
		conn.send(jogada.encode())
		
		if jogada == "sair":
			print ('Aplicação foi finalizada\n')
			sair = True
			break
		
		jogada = traduzJogada(jogada)
		tabuleiro[jogada[0]][jogada[1]] = "O"
		imprimirTabuleiro(tabuleiro)

		f = fimDeJogo(tabuleiro)
		if f > 0:
			if f == 1: 
				print("\n\t~~~~Você Ganhou! Parabéns!")
			else:
				print("\n~~~~~Jogo Empatado!")
			
			print ("\n\t~~Jogo Terminado! :D")
			break

conn.close()
