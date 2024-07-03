"""
Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles
"""

def solicitar_numeros(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError as e:
            print('Entrada inválida. Por favor, digite um número inteiro valido ', e)


def main():

    numeros = []

    for i in range(3):
        valor = int(input(f'Digite o {i+1}º número: '))
        numeros.append(valor)

    print(f'A soma dos números é: {sum(numeros)}')

if __name__ == "__main__":
    main()










