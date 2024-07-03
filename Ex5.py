"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

import math

class SolicitarNumeros:
    def __init__(self):
        self.numero = self.solicitar_numero('Digite um número inteiro: ')

    def solicitar_numero(self, prompt):

        while True:
            try:
                return int(input(prompt))
            except ValueError as e:
                print('Entrada inválida. Por favor, digite um número válido.', e)

class NumeroPositivo:
    def __init__(self, positivo):
        self.positivo = positivo

    def resultado(self):

        try:
            if self.positivo.numero >= 0:
                raiz_quadrada = math.sqrt(self.positivo.numero)
                return f'A raíz quadrada é {raiz_quadrada:.2f}'
            elif self.positivo.numero < 0:
                return 'Número é inválido.'
            else:
                print('Digite um número válido')
        except ValueError:
            print('Entrada inválida')

if __name__ == "__main__":

    numero = SolicitarNumeros()

    res = NumeroPositivo(numero)

    print(res.resultado())



