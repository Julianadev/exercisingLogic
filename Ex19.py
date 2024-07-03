"""
Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

import datetime

class Pessoa:
    def __init__(self, nome, data_nascimento, email):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError('O nome deve ser uma string')
        self._nome = novo_nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        try:
            nova_data = datetime.datetime.strptime(nova_data, "%d/%m/%Y")
        except ValueError:
            raise TypeError('A data deve ser no formato DD/MM/YYYY')
        self._data_nascimento = nova_data

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email, str):
            raise TypeError('O email deve ser uma string')
        self._email = novo_email

    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Email: {self.email}")
        print('\n')

class GerenciandoDados:
    def __init__(self):
        self.lista = []

    def inserindo_dados(self):
        while True:
            try:
                nome = input('Digite o nome: ').capitalize()
                data_nascimento = input('Digite a data de nascimento (DD/MM/YYYY): ')
                email = input('Digite o email: ')
                pessoa = Pessoa(nome, data_nascimento, email)
                self.lista.append(pessoa)
                continuar = input('Deseja adicionar outra pessoa? (s/n): ')
                if continuar.lower() != 's':
                    break
            except ValueError:
                print('Entrada inválida')

    def imprimindo(self):
        for pessoa in self.lista:
            pessoa.imprimir_dados()

if __name__ == "__main__":
    gerenciador = GerenciandoDados()
    gerenciador.inserindo_dados()
    gerenciador.imprimindo()








