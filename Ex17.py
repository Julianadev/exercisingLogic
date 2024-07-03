"""
Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
vogais e quantas são consoantes
"""
import os
import logging

class GerenciadorDePalavras:
    def __init__(self):
        self.contVogais = 0
        self.contConsoantes = 0
        self.vogais = 'aeiouAEIOU'
        self.gerenciar_arquivos()

    def gerenciar_arquivos(self):

        nome_arquivo = input('Digite o nome do arquivo que deseja fazer a leitura: ')

        if os.path.exists(nome_arquivo):
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    conteudo = arquivo.read()
                    self.verificando_caracteres(conteudo)
            except FileNotFoundError:
                logging.error(f'Arquivo {nome_arquivo} não existe.')
                print(f'Erro: O arquivo {nome_arquivo} não foi encontrado.')
        else:
            logging.error('Necessário adicionar um arquivo válido para continuar a execução do programa.')
            print('Erro: Necessário adicionar um arquivo válido para continuar a execução do programa.')


    def verificando_caracteres(self, conteudo):

        for char in conteudo:
            if char.isalpha():
                if char in self.vogais:
                    self.contVogais += 1
                else:
                    self.contConsoantes += 1

        print(f'O arquivo possui {self.contVogais} vogais e {self.contConsoantes} consoantes')
        

if __name__ == "__main__":
    GerenciadorDePalavras()


