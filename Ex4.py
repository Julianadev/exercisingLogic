"""
 Faça um programa que receba dois números inteiros e mostre qual deles é o maior
"""

class NumerosInteiros:
    def __init__(self):
        self.lista = []
        for i in range(2):
            self.lista.append(self.solicitar_numeros(f'Digite o {i+1}º número: '))

    def solicitar_numeros(self, prompt):

        while True:
            try:
                return int(input(prompt))
            except ValueError as e:
                print('Entrada inválida. Por favor, digite um número válido.', e)

    def max_min(self):

        print(f'O maior número é: {max(self.lista)}')



if __name__ == "__main__":

    num = NumerosInteiros()

    num.max_min()
