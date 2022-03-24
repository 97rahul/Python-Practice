# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:04:58 2022

@author: tom97
"""

def partition(arr,low,high):
    
    i = low -1
    pivot = arr[high]
    
    for j in range(low,high):
            
        if arr[j]<pivot:
                
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
                
    arr[i+1],arr[high] = arr[high],arr[i+1]
        
    return i+1
    
    
def QuickSort(arr,low,high):
    
    if len(arr) == 1:
        return arr
    
    if low < high:
        
        p = partition(arr,low,high)
        QuickSort(arr,low,p-1)
        QuickSort(arr,p+1,high)
        
        
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
QuickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i],end = ' ')
            