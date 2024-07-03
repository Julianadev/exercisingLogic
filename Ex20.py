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
            raise TypeError('O número de telefone deve ser uma string')
        self._telefone = novo_telefone

    def imprimindo_dados(self):

        print(f'Nome: {self.nome} - Telefone: {self._telefone}')

class GerenciandoContatos:
    def __init__(self):
        self.contatos = {}

    def armazenar_contato(self):
        while True:
            try:
                nome = input('Digite o nome do contato: ').capitalize()
                telefone = input('Digite o telefone do contato: ')
                pessoa = Agenda(nome, telefone)
                self.contatos[pessoa.nome] = pessoa.telefone
                continuar = input('Deseja adicionar mais contatos? (s/n) ')
                if continuar.lower() != 's':
                    break
            except ValueError:
                print('Entrada inválida.')

    def remover_contatos(self):
        while True:
            removendo = input('Digite o contato que deseja excluir: ').capitalize()
            if removendo in self.contatos:
                del self.contatos[removendo]
                print(f'Contato {removendo} excluído com sucesso!')
                continuar = input('Deseja remover mais contatos? (s/n) ')
                if continuar.lower != 's':
                    break
            else:
                print('Contato não existe na agenda')
                continuar = input('Deseja tentar novamente? (s/n) ')
                if continuar != 's':
                    break

    def buscar_contato(self):
        if not self.contatos:
            print('Nenhum contato disponível.')
        else:
            while True:
                try:
                    nome_contato = input('Digite o contato que deseja buscar: ').capitalize()
                    indices = list(self.contatos.keys())
                    if nome_contato in indices:
                        index = indices.index(nome_contato)
                        telefone = self.contatos[nome_contato]
                        print(f'Contato {nome_contato} encontrado na posição: {index} e tem o telefone {telefone}')
                        continuar = input('Deseja buscar mais contatos? (s/n) ')
                        if continuar != 's':
                            break
                    else:
                        print(f'Contato {nome_contato} não encontrado na agenda.')
                except ValueError:
                    print('Entrada inválida')
    def imprimindo_contatos(self):
        if not self.contatos:
            print('Nenhum contato encontrado')
        else:
            for nome, telefone in self.contatos.items():
                print(f'Nome: {nome} - Telefone: {telefone}')
            print('\n')


if __name__ == "__main__":
    gerenciador = GerenciandoContatos()
    gerenciador.armazenar_contato()
    gerenciador.imprimindo_contatos()
    gerenciador.remover_contatos()
    gerenciador.imprimindo_contatos()
    gerenciador.buscar_contato()

