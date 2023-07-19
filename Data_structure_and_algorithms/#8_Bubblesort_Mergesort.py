# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:55:40 2023
# 8 quicksort, Bubblesort , Mergesort algorithms 
@author: User
"""

from random import randrange
def qsortTrue(array):
    if len(array)<2:
        return array
    value = array.pop(randrange(len(array)))
    big = [a for a in array if a>=value]
    low = [a for a in array if a<value]
    return qsortTrue(low)+[value]+qsortTrue(big)
 
def qsortFalse(array):
    if len(array)<2:
        return array
    value = array.pop(randrange(len(array)))
    big = [a for a in array if a>=value]
    low = [a for a in array if a<value]
    return qsortFalse(big)+[value]+qsortFalse(low)

def bubblesort(array):
    n= len(array)
    for a in range(n):
        for b in range(0,n-a-1):
            if array[b]>array[b+1]:
                array[b],array[b+1]=array[b+1],array[b]
    return array

def mergeSort(arr):
	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2
		# Dividing the array elements
		L = arr[:mid]
		# into 2 halves
		R = arr[mid:]
		# Sorting the first half
		mergeSort(L)
		# Sorting the second half
		mergeSort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
            
arr = [64, 34, 25, 12, 22, 11, 90]
    
print(bubblesort(arr),sorted(arr))
    
    
    
    

    
    
    
    
    
    