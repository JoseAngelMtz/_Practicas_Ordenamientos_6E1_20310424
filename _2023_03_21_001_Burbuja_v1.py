# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:20:55 2023

@author: josea
"""

def bubble(listax):
    change = True
    while change:
        change = False
        for i in range(len(listax)-1):
            if listax[i] > listax[i+1]:
                listax[i] , listax[i+1] = listax[i+1] , listax[i]
                change = True
                

listanum = [10,20,80,5,7,51,4]
bubble(listanum)
print(listanum)