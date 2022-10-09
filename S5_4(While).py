# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:52:49 2022

@author: grace
"""
"""
#1 Uso de while 
numero=input("Ingrese # al que debo contar: ")
numero=int(numero)
contador=1
while contador<= numero:
    print (contador)
    contador+=1 #contador = contador+1
"""

#2 Uso de while
numero=input("Ingrese # al que debo contar: ")
numero=int(numero)
contador=1
while True:
    print (contador)
    contador+=1 #contador = contador+1
    if contador>numero:
        break