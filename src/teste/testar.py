"""
script de teste completo - verifica todas as funcionalidades
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

def testar_expressao_atribuicao():
    """testa expressão de atribuição"""
    print("testando: expressão de atribuição")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("x", "integer", 4)
    gc.declarar_variavel("y", "integer", 4)
    
    gc.ldc(5)
    gc.expressao_atribuicao("x")
    gc.expressao_atribuicao("y")
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    # verifica se contém instruções esperadas
    assert "DUP" in codigo, "deve conter DUP para expressão de atribuição"
    assert "STA _x" in codigo, "deve atribuir a x"
    assert "STA _y" in codigo, "deve atribuir a y"
    print("  [ok] expressao de atribuicao")
    return True

def testar_incremento():
    """testa incremento e decremento"""
    print("testando: incremento e decremento")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("a", "integer", 4)
    
    gc.pre_incremento("a")
    gc.pos_incremento("a")
    gc.pre_decremento("a")
    gc.pos_decremento("a")
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "LDA _a" in codigo, "deve carregar variável a"
    assert "ADD" in codigo, "deve usar ADD para incremento"
    assert "SUB" in codigo, "deve usar SUB para decremento"
    print("  [ok] incremento/decremento")
    return True

def testar_operador_mais_igual():
    """testa operador +="""
    print("testando: operador +=")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("x", "integer", 4)
    
    gc.ldc(10)
    gc.atribuir_variavel("x")
    gc.ldc(5)
    gc.atribuicao_adicao("x")
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "LDA _x" in codigo, "deve carregar x"
    assert "ADD" in codigo, "deve usar ADD"
    assert "STA _x" in codigo, "deve atribuir a x"
    print("  [ok] operador +=")
    return True

def testar_operador_condicional():
    """testa operador condicional ?:"""
    print("testando: operador condicional ?:")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("x", "integer", 4)
    gc.declarar_variavel("y", "integer", 4)
    gc.declarar_variavel("z", "integer", 4)
    
    gc.carregar_variavel("x")
    gc.carregar_variavel("y")
    gc.grt()
    
    rotulo_else = gc.ts.novo_rotulo_cod()
    rotulo_fim = gc.ts.novo_rotulo_cod()
    
    gc.jzer(rotulo_else)
    gc.carregar_variavel("x")
    gc.jmp(rotulo_fim)
    gc.emitir_rotulo(rotulo_else)
    gc.carregar_variavel("y")
    gc.emitir_rotulo(rotulo_fim)
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "GRT" in codigo, "deve usar GRT para comparação"
    assert "JZER" in codigo, "deve usar JZER para condicional"
    assert "JMP" in codigo, "deve usar JMP"
    print("  [ok] operador condicional ?:")
    return True

def testar_do_while():
    """testa comando do-while"""
    print("testando: comando do-while")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("i", "integer", 4)
    
    rotulo_inicio, rotulo_fim = gc.inicio_do_while()
    gc.pos_incremento("i")
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.fim_do_while()
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "JNZ" in codigo, "deve usar JNZ para do-while"
    print("  [ok] do-while")
    return True

def testar_for():
    """testa comando for"""
    print("testando: comando for")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("i", "integer", 4)
    
    gc.ldc(0)
    gc.atribuir_variavel("i")
    
    rotulo_teste, rotulo_incremento, rotulo_fim = gc.inicio_for()
    gc.carregar_variavel("i")
    gc.ldc(10)
    gc.les()
    gc.teste_for()
    
    gc.carregar_variavel("i")
    gc.ldc(1)
    gc.add()
    gc.atribuir_variavel("i")
    gc.fim_for()
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "JMP" in codigo, "deve usar JMP"
    assert "JZER" in codigo, "deve usar JZER para teste"
    print("  [ok] for")
    return True

def testar_break_continue():
    """testa break e continue"""
    print("testando: break e continue")
    gc = GeradorCodigo()
    gc.inicio_programa()
    gc.declarar_variavel("i", "integer", 4)
    
    rotulo_inicio, rotulo_fim = gc.inicio_while()
    gc.break_cmd()
    gc.continue_cmd()
    gc.fim_while()
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "JMP" in codigo, "deve usar JMP para break/continue"
    print("  [ok] break e continue")
    return True

def testar_struct():
    """testa variáveis do tipo struct"""
    print("testando: variáveis do tipo struct")
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_struct("Ponto", [
        ("x", "integer", 4),
        ("y", "integer", 4)
    ])
    
    gc.declarar_variavel_struct("p", "Ponto")
    
    gc.ldc(10)
    gc.carregar_variavel("p")
    gc.ldc(0)
    gc.add()
    gc.emitir("STI")
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "_p DS 8" in codigo, "deve reservar 8 bytes para struct"
    assert "STI" in codigo, "deve usar STI para armazenar em struct"
    print("  [ok] struct")
    return True

def testar_array():
    """testa arrays de inteiros"""
    print("testando: arrays de inteiros")
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_array("arr", "integer", 4, 5)
    
    gc.ldc(0)
    gc.ldc(10)
    gc.atribuir_array_elemento("arr")
    
    gc.ldc(2)
    gc.carregar_array_elemento("arr")
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "_arr DS 20" in codigo, "deve reservar 20 bytes para array"
    assert "STI" in codigo, "deve usar STI para array"
    assert "LDI" in codigo, "deve usar LDI para carregar de array"
    print("  [ok] arrays de inteiros")
    return True

def testar_struct_com_array():
    """testa struct com array"""
    print("testando: struct com array")
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_struct("Pessoa", [
        ("idade", "integer", 4),
        ("scores", "array[3]", 12)
    ])
    
    gc.declarar_variavel_struct("p", "Pessoa")
    
    gc.ldc(100)
    gc.carregar_variavel("p")
    gc.ldc(4)
    gc.add()
    gc.ldc(0)
    gc.ldc(4)
    gc.mul()
    gc.add()
    gc.emitir("STI")
    
    gc.fim_programa()
    codigo = gc.get_codigo()
    
    assert "_p DS 16" in codigo, "deve reservar 16 bytes"
    print("  [ok] struct com array")
    return True

def executar_todos_testes():
    """executa todos os testes"""
    print("=" * 60)
    print("executando testes do gerador de código")
    print("=" * 60)
    print()
    
    testes = [
        testar_expressao_atribuicao,
        testar_incremento,
        testar_operador_mais_igual,
        testar_operador_condicional,
        testar_do_while,
        testar_for,
        testar_break_continue,
        testar_struct,
        testar_array,
        testar_struct_com_array
    ]
    
    resultados = []
    for teste in testes:
        try:
            resultado = teste()
            resultados.append(("ok", teste.__name__))
        except AssertionError as e:
            print(f"  [erro] {e}")
            resultados.append(("erro", teste.__name__))
        except Exception as e:
            print(f"  [excecao] {e}")
            resultados.append(("exceção", teste.__name__))
        print()
    
    print("=" * 60)
    print("resumo dos testes")
    print("=" * 60)
    
    ok = sum(1 for status, _ in resultados if status == "ok")
    erros = sum(1 for status, _ in resultados if status != "ok")
    
    print(f"testes passaram: {ok}/{len(testes)}")
    print(f"testes falharam: {erros}/{len(testes)}")
    
    if erros > 0:
        print("\ntestes que falharam:")
        for status, nome in resultados:
            if status != "ok":
                print(f"  - {nome}: {status}")
    
    print()
    return erros == 0

if __name__ == "__main__":
    sucesso = executar_todos_testes()
    if sucesso:
        print("[ok] todos os testes passaram!")
    else:
        print("[erro] alguns testes falharam")
    exit(0 if sucesso else 1)

