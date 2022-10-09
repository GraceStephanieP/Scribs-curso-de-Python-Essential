# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:52:59 2022

@author: grace
"""

def F(n):
    SecuenciaF=[] #lista de la secuencia
    a = 0 #constante inicial
    b = 1 #constante inicial
    while b<=n:
        c=a+b #variable
        a=b
        b=c
        SecuenciaF.append(a) #adjuntar a lista
    print(SecuenciaF)
    
F(int(input("Ingrese número límite de Fibonacci: ")))