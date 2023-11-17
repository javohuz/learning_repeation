"""
Repeation for my self 

lesson lesson 32 DUNDER MEDOTLARI

for repiation  https://quizlet.com/813290538/dunder-metodlari-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""

"""                          lesson 32                              """

"""MAXSUS METODLAR    double underscore yoki qisqa qilib dunder 
Dunder metolar yordamida obyektlarga qo'shimcha qulayliklar va vazifalar 
qo'shishimiz mumkin. Klass yoki obyektga oid dunder metodlar ro'yxatini ko'rish
uchun dir() funksiyasidan foydalanamiz:
"""
"""
__init__ Bu metod klassdan obyekt yaratishda chaqiriladi va obyektning 
xususiyatlarini belgilaydi
"""

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narh
        Avto.__num_avto += 1
        
""" __str__ dunder motodi bu metod orqali obyektni biz hohlhlagandek chaqiradi 
yani obyektga murojan qilganimizda biz kititgan kodni qaytaradi """

    def __str__(self):
        return f"Avto : {self.make} , {self.model} "
    
    def __repr__(self):
        """ obyekt haqida malumot qaytaradi """
        return f"Avto : {self.make} , {self.model} "

avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1)

""" yani oldin obyektga mirojat qilganimizda mana bunday mal qaytarardi 
<__main__.Avto object at 0x00000277A4127610> , endi , obyektga mirojat qilsak 
Avto : GM , Malibu """
__str__ == __repr__ ikalasni vazifasi bir lekin __repr__ tavsiya qilinadi
murojat qilish uchun print() yoki str(object) agar __repr__ bulsa repr(object) deb

  """ taqqoslash metodlari ular oltita yani hammasni >= == ... 
x.__lt__(self,y)  =>  x<y
x.__le__(self,y)  =>  x<=y
x.__gt__(self,y)  =>  x>y
x.__ge__(self,y)  =>  x>=y
x.__eq__(self,y)  =>  x==y
x.__ne__(self,y)  =>  x!=y

lekin kodda ularni  armini yozish kifoya 
yani < ekanligini bilsa > ni ham biladi teskarisini oladi """

    def __eq__(self,y):
        return self.narx == y.narx
    
    def __gt__(self,y):
        return self.narx > y.narx
    
    def __ge__(self,y):
        return self.narx >= y.narx

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
print(avto1<avto2)

""" new matod obyektni klassga tegishli yoki yuligini tekshiradi 
isinstance(obyekt,class) 
isinstance(avto1, Avto) """

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index] =qiymat

    def add_avto(self,*qiymat):
        for avto in qiymat :
            if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")
            
    def __call__(self,*new_info):
        if new_info:
            for avto in new_info:
                self.avtolar.append(avto)
                
        return [avto for avto in self.avtolar]
       
    def __add__(self,y):
        if isinstance(y,AvtoSalon):
            new_one = AvtoSalon(f" {self.name} {y.name}")
            new_one.avtolar = self.avtolar + y.avtolar
            return new_one
        elif isinstance(y,Avto ):
              self.avtolar.append(y)
            
            
salon1 = AvtoSalon("GM")
# Avto obyektlarini yaratamiz
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

salon1.add_avto(avto1 , avto2 )
salon1[:]

salon1[1]=avto3
len(salon1)
# salon1(avto4 , avto5 , avto6)
salon2=AvtoSalon('BMW')
salon2(avto4 , avto5 , avto6)
salon3 = salon1+salon2
print(salon3,salon3())

"""
__getitem__ bu lugat bulsa ushani index qiymati kritilsa natijani chiqaradi 
__setitem__ index qiymati kiritilganda usha indexlini uzgartasa buladi
__len__  len() metodi ishlatilganda __len__ ichidagi kodni chiqaradi
__repr__ obyektga mirojat qilganda biz hohlagan malumotni chiqaradi or __str__
__call__ obyektni chaqiradigan yani salon1() qilganda malum bir funksiya 
bajaradigan yoki biz hohlagan matnni qaytaradigan qilishimiz mumkun 

Mat amallar bajarish metodlarin 
__add__ ==> ( + )
__sub__ ==> ( - )
__mul__ ==> ( * )
__div__ ==> ( : )
__pow__ ==> ( ** )
"""

"""                              Amalyot                         """



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

    def __repr__(self):
        return f"{self.ism} ismli shaxs"


class Talaba(Shaxs): 
    def __init__(self ,ism, familiya, pasport , tyil , idraqam ,fanlar):
        """Talaba haqida malumot """
        super().__init__(ism,familiya,pasport,tyil) 
        self.idraqam = idraqam
        self.bosqich = 1 
        self.fanlar = []
        
    def get_id(self):
        return self.idraqam
    
    def get_passport(self):
        return self.passport
    
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
    
    def __eq__(self,y):
        return self.bosqich == y.bosqich
    
    def __lt__(self,y):
        return  self.bosqich < y.bosqich
    

class Fan:
    def __init__(self,name_fan):
        self.name_fan = name_fan
        self.talabalar = []

    def add_talaba (self,*talabalar):
        for talaba in talabalar :
            self.talabalar.append(talaba)
    
    def __repr__(self):
        return self.name_fan
    
    def __call__(self,*y):
        for c in y :
            if isinstance(c,Talaba):
                self.talabalar.append(c)
        return self.talabalar
    
    def __getitem__(self,index):
        return self.talabalar[index]
    
    def __setitem__(self,index,new_one):
        self.talabalar[index]=new_one
    
    def __len__(self):
        return len(self.talabalar)
    
    def __add__(self,y):
        if isinstance(y,Talaba):
            return self.talabalar.append(y)
        elif isinstance(y,Fan):
            new_fan = Fan(f"{self.name_fan} va {y.name_fan}")
            new_fan.talabalar = self.talabalar + y.talabalar
            return new_fan
   
    def __sub__(self,y):

        if isinstance(y,Talaba):
            return self.talabalar.remove(y)
        
        else :
            for talaba in self.talabalar :
                if talaba.get_id() == y or talaba.get_passport() ==y :
                    return self.talabalar.remove(talaba)
            
        
shaxs1 = Shaxs('Javohir',"Rashidov","AD4324686",2004)
talaba1 = Talaba('Javohir',"Rashidov","AD4324646",2004,"AD6726773","matem")
talaba2 = Talaba('Jasur',"Rashidov","AD4324686",2004,"AD6726773","matem")
print(talaba1==talaba2)
talaba2.set_bosqich(4)
print(talaba1<talaba2)
                
fan1 = Fan("Matem")
fan1.add_talaba(talaba1)
fan2 = Fan ('fizika')
fan1(talaba2)
fan1[1] = talaba1
fan1[1]
len(fan1)


fan1+talaba2
fan2+talaba1

fan3 = fan1+fan2
fan3()
fan3-'AD6726773'
fan3()
