"""
Repeation for my self 

lesson 38 python library 

for repiation  

@author: rashidovj
"""

"""                             lesson 38                                   """
    
""" datetime Ushbu modul yordamida Pythonda sanalar bilan ishlashimiz mumkin"""
    
import datetime as dt 

hozir = dt.datetime.now()

"""agar kerakli vaqt kiritish kk bulsa qulda kiritamiz """
ertaga = dt.date(2023,7,27)

# print(hozir , ertaga)     
 
print(hozir.date() , hozir.time()) 

""" 
dt.date.today() => agar faqat hozirgi kun kerak bulsa 
dt.date.now()  => hozirgi vaqtni kun soat min sec ml sek bn chiqaradi 
"""

qoldi = ertaga-hozir.date()
# print(qoldi.days)

aksiya = dt.datetime(2023,7,16,16,59,00,00)
qoldi1= aksiya-hozir

secondlar = qoldi1.seconds
minutlar = int(secondlar/60)

# print(minutlar)
print(hozir.time())

""" chala secundamer for 59 seconds """
n= hozir.second
while aksiya != hozir :
    hozir = dt.datetime.now()
    qoldi = aksiya -hozir
    if  hozir.second > n :
        n = hozir.second
        print(qoldi)
    else:
        pass













