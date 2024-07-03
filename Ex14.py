"""
 Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.
"""
import datetime

class SolicitandoData:
    def __init__(self):
        self.data = self.verificarData('Digite uma data: (Ex: 01/01/2024) ')

    def verificarData(self, prompt):

        while True:
            try:
                data = str(input(prompt))
                return data
            except ValueError:
                print('Entrada inválida. Por favor digite uma data válida.')

    def dataPorExtenso(self):

        data = datetime.datetime.strptime(self.data, "%d/%m/%Y")

        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
                 "outubro", "novembro", "dezembro"]

        print(f'{data.day} de {meses[data.month - 1]} de {data.year}')


if __name__ == "__main__":

    data = SolicitandoData()

    data.dataPorExtenso()
