"""
Repeation for my self 

lesson lesson 30 vorislar va polimorfizm 

for repiation  https://quizlet.com/812922417/oop-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""


"""                         lesson 30                         

vorislik va polimorfizm => vorislik bu otak class or( super class ) dan yaratilgan 
yangi class polimorfizm bu yangi classda sper klassning funksiyalarni uzgartrish 
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
""" Voris yasash """

class Talaba(Shaxs): # shaxs ni metodlarini meros qil
    def __init__(self ,ism, familiya, pasport , tyil , idraqam , manzil):
        """Talaba haqida malumot """
        super().__init__(ism,familiya,pasport,tyil) 
        self.idraqam = idraqam
        self.bosqich = 1 
        self.manzil = manzil
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def set_bosqich(self,new_corse):
        self.bosqich = new_corse

# """ polimorifzm yani super fazadagi metodni uzgartiramiz shu """
        
    def get_info(self): 
        """Talava haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Bpsqich:{self.bosqich} , ID_raqam: {self.idraqam}"
        return info
    
        
""" buyerda Talaba voris ,Shaxs super class , super() => vazifasi super classdan 
__init__ ichida kiritilgan qiymatlarni super classdan meros qiladi va super class
ning metodlari voris klacda ham ishlaydi
Yana istalgan class boshqa class uchun super class bulishi mumkun 
Birvaqqtda bitta klasda 2 ta super class ni voris qilish mumkun faqat kod
murakkablashadi bu usul unchalik tavsiya qilinmaydi
"""

""" bazida classning xsusiyatlari kupayib ketishi mumkun bu xatalikka yoki 
noqulaylikka olib kelishi mumkun bu hollarda yangi class yaratib u klasning 
malumotlarini boshqa klacda foydalanish mumkun 
"""
# Talaba klasiga manzil degan xsusiyat qushdik 
class Manzil:
    def __init__(self,uy,kuchasi,tuman,viloyat):
        self.uy=uy
        self.kuchasi = kuchasi
        self.tuman = tuman 
        self.viloyat =viloyat
    
    def get_manzil(self):
        manzil= f'{self.uy}-Uy , Ko\'chasi : {self.kuchasi} ,'
        manzil += f"Tumani : {self.tuman} , Vilayati : {self.viloyat}"
        return manzil

talaba1_manzil= Manzil(17 ,'Zamondosh','SHahrizabz','Qashqadaryo' )
talaba1 = Talaba('Javohir','Rashidov','AD0056845',2004,'N00011251',talaba1_manzil)
talaba1.manzil.get_manzil()


"""                     Amalyot                             """


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs): 
    def __init__(self ,ism, familiya, pasport , tyil , idraqam ,fanlar):
        """Talaba haqida malumot """
        super().__init__(ism,familiya,pasport,tyil) 
        self.idraqam = idraqam
        self.bosqich = 1 
        self.fanlar = []
        
    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def set_bosqich(self,new_corse):
        self.bosqich = new_corse
        
    def get_info(self): 
        """Talava haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Bpsqich:{self.bosqich} , ID_raqam: {self.idraqam}"
        return info
    
    def fanga_yozil(self,fan):
        return self.fanlar.append(fan)
    
    def remove_fan(self,x_fan):
        if x_fan not in self.fanlar :
            natija= f'Siz {x_fan} faniga yozilmagansiz ' 
        else :
            natija=self.fanlar.remove(x_fan) 
        return natija
    
class Fan():
    
    def __init__(self,fan):
        self.fan = fan
        
    def get_fan(self):
        return self.fan
    
    
fan1 = Fan('Matematika')
fan2 = Fan('Fizika')
talaba1 = Talaba('Javohir','Rashidov','AD0056845',2004,'N00011251',"fanlar")

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)

talaba1.remove_fan(fan1)
print(talaba1.fanlar)

class User(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
    def get_info(self): 
        """Talava haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"ID_raqami: {self.idraqam}"
        return info
    
user1 = User('Javohir','Rashidov','ND15641540',2004,323211112200)
user1.get_info()

class Admin(User):
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        super().__init__(ism,familiya,passport,tyil,idraqam)
    
    def ban_user(self,user_name):
        return f'{user_name} bloklandi'
    
user2 = Admin('Javohir','Rashidov','ND15641540',2004,323211112200)
user2.ban_user('Javohir')























