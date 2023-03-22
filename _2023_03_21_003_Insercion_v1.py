# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:04:30 2023

@author: josea
"""

def insert(listax):
    for i in range(1,len(listax)):
        ins = listax[i]
        j = i -1
        while j >= 0 and listax[j] > ins:
            listax[j + 1] = listax[j]
            j -= 1
        listax[j + 1] = ins
listanum = [61,15,34,2,42,3,80,4]
insert(listanum)
print(listanum)