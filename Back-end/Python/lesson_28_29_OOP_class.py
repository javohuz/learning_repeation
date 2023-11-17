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


"""                 lesson 29 obyektlar                         """

""" qiymatlarni (smt.yosh) yuli bn chaqirish mumkun lekin bu tafsiya qilinmaydi bu 
faqat python tiliga mos ularni chaqirish uchun alohida metod chaqirish kk 
"""

class BIO:   
    def __init__(self,name,familiya,yosh):#__init__ yzilishi kk
        self.name = name
        self.familiya= familiya
        self.yosh=yosh
        self.bosqich = 1  # standard qiymat
        
    def tanishtir(self):# buyerda self obyektni ichidagilrni uiga yukliydi
        tanishtir=f'my name is {self.name}'
        return tanishtir
    
    def set_bosqish(self,new_bosqich):
        """ set_smt bu hsusiyatni uzgartrish uchun """
        self.bosqich=new_bosqich
    
    def get_name(self):
        """get_smt bu kk li hsusiyatni chaqrib olish uchun """
        return self.name
    def get_fullname(self):
        return f'{self.name} , {self.familiya}'
    
    def  update_bosqich(self):
        """ update_smt bu qandaydir amal bajaradi yoki update qiladigan """
        self.bosqich += 1
    
    def get_yosh(self):
        return self.yosh
        
"""
get_smt , set_smt , update_smt => bular shunchaki nom yuqoridagi vazifalarni 
bajarayotganda shulardan foydalanish tafya qilinadi
"""

info1=BIO('Jasur','rashidov',19)
info2=BIO('Javohir','rashidov',19)
info3=BIO('Nurbek','rashidov',16)

info3.get_name()
info2.get_yosh()

info3.update_bosqich()

info2.set_bosqish(3)
info3.bosqich

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar = []
        self.talaba_soni = 0

    def add_talaba(self,talaba):
        """talaba qushish """
        self.talabalar.append(talaba)
        self.talaba_soni += 1 
        
    def get_talaba(self):
        # talaba_name =[]
        # for talaba in self.talabalar:
        #     talaba_name.append(talaba.get_fullname().title())
        # return talaba_name
        return [talaba.get_fullname().title() for talaba in self.talabalar ]
    

matem = Fan('Matematika')
matem.add_talaba(info1)
matem.add_talaba(info2)
matem.get_talaba()

"""
dir() FUNKSIYASI
dir() funksiyasi yordamida istalgan obyekt yoki klassning xususiyatlari va 
metodlarini ko'rib olishimiz mumkin:
"""
dir(BIO)

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(BIO),dir(BIO))

"""                         amalyot                     """

class Avto():
    def __init__(self, model, rang, karobka ,narx ):
        self.model =model
        self.rang =rang
        self.karobka = karobka
        self.narx=narx
        self.kilometr = 0
    
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_karobka(self):
        return self.karobka
    
    def get_narx(self):
        return self.narx
    
    def set_kilometr(self,kilometri):
        self.kilometr = kilometri
        
    def update_narx(self,foizi):
        """avtomobil narxi % uzgarganini hisoblaydi agar kamaygan bulsa (-) ishora bilan yozing"""
        self.narx += self.narx*foizi/100
    
    def get_avto_info(self):
        return f' Modeli : {self.model.title()} \n Rangi : {self.rang} \n Karobkasi : {self.karobka} \n Narxi : {self.narx} \n Yurilgan kilometri : {self.kilometr} '

avto1 = Avto('jentra','oq','mexanik',15000)
avto2 = Avto('jentra','qora','mexanik',15000)
avto3 = Avto('jentra','qora','avtomat',17000)
avto4 = Avto('jentra','qora','avtomat',17000)
avto5 = Avto('jentra','qora','avtomat',17000)
avto6 = Avto('jentra','qora','avtomat',17000)
avto7 = Avto('jentra','qora','avtomat',17000)
avto8 = Avto('jentra','qora','avtomat',17000)
avto9 = Avto('jentra','qora','avtomat',17000)

avto1.get_narx()
avto2.update_narx(-10)
avto2.get_narx()
avto1.set_kilometr(5000)
print(avto1.get_avto_info())

class Avtosalon():
    def __init__(self,salon_nomi , salon_manzili , avtamobillari  ):
        self.salon_nomi =salon_nomi
        self.salon_manzili = salon_manzili
        self.avtamobillari = [avtamobillari]
    
    def add_car(self, new_car):
        return self.avtamobillari.append(new_car) 
    
    def get_cars(self):
        return self.avtamobillari
    
    def get_info(self):
        car_list = [ car_info.get_avto_info() for car_info in self.avtamobillari ]
        n=len(car_list)+1
        info = []
        while car_list : 
            n-=1
            x= f'     car{n} \n{car_list.pop()}'
            info.append(x)
        return info
            
avto6.update_narx(50)
salon1 = Avtosalon('GM', 'Andijon', avto1)
salon1.add_car(avto2)
salon1.add_car(avto3)
salon1.add_car(avto4)
salon1.add_car(avto5)
salon1.add_car(avto6)
salon1.add_car(avto7)
salon1.add_car(avto8)
salon1.add_car(avto9)


for x in salon1.get_info():
    print(x)

print(dir(Avto),'\n',dir(Avtosalon),Avto.__dict__)

