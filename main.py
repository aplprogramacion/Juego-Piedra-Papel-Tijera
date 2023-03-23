# Importar el módulo random para generar la elección aleatoria de la computadora
import random

# Pedir al usuario que elija entre rock, paper o scissors
jugada = input("Elige entre rock, paper o scissors: ")

# Generar la elección aleatoria de la computadora
opciones = ["rock", "paper", "scissors"]
computadora = random.choice(opciones)

# Imprimir la elección de la computadora
print(f"La computadora eligió: {computadora}")

# Determinar el resultado del juego
if jugada == computadora:
    print("Empate")
elif jugada == "rock":
    if computadora == "paper":
        print("La computadora gana")
    else:
        print("Tú ganas")
elif jugada == "paper":
    if computadora == "scissors":
        print("La computadora gana")
    else:
        print("Tú ganas")
elif jugada == "scissors":
    if computadora == "rock":
        print("La computadora gana")
    else:
        print("Tú ganas")
else:
    print("Jugada inválida. Elige entre rock, paper o scissors.")

