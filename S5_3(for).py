# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:34:33 2022

@author: grace
"""

lista2=[]
lista=["R1","R2","R3","R4","S1","S2"]
for item in lista:
    if "S" in item:
        lista2.append(item)
print(lista2)