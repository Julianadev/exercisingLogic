"""
Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.

"""

class SolicitarNumeros:
    def __init__(self):
        self.lista = []
        for i in range(7):
            self.solicitar_numeros(f'Digite o {i+1}º número: ')

    def solicitar_numeros(self, prompt):

        while True:
            try:
                num = int(input(prompt))
                self.lista.append(num)
                break
            except ValueError:
                print('Entrada inválida. Por favor, digite uma entrada válida.')

if __name__ == "__main__":

    numero = SolicitarNumeros()
    print('Lista: ', numero.lista)
