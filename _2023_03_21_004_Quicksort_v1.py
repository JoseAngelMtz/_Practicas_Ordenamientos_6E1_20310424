# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:04:33 2023

@author: josea
"""

def particion (array,low,high):
    pivot = array[high]
    i = low -1
    for j in range(low,high):
        if array[j] <=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]= array[high],array[i+1]
    return i+1
def quick(array,low,high):
    if low<high:
        pi = particion(array,low,high)
        quick(array,low,pi-1)
        quick(array,pi+1,high)
        
listax=[12,-5,5,4,21,88,77,464]

quick(listax,0,len(listax)-1)
print(listax)