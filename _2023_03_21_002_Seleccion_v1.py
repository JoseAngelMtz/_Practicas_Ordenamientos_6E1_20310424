# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:48:54 2023

@author: josea
"""

def selct(listax):
    for i in range(len(listax)):
        low = i
        for j in range(i + 1 , len(listax)):
            if listax[j] < listax[low]:
                low = j
                
        listax[i] , listax[low] = listax[low] , listax[i]
        
listanum = [1,184,1,81,585,55,42,10,10]
selct(listanum)
print(listanum)