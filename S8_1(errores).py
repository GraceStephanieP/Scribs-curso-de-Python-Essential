# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:49:33 2022

@author: grace

"""

try:
    print("1")
    x=1/0#error
    print("2")#no se mostraría 2 si hay error, lo salta
except:
    print("Sorry")
print("3")