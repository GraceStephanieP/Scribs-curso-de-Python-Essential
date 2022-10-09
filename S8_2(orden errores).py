# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:26:31 2022

@author: grace
"""

try:
    y=1/0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

    
print ("The end")
