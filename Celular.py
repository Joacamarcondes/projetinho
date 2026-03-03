class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria

    def usar(self):
        print('Usando o celular...')
        self.bateria -= 10