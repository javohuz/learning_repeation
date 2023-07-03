"""
Repeation for my self 

lesson lesson 28 OOP class va obyektlar

for repiation  https://quizlet.com/812922417/oop-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""

"""                        lesson 28 class
 OOP obyektga yunaltrilgan dasturlash
"""
# https://quizlet.com/812922417/oop-flash-cards/?i=52phgt&x=1qqt

""" 
obyekt nima => obyekt bu bir nechta funksiyalar va uzgaruvchilar jamlanmasi 
class nima => class bu obyekt yaratish ycun shablon 
"""

""" 
obyekt yaratish uchun birinchi class yash kk chunki class obyekt uchun qolib 
"""

class BIO:   
    def __init__(self,name,familiya,yosh,other=None):#__init__ yzilishi kk
        self.name = name
        self.familiya= familiya
        self.yosh=yosh
        self.other= other
        
    def tanishtir(self):# buyerda self obyektni ichidagilrni uiga yukliydi
        tanishtir=f'my name is {self.name}'
        return tanishtir

    def get_tyil(self,yil):
        return yil-self.yosh
    
    
info1=BIO('Jasur','rashidov',19)
info2=BIO('Javohir','rashidov',19)
info3=BIO('Nurbek','rashidov',16)
info3.yosh
print(info1.tanishtir())
print(info2.get_tyil(2023))

"""
__init__(self,a,b,c,d)  init xsusyatlarni yozish uchun
a,b,c,d lar buyerda xsusiyatlari
self obyektning xsusiyatlariga murojat qilishimiz uchun yani self manisi uzi 
xsusiyatlarni nomini ( uzin uziga yuklash uchun )
def __init__(self) — klassga tegishli xususiyatlarni saqlovchi maxsus metod 
(funksiya). self kalit so'zi ingliz tilidan "o'zi" deb tarjima qilinadi,
  va bu klassdan yaratilgan obyektning o'ziga ishora qiladi. Ya'ni keyinchalik
  biz obyekt ichidagi metodga murojat qilganimizda shu obyektning o'zi birinchi 
  bo'lib funksiyaga argument sifatida uzatiladi, obyket ustida turli amallar
  bajarish imkonin beradi
"""

"""                 Amalyot                      """


class user:
    def __init__(self,nick,name,age,email,exemail=None):
        self.nick =nick
        self.name = name
        self.age = age
        self.email = email
        self.exemail =exemail
        
    def info(self):
        return f'foydalanivchi {self.nick}, ismi:{self.name.upper()},yoshi :{self.age},email :{self.email} , exemail : {self.exemail} '

user1 = user('javohir5266', 'javohir',19,'rashidovjavohir33@gmail.com')
user2 = user('jasur5266', 'jasur',19,'rashidovjavohir33@gmail.com')

print(user2.info())


