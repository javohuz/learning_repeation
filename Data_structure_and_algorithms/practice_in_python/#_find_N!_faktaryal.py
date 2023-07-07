# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:08:08 2023
need to find N!

1 : start , create N , i 
2 : create N , i = qiymatni yuklash uchun 
3 : N=1 , i=1 
4 : N  ga qiymat qabul qilamiz 
5 : N=i bulgunga qadar takrorlanuvchi kod yozamiz 
    N=N*i
    i = i+1
6 : N qiymatni qaytar
7 : stop
@author: rashidovj
"""

def faktoryal(n):
    
    i=1
    N=n
    while n!=i :
        N=N*i
        i += 1
    return N

print(faktoryal(5))


def faktorial(N):
    i=1
    fakt=1
    while i!=N+1:
        fakt = fakt*i        
        i += 1
    return fakt

print(faktorial(5))


