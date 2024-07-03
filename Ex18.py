"""
Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
arquivo possui
"""
import os

class ContadorDeLinhas:
    def __init__(self):
        self.lendo_arquivo()

    def lendo_arquivo(self):

        nome_arquivo = input('Digite o nome do arquivo: ')

        if os.path.exists(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    conteudo = arquivo.readlines()

                    print(f'O arquivo possui {len(conteudo)} linhas.')
            except FileNotFoundError:
                print(f'O arquivo {nome_arquivo} não existe.')

if __name__ == "__main__":

    ContadorDeLinhas()