"""
Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
"""

class SolicitandoNumero:
    def __init__(self):
        self.numero = self.verificando_numero('Digite um número: ')

    def verificando_numero(self, prompt):

        while True:
            try:
                num = int(input(prompt))
                return num
                break
            except ValueError:
                print('Entrada inválida. Por favor, digite um número inteiro')

    def dobrandoNumero(self):

        return self.numero * 2

if __name__ == "__main__":

    numero = SolicitandoNumero()
    dobro = numero.dobrandoNumero()

    print(f'O dobro de {numero.numero} é: {dobro}')