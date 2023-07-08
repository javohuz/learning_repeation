"""
Created on Sat Jul  8 16:56:44 2023

linear search and binary search

@author: User rashidovj
"""

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
#  ex - 1
def linearSearch(mylist,x):
    n = 0
    for a in mylist:
        if a == x:
            return n
        n+=1
    return None

linearSearch(myList,45)

def linearSearch(list,x):
    for n in range(len(list)):
        if list[n]==x :
          return n
    return None

linearSearch(myList,44)

  # ex 2

def binarySearch(list,x):
    l=0
    h=len(list)-1
    q = 1 # urinishlar soni 
    while l<=h :
        m=(l+h)//2
        if list[m] == x:
            return m , q
        if list[m] < x :
            l=m+1 
            q+=1
        else :
            h=m-1 
            q+=1
    return None 
            
print(binarySearch(myList,1))















