from handler import *

cesta = 'texty/klasifikuj/klasifikuj.txt'

with open(cesta, 'r') as pesnicka:
    data=pesnicka.read().replace('\n', '')

klasifikuj(data)