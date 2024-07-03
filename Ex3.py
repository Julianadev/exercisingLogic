"""
 Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos
"""

class SolicitarNumeros:
    def __init__(self):
        self.numeros = []
        for i in range(3):
            self.numeros.append(self.solicitar_numero(f'Digite o {i+1}º número: '))

    def solicitar_numero(self, prompt):

        while True:
            try:
                return float(input(prompt))
            except ValueError as e:
                print('Entrada inválida. Por favor, digite um número válido.', e)

class Soma:
    def __init__(self, numeros):
        self.numeros = numeros

    def soma_quadrados(self):

        soma = sum(num ** 2 for num in self.numeros)
        return soma


if __name__ == "__main__":

    numeros = SolicitarNumeros()

    soma = Soma(numeros.numeros)

    print(f'A soma dos quadrados dos valores é: {soma.soma_quadrados()}')

