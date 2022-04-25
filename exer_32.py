# exer_32.py

# Descrição
#   Agregando listas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

remetentes, destinatarios, mensagens = [], [], []

while True:
    remetentes.append(input('Informe o seu nome: '))

    destinatarios.append(input('Para quem você deseja entregar essa mensagem: '))

    mensagens.append(input('Informe a mensagem que deseja exibir: '))

    controle = input('Deseja continuar s/n ? ')

    if controle == 'n': break
    
    print('')

print('')

correio_elegante = list(zip(remetentes, destinatarios, mensagens))

for i in correio_elegante:
    print(i[1], 'O', i[0], 'quer que você saiba que:', i[2])



