# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:27:57 2022

@author: grace
"""

def Fb(n):
    a=0 #constante inicial
    b=1 #constante inicial
    i=1 #contador
    Secuencia=[b]
    while i<=n-1:
        c=a+b #variable
        a=b
        b=c
        i=i+1
        Secuencia.append(c) #adjuntar a lista
    print(Secuencia)

Fb(int(input("Ingrese número de items: ")))
