# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:11:23 2022

@author: grace
"""

acl=input("Ingrese el # de ACL: ")

if acl>="1" and acl <="99": #usar "" para comparar string con string
    print("Es una ACL de tipo estándar")
elif acl>="100" and acl<="199":
    print("Es una ACL de tipo extendida")
else:
    print("No es un ACL")