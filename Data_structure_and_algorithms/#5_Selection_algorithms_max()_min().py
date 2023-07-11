"""
Created on Tue Jul 11 16:53:51 2023

Aim is create max() and min() function 

@author: User rashidovj
"""

def max_index(array):
    """ find max index  """
    index = 0
    max_q = array[0]
    for n in range(1,len(array)):
        if array[n] > max_q:
            max_q = array[n]
            index=n
    return index

def min_index(array):
    """ find min index """
    index = 0
    max_q = array[0]
    for n in range(1,len(array)):
        if array[n] < max_q:
            max_q = array[n]
            index=n
    return index

def max0(array):
    """ find max """
    index = 0
    max_q = array[0]
    for n in range(1,len(array)):
        if array[n] > max_q :
            max_q = array[n]
            index=n
    return array[index]

def min0(array):
    """ find min """
    index = 0
    max_q = array[0]
    for n in range(1,len(array)):
        if array[n]<max_q:
            max_q = array[n]
            index=n
    return array[index]

def sum0(array):
    "find summed up "
    s=0
    for a in array:
        s += a
    return s

a = [ 9 , 33 , 62 , 923 , 12 , 64]

print(min0(a))
print(min_index(a))
print(max_index(a))
print(max0(a))
print(sum0(a))

