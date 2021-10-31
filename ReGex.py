#!/usr/bin/python3

#RegEx Email function
import re

def emailChecker(mail):
    if re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        print ("El mail ingresado es correcto.")
    else:
        print("El mail ingresado es inválido.")
mail = input("Ingrese un mail: ")
emailChecker(mail)

#RegEx 2 Decimals
def decimals(price):
   if re.match(r"^[0-9]+\.[0-9]{2}$", price):
       print ("El valor ingresado es correcto.")
   else:
       print ("El valor ingresado es incorrecto.")
price = input("Ingrese un precio: ")
decimals(price)

#RegEx Cellphone in Bs As, Argentina
def validateCel(cel):
    if re.match(r"[1]{2}-[0-9]{4}-[0-9]{4}$", cel):
        print ("El Celular ingresado es correcto.")
    else:
        print ("El Celular ingresado es incorrecto.")
cel = input("Ingres el número de celular: ")
validateCel(cel)
