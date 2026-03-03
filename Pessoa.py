class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0

    def trabalhar(self):
        print('trabalhei...')
        self.dinheiro += 50

    def gastar(self ):
        print('Ganhei...')
        self.dinheiro -= 20