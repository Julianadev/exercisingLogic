class Televisao:
    def __init__(self):
        self.status = False  # False para desligado, True para ligado
        self.volume = 10     # Volume inicial
        self.canal = 1       # Canal inicial

    def ligar(self):
        self.status = True
        print('A TV está ligada.')

    def desligar(self):
        self.status = False
        print('A TV está desligada.')

    def aumentar_volume(self):
        if self.status:
            if self.volume < 100:
                self.volume += 1
                print(f'Volume: {self.volume}')
            else:
                print('Volume máximo atingido.')
        else:
            print('A TV está desligada.')

    def diminuir_volume(self):
        if self.status:
            if self.volume > 0:
                self.volume -= 1
                print(f'Volume: {self.volume}')
            else:
                print('Volume mínimo atingido.')
        else:
            print('A TV está desligada.')

    def aumentar_canal(self):
        if self.status:
            self.canal += 1
            print(f'Canal: {self.canal}')
        else:
            print('A TV está desligada.')

    def diminuir_canal(self):
        if self.status:
            if self.canal > 1:
                self.canal -= 1
                print(f'Canal: {self.canal}')
            else:
                print('Este é o menor canal disponível.')
        else:
            print('A TV está desligada.')

    def trocar_canal(self, novo_canal):
        if self.status:
            if isinstance(novo_canal, int) and novo_canal > 0:
                self.canal = novo_canal
                print(f'Canal alterado para: {self.canal}')
            else:
                print('Número de canal inválido.')
        else:
            print('A TV está desligada.')


class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao

    def ligar(self):
        self.televisao.ligar()

    def desligar(self):
        self.televisao.desligar()

    def aumentar_volume(self):
        self.televisao.aumentar_volume()

    def diminuir_volume(self):
        self.televisao.diminuir_volume()

    def aumentar_canal(self):
        self.televisao.aumentar_canal()

    def diminuir_canal(self):
        self.televisao.diminuir_canal()

    def trocar_canal(self, novo_canal):
        self.televisao.trocar_canal(novo_canal)


# Exemplo de uso
tv = Televisao()
controle = ControleRemoto(tv)

# Controlando a TV diretamente
tv.ligar()
tv.aumentar_volume()
tv.trocar_canal(5)
tv.diminuir_canal()
tv.desligar()

# Controlando a TV via controle remoto
controle.ligar()
controle.aumentar_volume()
controle.trocar_canal(10)
controle.diminuir_volume()
controle.desligar()
