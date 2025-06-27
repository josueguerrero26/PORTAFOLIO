from secret import get_secret_word, get_hint, check_guess


def pay_game():
    #definamos las variables y dar mensaje de bienvenida
    print("Bienvenido al juego de adivinar la palabra secreta: ")

    secret = get_secret_word()
    max_intentos = 4
    intentos = 0
    score = 0
    print(get_hint(secret))
    while intentos < max_intentos:
        guess = input(f'Intentos {intentos + 1}/{max_intentos} adivina la palabra: ').strip()
        guessed, points = check_guess(secret, guess, intentos)
        score += points
        if guessed:
            break
        if intentos < max_intentos:
            print(f'Tu puntaje es {score}')
        else:
            print(f'La palabra secreta era {secret}')
    print(f'Tu puntaje es {score}')
            

if __name__ == '__main__':
    pay_game()