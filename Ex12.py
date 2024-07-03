"""
 Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""

class SolicitandoNumero:
    def __init__(self):
        self.lista = []
        for i in range(10):
            self.inserindoNumeros(f'Digite o {i+1}° número: ')

    def inserindoNumeros(self, prompt):

        while True:
            try:
                num = int(input(prompt))
                self.lista.append(num)
                break
            except ValueError:
                print('Entrada inválida. Por favor, digite um número inteiro válido.')


    def verificandoParidade(self):

        pares = [num for num in self.lista if num % 2 == 0]
        print(f'A lista {self.lista} tem {len(pares)} valores pares.')



if __name__ == "__main__":

    numero = SolicitandoNumero()

    numero.verificandoParidade()

