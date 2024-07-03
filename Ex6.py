"""
 Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""

class SolicitarNumero:
    def __init__(self):
        self.numero = self.solicitar_numero('Digite um número inteiro: ')

    def solicitar_numero(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print('Entrada inválida. Por favor, digite um número válido.')

class Verificar:
    def __init__(self, numero):
        self.numero = numero

    def parImpar(self):

        if self.numero.numero % 2 == 0:
            return 'Número Par'
        else:
            return 'Número Ímpar'

if __name__ == "__main__":

    numero = SolicitarNumero()

    res = Verificar(numero)

    print(res.parImpar())
