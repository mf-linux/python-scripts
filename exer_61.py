# exer_61.py

# Descrição
#    OOP - Herança e sobrescrita de métodos
#       

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

class Pessoa:
    
    def __init__(self, nome: str, data_nasc: str, cpf: str):
        self._nome = nome
        self._data_nasc = data_nasc
        self._cpf = cpf
    
    # Sobrescreve o método string
    def __str__(self) -> str:
        return 'Nome: {}\nData de Nascimento: {}\nCPF: {}'.format(self._nome, self._data_nasc, self._cpf)

    
    # Getters & Setters
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def data_nasc(self) -> str:
        return self._data_nasc
    
    @property
    def cpf(self) -> str:
        return self._cpf

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @data_nasc.setter
    def data_nasc(self, data_nasc: str):
        self._data_nasc = data_nasc
    
    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf
    

class Funcionario(Pessoa):

    # Utiliza o construtor do pai dentro do construtor do filho
    def __init__(self, nome, data_nascimento, cpf, num_cracha: int):
        super().__init__(nome, data_nascimento, cpf)
        self._num_cracha = num_cracha
    
    # Reutiliza a implementação do __str__ do pai dentro do filho
    def __str__(self):
        return '{}\nCracha: {}'.format(super().__str__(), self._num_cracha)
        
    @property
    def num_cracha(self) -> str:
        return self._num_cracha
    
    @num_cracha.setter
    def num_cracha(self, num_cracha: str):
        self._num_cracha = num_cracha


p = Pessoa('Marcus', '23-11-1997', '111.111.111-11')
f = Funcionario('Marcus', '23-11-1997', '111.111.111-11', 1)

print(f'\nObjeto Pessoa\n{p}', f'Objeto Funcionário\n{f}', sep='\n\n')







    