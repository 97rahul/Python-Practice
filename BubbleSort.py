# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:00:44 2022

@author: tom97
"""

def BubbleSort(array):
    
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    return array

arr = [10, 7, 8, 9, 1, 5]

x = BubbleSort(arr)
print(x)
 