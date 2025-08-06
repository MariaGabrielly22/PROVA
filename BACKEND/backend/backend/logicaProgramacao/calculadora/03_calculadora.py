nota = int(input("Digite sua nota: "))

match nota:
    case 10:
        print("Parabéns, nota máxima!")
    case 9 | 8 | 7:
        print("Aprovado")
    case 6 | 5 | 4 | 3 | 2 | 1 | 0:
        print("Reprovado")
    case _:
        print("Nota inválida")