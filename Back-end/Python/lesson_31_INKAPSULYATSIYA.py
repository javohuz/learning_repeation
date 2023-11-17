"""
Repeation for my self 

lesson lesson 31 INKAPSULYATSIYA

for repiation  https://quizlet.com/812922417/oop-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""
"""                          lesson 31 
INKAPSULYATSIYA
Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya
  ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat 
  qilishni va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda 
  bunday yopiq xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi: 
"""
""" uuid  moduli ning uuid4 funksyasi orqali id raqam olish mumkun id raqam har
  doim turlicha buladi from uuid import uuid4
"""
""" klaslarning yana qulayliklaridan biri uzgarmas xsusiyatlar qushishimiz 
mumkun yani __init__ qilib hsusiyat qushmasdan uzgarmasni __init__dan oldin 
yozishimiz kerak """

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __number_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__number_avto +=1
        
"""yuqpridi Avto,number_avto +=1 har safar classdan foydalanganda 1 qushadi"""
 
    def add_km(self,km):
        if km >= 0:
            self.__km + km
        else :
            print('avtomobil km ni kamaytrib bumaydi')
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    @classmethod
    def get_num_avto(cls):
        return cls.__number_avto 
    
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
print(Avto.get_num_avto())


""" class larni modul qilish huddi funksiyaday amalga oshiriladi faqat class  
nomi bn chaqiriladi """ 



"""                          amalyot                                        """


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __shaxs_soni = 0
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__shaxs_soni +=1 
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
    
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    @classmethod
    def get_Shaxs_num(cls):
        return cls.__shaxs_soni
        
talaba1 = Shaxs('Javohir','Rashidov','AD0056845',2004)
talaba1.get_Shaxs_num()