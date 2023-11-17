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


""" pprint malumotlarni tartiblab konsulga chiqaradi """
from pprint import pprint
import json 

with open('bemor.json') as file:
    bemor = json.load(file)

pprint(bemor)


""" 
RegEx - ANDOZA YORDAMIDA MATN IZLASH 
re (regular expressions) moduli.
"""
import re

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

"""
So'zlarni andozaga solishtirish uchun re.match() funksiyasidan foydalanamiz.
  Agar tekshirgan so'zimiz andozaga mosh tushsa, re.match() metodi so'zni o'zini 
  qaytaradi, aks holda None qiymatini qaytaradi.
"""

"""
andozalardan matndan uzimizga kerakli emile adres yoki sana shunga uhshash malumotlarni 
sugurib olishmiz mumkun 
https://ihateregex.io/ sahifasidan esa loyihangiz uchun tayyor andozalarni topishingiz mumkin. 
"""

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

"""
Keling, yuqoridagi andoza asosida biror matndan email manzilini ajratib olamiz.
  Buning uchun re.findall() funksiyasidan foydalanamiz
"""


"""                         practice                                        """

import datetime as dt 

now = dt.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day

for n in range(13):  
    dates = dt.date( now_year , now_month , now_day)
    print(dates)
    now_day += 14
    if now_day > 30:
        now_month += 1
        now_day -= 30

    if now_month > 12:
        now_year += 1
        now_month -= 12
        
a=int(input("tug'ilgan yilingizni kiriting > "))
b=int(input("tug'ilgan oyingizni  kiriting > "))
c=int(input("tug'ilgan kuninggizni kiriting > "))
y = now_year-a
m = now_month -b
d = now_day -c
if d<=0:
    m -=1 
    d +=30
if m <= 0 :
    y-=1 
    m +=12

vaqt = dt.date( y , m , d)

print(f'tugulganizga {y} yil {m} oy {d} kun bulubdi hayotni qadriga yeting u bir marotaba beriladi ')

import re

tel_number = input('Telefon raqamingizni kiriting (998.......)  > ')
andoza = '^998.........$'

if re.match(andoza, tel_number)==None :
    print('Xato raqamingizni (998906675266) shaklda kiriting')

else :
    print('Malumot SMS tarda yuboriladi ')

string = """
Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://www.youtube.com/watch?v=vsxJPRLXpgI 
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va https://github.com/geongeorge/i-hate-regex
metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
        """

andoza1 = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
linklar = re.findall(andoza1,string)

print(linklar)





