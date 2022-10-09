# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:43:50 2022

@author: grace
"""

def readint(prompt, min, max):
    while (True):
        try:
            valor = int(input(prompt))
        except ValueError:
            print("Error de ingreso")
        else:
            if(min <= valor <= max):
                break
            else:
                print("Error: el valor no está en el rango permitido (-10..10)")
    return valor    

v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)

#valor!=v
