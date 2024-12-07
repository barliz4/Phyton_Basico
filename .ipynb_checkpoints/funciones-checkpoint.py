def saludar(nombre):
    print(f"¡Hola, {nombre}!")      #La F es muy importante para que el sistema lea la funciónA

usuario = input ("Ingrese su nombre en la consola: ")

# Llamar a la función
saludar(usuario)  # Imprime "¡Hola, y el nombre de usuario!"



def sumar(a, b):
    return a + b

num1=int (input ("Ingrese el numero 1: "))
num2=int (input ("Ingrese el numero 2: "))


resultado = sumar(num1,num2)
print(resultado)  # Imprime 