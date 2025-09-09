import random

numero_magico = random.randint (1,100)
numero_usuario = 0


while numero_usuario != numero_magico:
    numero_usuario = int(input("digite o numero entre 1 a 100:"))

    if numero_usuario == numero_magico :
        print ("parabens, voce acertou!")

    elif numero_magico > numero_usuario:
        print ("o numero magico é maior")

    else:
        print("o numero magico é menor")

