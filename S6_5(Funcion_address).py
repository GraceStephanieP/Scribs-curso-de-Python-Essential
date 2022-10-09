# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:26:17 2022

@author: grace
"""

def address(street,city,postalCode):
    print("Your address is:",street,"St.,",city,postalCode)

s=input("Street: ")
pC=input("Postal Code: ")
c=input("City: ")

address(s,c,pC)