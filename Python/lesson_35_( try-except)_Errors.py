"""
Repeation for my self 

lesson 35 xatolar bn ishlash try - except operatorlari

for repiation  https://quizlet.com/814130384/hatolar-bn-ishlash-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""
       
"""                              lesson 35                                 """

"""
pythonda kod xato bulganda yoki malumot qabul qilganda turli xil xatoliklar kelib 
chiqishi mumkum misol uchun Run time error yoki shunga uhshash bu vaqtta dastur 
ishlashdan tuhtaydi  buning oldini olish uchun try: except: else : operatorlaridan 
foydalaniladi  
"""

yosh = input('yoshingizni kiriting >> ')
yosh = int(yosh)
try :  
    yosh = int(yosh) 

except:
    print('siz butun son kiritmadingiz ')
    
else :  
    print(f'siz {2023-yosh} yilda tugilgansiz ')
        
""" try : => manosi harakat qil yani xatolik yuzaga kelishi mumkun bulgan kod yoziladi 
    except : => agar try ichidagi kodda xatolik bulsa except ichidaki kod bajarildi
    yana except KeyError : yani expect ichida kelib chiqadigan xatolikni nomini ham yozish 
    mumkun bu holda except faqat kiritilgan xatolik bulganda bajarildi
    else: => yani agar xatolik bulmasa else : ichidagi kod bajarildi 
    
buning qulay tomini agar xatolik bulsa ham dasturn tuhtab qolmaydi yani 
xato bulgan kodlar pastidagi kodlar bajarila veradi 
"""

"""
bir nechta xatolar bn ishlash try-except ketma-ketligida bir nechta except
 operatorlari ham bo'lishi mumkin. Ularning har biri ma'lum turdagi xatolik uchun 
 javobgar bo'ladi:
"""
n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError: # agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lib bo'lmaydi")
else:
    print(f"x={x}")
        
        
""" pass operatori => Hech qanday ma'lumot ko'rsatmay, dasturni davom etish uchun
 pass operatoridan foydalanamiz.
"""  
yosh = input('yoshingizni kiriting >> ')

try :  
    yosh = int(yosh) 
except:
    pass      
else :  
    print(f'siz {2023-yosh} yilda tugilgansiz ')
            
"""
agar xatolikni oldini oshin mumkun bulsa (while , if ..) xatolikni oldini olygan yaxshiroq buladi   
"""       
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break        
print(f"Siz {2021-yosh} yilda tug'ilgansiz") 
