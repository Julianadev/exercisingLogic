"""
Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:

a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

class Agenda:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise TypeError('O nome deve ser uma string')
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, str):
            raise TypeError('O telefone deve ser uma string')
        self._telefone = novo_telefone

    def imprimir_dados(self):

        print(f'Nome: {self.nome} | Telefone: {self.telefone}')

class GerenciandoContatos:
    def __init__(self):
        self.contatos = []

    def armazenar_contato(self):

        while True:
            try:
                nome = input('Digite o nome do contato: ').capitalize()
                telefone = input('Digite o telefone do contato: ')
                pessoas = Agenda(nome, telefone)
                self.contatos.append(pessoas)
                continuar = input('Deseja adicionar mais contatos? (s/n) ')
                if continuar.lower() != 's':
                    break
            except ValueError:
                print('Entrada inválida')

    def remover_contato(self):
        while True:
            nome = input('Digite o nome do contato que deseja excluir: ').capitalize()
            for contato in self.contatos:
                if contato.nome == nome:
                    self.contatos.remove(contato)
                    print(f'Contato {nome} excluído com sucesso!')
                    break
            else:
                print('Contato não encontrado.')
            continuar = input('Deseja remover mais contatos? (s/n) ')
            if continuar.lower() != 's':
                break

    def buscar_contato(self):
        while True:
            nome = input('Digite o nome do contato que deseja buscar: ').capitalize()
            for indice, contato in enumerate(self.contatos):
                if contato.nome == nome:
                    print(f'Contato {nome} encontrado na posição {indice}.')
                    contato.imprimir_dados()
                    break
            else:
                print('Contato não encontrado.')
            continuar = input('Deseja buscar mais contatos? (s/n) ')
            if continuar.lower() != 's':
                break

    def imprimir_agenda(self):

        if self.contatos is None:
            print('Agenda vazia.')
        else:
            for contato in self.contatos:
                contato.imprimir_dados()
            print('\n')

    def imprimir_contato(self, indice):

        if not self.contatos:
            print('Agenda vazia')
        elif 0 <= indice < len(self.contatos):
            self.contatos[indice].imprimir_dados()
        else:
            print('índice não encontrado.')

if __name__ == "__main__":
    gerenciador = GerenciandoContatos()
    gerenciador.armazenar_contato()
    gerenciador.imprimir_agenda()
    gerenciador.remover_contato()
    gerenciador.imprimir_agenda()
    gerenciador.buscar_contato()

    indice = int(input('Digite o índice do contato que deseja imprimir: '))
    gerenciador.imprimir_contato(indice)

