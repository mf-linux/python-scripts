# exer_40.py

# Descrição
#   Invocação de funções através de variáveis

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def mostrarMensagem(msg = 'Olá Mundo'):
    print(msg)

# Atribui o nome da função a variável
temp = mostrarMensagem

# Invoca a função adicionando () e os argumentos a variável
temp()                                  # Invoca a função sem argumento
temp('Oiiiii !!!!')                     # Invoca a funçào com argumento