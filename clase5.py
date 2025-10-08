
"""
#1 Realizar un programa que me diga si un numero es par o impar
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Su numero es par")
else:
    print("E")
#2 Realizar un programa que genere la tabla de multiplicar de un numero ingresado por elusuario (del 1 al 10)
numero2 = input("Ingrese un numero: ")
match numero2:
    case "1":
        print("1, 2, 3 , 4, 5, 6, 7, 8, 9, 10")
    case "2":
        print("2, 4, 6, 8, 10, 12, 14, 16, 18, 20")
    case "3":
        print("3, 6, 9, 12, 15, 18, 21, 24, 27, 30")
    case "4":
        print("4, 8, 12, 16, 20, 24, 28, 32, 36, 40")
    case "5":
        print("5, 10, 15, 20, 25, 30, 35, 40, 45, 50")
    case "6":
        print("6, 12, 18, 24, 30, 36, 42, 48, 54, 60")
    case "7":
        print("7, 14, 21, 28, 35, 42, 49, 56, 63, 70")
    case "8":
        print("8, 16, 24, 32, 40, 48, 56, 64, 72, 80")
    case "9":
        print("9, 18, 27, 36, 45, 54, 63, 72, 81, 90")
    case "10":
        print("10, 20, 30, 40, 50, 60, 70, 80, 90, 100")
    case _: 
        print("No ha ingresado un numero")
#3 Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad
nombre3 = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
"""
#4 Realizar un programa donde el usuario ingrese una palabra y un numero e imprima porpantalla la palabra ingresa tantas veces como el numero ingresado
palabra = input("Ingrese una palabra: ")
numero = int(input("Ingrese un número: "))

for i in range (numero):
    print(palabra)

#5 Realizar un programa que sume los números ingresados por el usuario hasta que se ingrese un 0. Al finalizar nos debe mostrar la suma por pantalla
# Programa que suma números hasta que el usuario ingrese 0

suma = 0

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    
print(f"La suma total es: {suma}")

