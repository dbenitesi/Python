import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D' , 'E', 'F', 'G']
    minusculas = ['q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m']
    caracteres = ['!','#','%','&']

    todo = mayusculas + minusculas + caracteres

    contrasena= []

    for i in range(15):
        caracter_random = random.choice(todo)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva cointrasena es: ' + contrasena)

if __name__ == '__main__':
    run()
