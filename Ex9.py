"""
Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).
"""

class Incrementando:
    def __init__(self, inicio):
        self.inicio = inicio

    def incrementando_numero(self):

        while self.inicio <= 100000:
            print(self.inicio)
            self.inicio += 1000
        print("FIM")

if __name__ == "__main__":
    incrementando_numero = Incrementando(0)
    incrementando_numero.incrementando_numero()
