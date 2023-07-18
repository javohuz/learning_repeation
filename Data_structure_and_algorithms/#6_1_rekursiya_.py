"""
Created on Tue Jul 11 18:53:51 2023
<<<<<<< HEAD
rekursiya
=======
rekursiya 
>>>>>>> 8b05ae4f7764cd56630ed814b8e29aaf029015be
@author: User rashidovj
"""
            
def sana(n):
    print(n)
    if n<=1:
        return 
    else :
        sana(n-1)

    
print(sana(8))

def find_faktaryal(a):
    if a<=1 :
        return 1
    else :
        return a*find_faktaryal(a-1)
        


print(find_faktaryal(5))











