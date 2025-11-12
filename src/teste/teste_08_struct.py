#teste 8: variáveis do tipo struct
#adicionar possibilidade de usar variáveis do tipo struct
import _import_helper# import helper que configura o path corretamente
from gerador_codigo import GeradorCodigo

def gerar_teste():#gera codigo de teste para variáveis do tipo struct
    gc = GeradorCodigo()
    gc.inicio_programa()
    
    gc.declarar_struct("Ponto", [ #declara a struct Ponto
        ("x", "integer", 4),
        ("y", "integer", 4)
    ]) #declara a struct Ponto
    
    gc.declarar_variavel_struct("p", "Ponto") #declara a variável p do tipo Ponto   
    
    # p.x := 10
    gc.ldc(10) #carrega o valor 10
    gc.carregar_variavel("p") #carrega a variável p
    gc.ldc(0) #carrega o valor 0 (offset do campo x)
    gc.add() #adição
    gc.emitir("STI") #emite a instrução STI
    
    # p.y := 20
    gc.ldc(20) #carrega o valor 20
    gc.carregar_variavel("p") #carrega a variável p
    gc.ldc(4) #carrega o valor 4 (offset do campo y)
    gc.add() #adição
    gc.emitir("STI") #emite a instrução STI
    
    gc.fim_programa()
    return gc.get_codigo()

if __name__ == "__main__":
    print("teste 8: variaveis do tipo struct")
    print("adicionar possibilidade de usar variaveis do tipo struct")
    print()
    print("programa fonte:")
    print("struct Ponto {")
    print("    x : integer;")
    print("    y : integer;")
    print("};")
    print("p : Ponto;")
    print("p.x := 10;")
    print("p.y := 20;")
    print()
    print("codigo gerado:")
    print(gerar_teste())


