# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:36:37 2023

@author: josea
"""

def heapx(array,n,i):
    large = i
    l = 2*i+1
    r = 2*i+2
    if l<n and array[i]<array[l]:
        large=l
    if r<n and array[large]<array[r]:
        large = r
    if large != i:
        array[i],array[large] = array[large],array[i]
        heapx(array,n,large)
        
def heap(array):
    for i in range(len(array)//2-1,-1,-1):
        heapx(array,len(array),i)
    for i in range (len(array)-1,0,-1):
        array[i],array[0]=array[0],array[i]
        heapx(array,i,0)
        
        
array=[12,12,484,2,84,5,654]
heap(array)
print(array)
    