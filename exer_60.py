# exer_60.py

# Descrição
#    OOP - Uso de @property, @static e @classmethod e sobrescrita de métodos
#       

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

import random

class Dados:
    def __init__(self, n_lados=6):
        self._nome = f'd{n_lados}'
        self._n_lados = n_lados
        self._v_atual = 0

    # Simula a rolagem do dado e armazena o valor no objeto
    def rolar(self):
        self._v_atual = random.randint(1, self._n_lados)

    # Retorna um objeto dado com uma rolagem já armazenada
    @classmethod
    def rolar_(cls, n_lados: int):
        d_tmp = cls(n_lados)
        d_tmp.rolar()
        return d_tmp
    
    # Simula a rolagem do dado e retorna o valor sem armazenar nada
    @staticmethod
    def rolar__(n_lados: int) -> int:
        return random.randint(1, n_lados)
    
    # Rescreve o método __str__ para mudar a impressão desse objeto
    def __str__(self) -> str:
        return f'{self._nome}: {self._v_atual}'

    # Sobrescreve o método add
    def __add__(self, outro_dado) -> tuple:    
        if type(self) is not type(outro_dado):
            raise ValueError('Os dois valores precisam ser do tipo Dado')

        self.rolar()
        outro_dado.rolar()

        return (self._v_atual, outro_dado._v_atual)
        
    # Sobrescreve o mul
    def __mul__(self, n_vezes: int) -> tuple:
        if n_vezes <= 0:
            raise ValueError('É impossível rolar um dado esse número de vezes')
        valores = []

        for r in range(1, n_vezes + 1):
            self.rolar()
            valores.append(self._v_atual)
        
        return tuple(valores)

    # Getters
    @property
    def nome(self):
        return self._nome

    @property
    def n_lados(self):
        return self._n_lados
    
    @property
    def v_atual(self):
        return self._v_atual

    # Setters
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @n_lados.setter
    def n_lados(self, n_lados):
        self._n_lados = n_lados


