import random


def obtener_palabra_secreta() -> str:
    palabras = ['python', 'java', 'angular', 'javascript', 'django',
                'tensorflow', 'git', 'flask', 'docker', 'kubernetes']
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):

    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_acertadas = []
    intentos = 7
    juego_terminado = False

    print('¡Bienvenido al juego del ahorcado!')
    print(f'Tienes {intentos} intentos para adivinar la palabra secreta')
    print(mostrar_progreso(palabra_secreta, letras_acertadas),
          " La cantidad de letras de la palabra secreta es: ", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input('Ingresa una letra: ').lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print('Por favor, una letra valida (solo escribir una letra)')
        elif adivinanza in letras_acertadas:
            print('Ya has adivinado esa letra')
        else:
            letras_acertadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(
                    f"¡Bien! La letra '{adivinanza}' está en la palabra secreta")
            else:
                intentos -= 1
                print(
                    f"¡Oh no! La letra '{adivinanza}' no está en la palabra secreta")
                print(f'Te quedan "{intentos}" intentos')

        progreso_actual = mostrar_progreso(palabra_secreta, letras_acertadas)
        print(progreso_actual)

        if '_' not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(
                f'¡Felicidades! Has adivinado la palabra secreta, la palabra secreta era: {palabra_secreta}')

    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(
            f'¡Oh no! Has perdido, se te acabaron los intentos, la palabra secreta era: {palabra_secreta}')


juego_ahorcado()
