"""
 Crie um programa que:

a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere
“0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""
import os
class CriandoArquivo:
    def __init__(self):
        self.arquivo = 'arq.txt'
        self.gravarCaracteres()

    def gravarCaracteres(self):

        with open(self.arquivo, 'w') as arquivo:
            while True:
                caractere = input('Digite um caractere ou digite "0" para sair: ')
                if caractere == '0':
                    break
                arquivo.write(caractere)

    def lendoArquivo(self):

        with open(self.arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(f'Conteúdo do arquivo {self.arquivo}:\n{conteudo}')



if __name__ == "__main__":

    arquivo = CriandoArquivo()
    arquivo.lendoArquivo()
