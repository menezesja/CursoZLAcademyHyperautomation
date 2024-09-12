import os
import shutil

import time

os.mkdir('exemplo_diretorio')

with open('exemplo_diretorio/arquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')

shutil.copy('exemplo_diretorio/arquivo.txt', 'arquivo_copia.txt')

shutil.move('arquivo_copia.txt', 'arquivo_renomeado.txt')

time.sleep(10)

os.remove('exemplo_diretorio/arquivo.txt')
os.mkdir('exemplo_diretorio')