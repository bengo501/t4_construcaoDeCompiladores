"""
teste 3: operador +=
adicionar o operador "+="
"""

import sys
import os
# ajusta o path dependendo de onde está o arquivo
if os.path.exists('src/gerador_codigo.py'):
    sys.path.insert(0, 'src')
elif os.path.exists('../src/gerador_codigo.py'):
    sys.path.insert(0, '../src')
else:
    sys.path.insert(0, '.')
from gerador_codigo import GeradorCodigo

def gerar_teste():
    """gera código de teste para operador +="""
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    # declara variável
    gc.declarar_variavel("x", "integer", 4)
    
    # inicializa x
    gc.ldc(10)
    gc.atribuir_variavel("x")
    
    # x += 5
    gc.ldc(5)
    gc.atribuicao_adicao("x")
    gc.drop()  # descarta valor retornado
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 3: operador +=")
    print("adicionar o operador '+='")
    print()
    print("programa fonte:")
    print("x : integer;")
    print("x := 10;")
    print("x += 5;   // x = x + 5")
    print()
    print("codigo gerado:")
    print(gerar_teste())


