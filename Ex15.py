"""
Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""

class SolicitandoValores:
    def __init__(self):
        self.lista = [self._solicitandoValores(f'Digite o {i+1}° número') for i in range(10)]

    def _solicitandoValores(self, prompt):

        while True:
            try:
                valor = int(input(prompt))
                return valor
            except ValueError:
                print('Entrada inválida. Por favor digite uma lista de inteiros válidos.')

    def maiorValor(self):

        return max(self.lista)

if __name__ == "__main__":
    numeros = SolicitandoValores()
    print(f'O maior número de {numeros.lista} é {numeros.maiorValor()}')