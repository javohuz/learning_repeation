"""
Repeation for my self 

lesson lesson 19 funksiyalar

for repiation  https://quizlet.com/_dfgct2?x=1qqt&i=52phgt

@author: rashidovj
"""
# funksiya bu ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
# misol uchun print() va range() funksiyasi

# salom beruvchi funksiya

# # def funksiya yasash uchun foydalaniladi 

# def salom_ber():  # salom_ber() -> function name (v)
#     """salob beradigan function """ # => info 
#     print("Assalomu alaykum ") # funksiya bajaradigan vazifa code

# salom_ber()


# def salom_ber(ism): # ism == parametr
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('Javohir') # javohi == argument
# salom_ber('Jasur')  # jasur == argunet
# print(salom_ber.__doc__)


# DOCSTRING funksiya haqida malumot => print(smt.__doc__)
# funksiya haqida malumotni bulish uchun uning nomi va ( ochsak chiqadi 

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")


# toliq_ism('javohir' , 'Rashiov')
# # kalit usuli 
# toliq_ism(familiya='Rashidov',ism='javohir')

# STANDART QIYMAT
# def yosh_hisobla(tugilgan_yil, joriy_yil=2023): # = 2023 => standart qiymat
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# yosh_hisobla(2004 ,2023)
# yosh_hisobla(2004)

#                                   amalyot

# def ism_yosh_aniqla(ism,yili):
#     """ ism va yoshni aniqlaydigan function """
#     print(f'{ism.title()}ning yoshingiz {2023-yili} yoshdasiz')

# ism = input("ismingizni kiriting >>")
# yil = input("tugulgan yilingizni kiriting >> ") 
# ism_yosh_aniqla(ism, int(yil)) 

# def qiymat_top(son1,son2):
#     """ Sonning katta sonni topib beruvchi function """
    
#     if son1 > son2 :
#         son = son1 
#     elif son1==son2 :
#         son = 'kiritilgan sonlar teng' 
#     else :
#         son = son2
#     print(f'{son} soni eng katta ') 
    
# son1 = int(input("birinchi raqani kiriting >>"))
# son2 = int(input("ikkinchi raqani kiriting >>"))
# qiymat_top(son1,son2)

# def bolinish_alomatlari(son):
#     for n in range(2, 11):
#         if not son % n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")


# bolinish_alomatlari(20)