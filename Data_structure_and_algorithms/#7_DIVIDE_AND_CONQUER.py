"""
Created on Wed Jul 19 12:55:40 2023
# QUICKSORT ALGORITIMI , DIVIDE AND CONQUER TAMOYILI 
@author: User rashidovj
"""

def gcd(a,b):    
    if a==0:
        return b
    if a>b:
        a,b=b,a    
    return gcd(b-a,a)

def gcd(a, b):
    if a == 0 :
        return b      
    return gcd(b%a, a)

def summa(array):
    if array == []:
        return 0
    return array[0]+summa(array[1:])


# def binarySearch(list,x):
#     l=0
#     h=len(list)-1
#     q = 1 # urinishlar soni 
#     while l<=h :
#         m=(l+h)//2
#         if list[m] == x:
#             return m , q
#         if list[m] < x :
#             l=m+1 
#             q+=1
#         else :
#             h=m-1 
#             q+=1
#     return None 

# birinchi urinish Xato return m yani har safar arrayni bulganimizga m ning qymati uzgaradi
def binaryDIVIDE1(array,x):
    l=0
    h=len(array)-1
    m=(l+h)//2

    if array[m]==x:
        return m 
    elif array[m]>x:
        h=m-1
    else :
        l=m+1
    return binaryDIVIDE1(array[l:h+1],x)

def binaryDIVIDE(array,x , l=0 , h = None):
    if h==None :
        h=len(array)-1
    if l>h:
        return None
    m=(l+h)//2

    if array[m]==x:
        return m 
    elif array[m]>x:
        return binaryDIVIDE(array, x, l, m-1)
    else :
        return binaryDIVIDE(array, x ,m+1,h)
    return None

def binarySearch(array,value,start=0,end=None):
    if end is None:
        end = len(array)-1
    if start>end:
        return None
    
    mid = (start+end)//2
    if array[mid]==value:
        return mid
    elif array[mid]>value:
        return binarySearch(array,value,start,mid-1)
    else:
        return binarySearch(array,value,mid+1,end)
    return None

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
print(binarySearch(myList,10))
print(binaryDIVIDE1(myList,10))










