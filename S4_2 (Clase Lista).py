# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:42:49 2022
@author: grace
"""

lista=[7,8.9,"Hola",True,5]
lista2=[1,50,60,80,58]

print(type(lista))
print(len(lista))
print(lista)
print(lista[3])
print("\n"*1)

tupla=(7,8.9,"Hola",True,5)
print(tupla)
print(tupla[-5])
print(lista[-4])

print("\n"*1)
lista[3]="CEC-EPN"
#tupla[0]=15 No es posible en tupla
del lista[1]
#del tupla [4] No es posible en  tupla
print(lista)
