"""
Repeation for my self 

lesson lesson 23 , 24 module , lambda

for repiation  https://quizlet.com/_dfgct2?x=1qqt&i=52phgt

@author: rashidovj
"""
"""
                          lesson 23  modullar
"""
"""
Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida
  yashirishimiz va kerak bo'lgan murojat qilishimiz mumkinligida. Maqsadimiz
  dasturimizni ixcham va tushunarli qilib, kelajakda o'zimiz yoki boshqalar 
  uchun ham "toza" kod qoldrisih. Bu yo'nalishda yana bir qadam qo'yib, 
  dasturimizni modullarga ajratimshimiz mumkin. 
"""
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")    
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")

"""
import bu 1- fayldagi kodni 2-chisiga imposrt qilish uchun use buning uchun 
ikala kod yozilgan fayllar bitta papkani ichiki bulishi kk
""" 
import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_info_mod.info_print(avto1)
"""
import smt as smt funksiya nomini har doim yozib yotish shart emas uni boshqa nomga birlashtrsa buladi
"""

import avto_info_mod as aim
avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)

"""
modulni ichidagi functions ni asosiy koodga kuchirib oslish
"""

from avto_info_mod import avto_info, avto_kirit ,info_print
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)

"""
agar funksiya nomini kodda yana ishlatadigan bulsak finction nomi uzgartrish can
"""
from avto_info_mod import avto_info as ai , avto_kirit as ak , info_print as ip
avto1 = ai("GM", "Malibu", "Qora", "avtomat", 2020,40000)
ip(avto1)


"""
* modul ichidagi functions ni bitta chiqarim oladi lekin bu kichik modullar uchun 
katto modullarda hamma funksiyalar kup bulishi umkun bu esa dastur sekin 
ishlashi yoki birxil nomli uzgaruvchilar hosil bulib dasturn hato ishlashi mumkun 
"""

from avto_info_mod import *
avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_info_mod.info_print(avto1)

"""
python tayyor modullar ruyhati => https://docs.python.org/3/py-modindex.html
  foydali modullar
"""
import math 
print(math.pow(3,4))
print(math.sin(0.5))
print(math.sqrt(100))


import random  as r

randint(a,b)  # rendit  a va b oralig'ida tasodifiy son
son = r.randint(0,100) 
print(son)

"""
choice(list) list ichidan rendomly tanlaydi
"""
sonlar =list(range(2,30,2))
x = r.choice(sonlar)   
print(x)

"""
shuffle(x) x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya
listni mixed qiladi
"""

x = list(range(11))
print(x)
r.shuffle(x)
print(x)
"""
sample(population, k) => population ruyhatdan k ta sini tanlab oladi list shaklida 
sonlar = r.sample(range(1000),10 )
"""
print(sonlar)

"""                             lesson 24 nomsiz funksiya

"""
"""
lambda =>Pythonning o'ziga xos xususiyatlaridan biri, nomsiz vaqtinchalik
funksiyalar yaratish imkoniyati. Bunday funksiyalarni yaratishda def
operatori o'rniga lambda operatori ishlatilgani uchun ham lambda funskiyalar
deb ataladi
"""

x = int(input("any numcer = "))
son = lambda x : x**2  # nomsiz funktsiyaga nom berdik 
print(son(x))

"""
funktiya yasovchi funksiya
"""
def any_numbers (n ):
    return lambda x :x**n

son = any_numbers(2)
son (8)
"""
  map() FUNKSIYASI =>Bu funksiya argument sifatida ro'yxat (yoki lug'at) va
boshqa bir funksiyani qabul qilib, ro'yxat elementlariga qabul qilingan
funksya yordamida ishlov beradi
map(a,b) a biron funksiya b list or dict , list or dict ni qiymatini a ga junatadi
"""
sonlar=list(range(10))
son_kvadrati = list(map(lambda x :x**2 , sonlar))
print(sonlar)
print(son_kvadrati)

from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x
print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz
"""
map funksiyasi orqali bir nechta qiymatalr junatish
"""
a = list(range(5))
b = list(range(6,11))
print(a,'\n',b)
print(list(map(lambda x,y : x*y , a , b)))

"""
map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:
ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda take :take.upper(),ismlar)))
"""
"""
filter(a,b) funksiyasi map() ga uhshiydi a funksiya bilan b ni tekshiradi
true bulda yoki a funk ni qanoatlantirsa qabul qiladi else unkazmakdi
"""
import random  as r
sonlar = r.sample(range(1000),10 )
print(sonlar)

def juft(n):
    return n%2==0

juft_sonlar = list(filter(juft,sonlar))
print(juft_sonlar)

juft_sonlar = list(filter(lambda n:n%2==0,sonlar))
print(juft_sonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda matn : matn.startswith('o'),mevalar))
print(mevalar_b)

"""
.startswith(smt) smt qandaydir harf agat matn smt bn boshlangan bulsa 
True qiymat qaytaradi else False
"""