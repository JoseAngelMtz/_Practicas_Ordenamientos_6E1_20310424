# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:13:32 2023

@author: josea
"""
def shell (array):
    n= len(array)
    gap = n/2
    gap = int(gap)
    print(gap)
    while gap>0:
        for i in range(gap,n):
            temp = array[i]
            j=i
            while j>= gap and array[j-gap]>temp:
                array[j]=array[j-gap]
                j -= gap
            array[j]=temp
        gap /=2
        gap = int(gap)

array=[15,5,-9,489,94,81,8,10]

shell(array)
print(array)
    