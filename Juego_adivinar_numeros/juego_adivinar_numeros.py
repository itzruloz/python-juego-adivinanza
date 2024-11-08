import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinar el número secreto entre 1 y 100")
    print("Tienes que adivinar el número secreto en menos de 10 intentos")
    print("intenta adivinarlo")

    while not adivinado:
        numeroAdivinar = input("Introduce un número: ")

        if numeroAdivinar.isdigit():
            numeroAdivinar = int(numeroAdivinar)
            intentos += 1
        else:
            print("Por favor introduce un número válido")
            continue

        if numeroAdivinar < numero_secreto:
            print(f"El número secreto es mayor a {numeroAdivinar}")
        elif numeroAdivinar > numero_secreto:
            print(f"El número secreto es menor a {numeroAdivinar}")
        else:
            adivinado = True
            print(
                f"Felicidades, has adivinado el número secreto en intento número: {intentos} y el número secreto era {numero_secreto}")
            break


juego_adivinanza()
