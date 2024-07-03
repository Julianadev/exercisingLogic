"""
Faça um programa que leia um número inteiro e imprima-o
"""

def numeroInteiro():
    try:
        numero = int(input('Digite um número inteiro: '))

        print(f'O número digitado foi: {numero}')
    except ValueError as e:
        print('Entrada inválida. Digite um número inteiro válido.', e)

numeroInteiro()

    