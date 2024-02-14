#Piedra, Papel o Tijeras
from multiprocessing.connection import wait
import random
import time
#import keyword
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
welcome = "Bienvenido al juego mas divertido de Python: Piedra(1), Papel(2) y Tijeras(3). Que vas a escoger: "
intermedio = "La casa esta por escoger, y recuerda que la casa siempre gana y la casa escoge: "

#while True:
a = [0,1,2]
imagenes = [rock, paper, scissors]
piedra = 1
papel = 2
tijera = 3
usuario = int(input(print(welcome)))
printeada = usuario - 1
print(imagenes[printeada])
print("\n")
print(intermedio)
time.sleep(3)
casa_eleccion = random.choice(a)
print(imagenes[casa_eleccion])
if printeada < casa_eleccion and casa_eleccion > 2:
    print("Has Ganado")
if printeada > casa_eleccion:
    print("Has Ganado")    
elif printeada == casa_eleccion:
    print("Empate")
else:
    print("Perdiste")
    #if keyboard.is_pressed("q"):
        #print("q pressed, ending loop")
        #break

