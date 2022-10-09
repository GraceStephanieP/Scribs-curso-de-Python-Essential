# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:25:50 2022

@author: grace
"""

def lista2(n):#crear una lista como resultado de una funcion
    lista=[]
    for item in range(1,n,4):
        lista.append(item)
    return lista

print(lista2(10))