# exer_63.py

# Descrição
#   Calculadora de IMC

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


class IMC:

    def __init__(self, valor: float):
        self._valor = valor
        self.validar(valor)

    def validar(self, valor: int) -> str:
        if(valor < 18.5):
            self._situacao = 'Magreza'
        elif(18.5 <= valor <= 24.9):
            self._situacao = 'Normal'
        elif(25 < valor <= 29.9):
            self._situacao = 'Sobrepeso'
        elif(30 < valor <= 39.9):
            self._situacao = 'Obesidade'
        else:
            self._situacao = 'Obesidade Grave'

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def situacao(self) -> str:
        return self.situacao

    @classmethod
    def calcular(cls, altura: float, peso: float):
        imc = peso / altura ** 2
        return cls(imc)


altura = float(input('Informe sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = IMC.calcular(altura, peso)

print('Seu IMC é:', imc._valor)
print('Isso significa que você tem', imc._situacao)




        