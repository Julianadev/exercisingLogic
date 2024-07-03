"""
Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0
"""

class SolicitarNumero:
    def __init__(self):
        self.numero = self.solicitar_numero('Digite um número inteiro: ')

    def solicitar_numero(self, prompt):

        while True:
            try:
                num = int(input(prompt))
                if num > 0:
                    return num
                else:
                    return 'O número deve ser maior que 0'
            except ValueError:
                print('Entrada inválida. Insira um número válido.')

class VerificaNumero:
    def __init__(self, numero):
        self.numero = numero

    def multiplos(self):

       multiplos = [self.numero * i for i in range(1, 6)]
       return multiplos

if __name__ == "__main__":

    numero = SolicitarNumero().numero

    res = VerificaNumero(numero)

    print("Os cinco primeiros múltiplos de 3 são:", res.multiplos())
