numero_secreto = 22

while True:
    palpite = int(input("Tente adivinhar o número secreto: "))
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns, você acertou!")
        break