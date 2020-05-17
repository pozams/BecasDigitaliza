# -*- coding: utf-8 -*-
"""
@author: spm
"""

import math

def menu():
    print("""
    
    *********************************************************
                           CALCULADORA 
                (BECAS DIGITALIZA - CURSO DEVNET)
    *********************************************************      
    """)
    
def opciones():
    operacion = input("""
    MENÚ:
    ----------------------------------------------
    1. SUMA
    2. RESTA
    3. MULTIPLICACIÓN
    4. DIVISIÓN
    5. POTENCIA
    6. RAÍZ CUADRADA
    
    0. SALIR
    
    Seleccione la operación a realizar: """)

    return operacion
    

def suma():
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    resultado = str(num1 + num2)
    print("\n{} + {} = ".format(num1, num2) + resultado)


def resta():
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    resultado = str(num1 - num2)
    print("\n{} - {} = ".format(num1, num2) + resultado)


def multiplicacion():
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))
    resultado = str(num1 * num2)
    print("\n{} * {} = ".format(num1, num2) + resultado)


def division():
    num1 = int(input("Introduzca el primer número: "))
    num2 = int(input("Introduzca el segundo número: "))

    while num2 == 0:
        print("Introduzca un número mayor que 0 \n")
        num2 = int(input("Por favor, introduzca el segundo número: "))

    resultado = str(num1 / num2)
    print("\n{} / {} = ".format(num1, num2) + resultado)


def exponencial():
    num1 = int(input("Introduzca un número: "))
    num2 = int(input("Introduza el exponente: "))
    resultado = str(num1 ** num2)
    print("\n{} elevado a {} = ".format(num1, num2) + resultado)


def raiz_cuadrada():
    num = int(input("Introduzca un número para saber su raiz cuadrada: "))
    resultado = math.sqrt(num)
    print("\n La raíz cuadrada de", num, "es: ", resultado)


menu()

op = 1
while op > 0:
    
    operacion = opciones()
    if operacion == "1":
        suma()
        parar = input("Pulsa 0 para salir o cualquier otra tecla para realizar otra operación: ")
        if parar == "0":
            op = int(parar)
   
    elif operacion == "2":
        resta()
        parar = input("Pulsa 0 para salir o cualquier otra tecla para realizar otra operación: ")
        if parar == "0":
            op = int(parar)

    elif operacion == "3":
        multiplicacion()
        parar = input("Pulsa 0 para salir o cualquier otra tecla para realizar otra operación: ")
        if parar == "0":
            op = int(parar)

    elif operacion == "4":
        division()
        parar = input("Pulsa 0 para salir o cualquier otra tecla para realizar otra operación: ")
        if parar == "0":
            op = int(parar)

    elif operacion == "5":
        exponencial()
        parar = input("Pulsa 0 para salir o cualquier otra tecla para realizar otra operación: ")
        if parar == "0":
            op = int(parar)

    elif operacion == "6":
        raiz_cuadrada()
        parar = input("Pulsa 0 para salir o cualquier otra tecla para realizar otra operación: ")
        if parar == "0":
            op = int(parar)

    elif operacion == "0":
        break
    
    else:
        print("\n------------------------------------------------------------------")
        print("El valor introducido no se corresponde a ninguna operación del menú")
        print("-------------------------------------------------------------------")