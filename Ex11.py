"""
Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:

a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha
"""

class ListandoNumeros:
    def __init__(self):
        self.listaA = [1, 0, 5, -2, -5, 7]

    def soma(self):

        soma_numeros = self.listaA[0] + self.listaA[1] + self.listaA[5]
        print(f'A soma dos números é: {soma_numeros}')


    def set_soma(self):

        self.listaA[5] = 100

    def listando(self):

        for num in self.listaA:
            print(num)

if __name__ == "__main__":

    numero = ListandoNumeros()

    numero.soma()

    numero.set_soma()

    numero.listando()