"""
Repeation for my self 

lesson 9 for takrorolsh aperatori

@author: javokhirdeveloper
"""

#                                       lesson 9

# for kodni takrorlash uchun ishlatiladi yani har birin bitta bitta kiritish shart mas

# mehmonlar =[ 'Ali','Vali', 'Jas', 'sinfdoshlar']

# for taklifnoma in mehmonlar :
#     print (f" {taklifnoma} , sizni tuyimizga taklif qilamiz ")

#     print (taklifnoma , 'kelmasayiz uziz bilasiz '  )

# sonlar= list(range(1,11))
# sonlar_kubi =[]
# for son in sonlar : 
#     print (son, "^2=" , son**2)

#     sonlar_kubi.append(son**3)


# dostlar =[]
# for n in range(4) :
#     dostlar.append(input(f"{n+1} - dostingizni ismini kiriting\n ....  ").title())

# print ( dostlar)



#                                       Amalyot -> 9


# """
# 19/11/2020

# Dasturlash asoslari

# #09-dars: for loops

# Muallif: Anvar Narzullaev

# Web sahifa: https://python.sariq.dev
# """
# # Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# # va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['Ali','Vali','Hasan','Husan','Olim']
# for ism in ismlar:
#     print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# # Yuoqirdagi tsikl tugaganidan so'ng, 
# # ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# # (n o'rniga kod necha marta takrorlanganini yozing)
# print(f"Kod {len(ismlar)} marta takrorlandi")

# # 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# # Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)

# # Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# # va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)    

# # Foydalanuvchidan bugun nechta odam bilan 
# # uchrashganini (suhbatlashganini) so'rang, 
# # va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)