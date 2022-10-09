# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:31:01 2022
@author: grace
"""

dict1={"R1":"10.0.0.1",
       "R2":"10.0.0.2",
       5100:"JUAN CARLOS",
       "EMAIL":"jdominguez@epn.edu.ec",
       "Age":50,
       "Value":False}

print("\n"*1)
print(dict1)
print(type(dict1))
print(len(dict1))
print(dict1["R1"])
print(dict1[5100])
print(dict1["EMAIL"])
dict1["S1"]="11.0.0.1"
dict1[5]=56.1

print("R3" in dict1) #existe R3 en el diccionario?
print("S1" in dict1) #existe S1 en el diccionario?