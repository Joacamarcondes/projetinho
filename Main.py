from Celular import Celular
from Pessoa import Pessoa


c1 = Celular('Apple', 'Iphone17')
c2 = Celular('Sansung', 'Note S20', 200)

print('c1', c1.marca)
print('c2', c2.bateria)

print('[antes do uso] Bateria c1:', c1.bateria)
c1.usar()
c1.usar()
print('[depois do uso] Bateria c1:', c1.bateria)

p1 = Pessoa('Juca')

print(f'Dinheiro[{p1.nome}]:', p1.dinheiro)
p1.trabalhar()
p1.trabalhar()
p1.gastar()
print(f'Dinheiro[{p1.nome}]:', p1.dinheiro)

print()