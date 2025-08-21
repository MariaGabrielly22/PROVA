# Exemplo 2

def dividir_numeros(a, b):
    try:
        resultado = a / b                  
    except ZeroDivisionError:             
        print("Erro: Não é possível dividir por zero!")
    except TypeError:                    
        print("Erro: Valores precisam ser números!")
    else:
        print("Resultado da divisão:", resultado)
    finally:
        print("Operação finalizada.\n")  

dividirNumeros(10, 2)
dividirNumeros(10, 0)
dividirNumeros(10, "a")