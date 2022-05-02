# exer_58.py

# Descrição
#   
#   OOP - Propriedades publicas e não públicas
#   e Parametros de Métodos com tipos especificos.
#   
#   A partir daqui eu fui introduzido ao PEP8
#   sendo assim os códigos a partir desse, tentarão
#   ao máximo utilizar as boas práticas ali disponíveis

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

import random

class Dado:

    # Nesse construtor o  argumento deve ser um inteiro
    def __init__(self, _n_lados=6):
        self._nome = f'd{_n_lados}'
        self._n_lados = _n_lados
        self._v_atual = 0

    def rolar(self):
        self._v_atual = random.randint(1, self._n_lados)

    # Getters & Setters
    def get_nome(self):
        return self._nome

    def get_n_lados(self):
        return self._n_lados
    
    def get_v_atual(self):
        return self._v_atual
    
    def set_nome(self, nome: str):
        self._nome = nome

    def set_n_lados(self, n_lados: int):
        self._n_lados = n_lados


dado = Dado()
dado.rolar()

print(dado.get_nome(), dado.get_v_atual(), sep=': ')



