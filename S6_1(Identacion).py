# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:10:54 2022

@author: grace
"""


while True:
    x=input("Enter a number to count to: ")
    if x =='q' or x == 'quit':
        break


    x=int(x)
    y=1
    
    while True:
        print(y)
        y=y+1
        if y>x:
            break
