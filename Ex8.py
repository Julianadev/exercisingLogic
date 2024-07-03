"""
Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem
"""
import time
class ContagemRegressiva:
    def __init__(self, inicio):
        self.inicio = inicio

    def contagem(self):

        while self.inicio >= 0:
            print(self.inicio)
            self.inicio -= 1
            time.sleep(2)
        print("FIM")


if __name__ == "__main__":

    contagem = ContagemRegressiva(10)
    contagem.contagem()


