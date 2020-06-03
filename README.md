# JogoDaVelhaPython

Aplicação onde simula um tabuleiro de um jogo da velha. Um computador é o servidor, responsável por esperar algum jogador se conectar, após existir alguma conexão, o jogo inicia, cada jogador tem sua vez de jogar, e a resposta é atualizada em ambos os computadores. Quando o jogo é finalizado, a conexão é encerrada e o jogador tinha que se reconectar para poder jogar novamente. Se houvesse um jogo já em andamento quando um cliente tentasse iniciar uma nova partida, a nova conexão é colocada em espera até o jogo ser finalizado.
