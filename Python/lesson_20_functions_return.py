"""
Repeation for my self 

lesson lesson 20 funksiyalar

for repiation  https://quizlet.com/_dfgct2?x=1qqt&i=52phgt

@author: rashidovj
"""
#                        lesson 20


# return = qiymat  qaytarish uchun

# def kelmagan_talaba(ism,familiya):
#     """ ism familiyani kursatadi """
#     talaba_nomi = f'{ism } {familiya} '
#     kelgan = f"{ism} kursdan qoldirilsin"
#     return talaba_nomi , kelgan  # return talaba_nomi degan uzgazuvchimi qaytaradi
     

# talaba=kelmagan_talaba('obidov' ,'hakim')
# print(talaba)

#  ixtiyoriy argument kiritsh yani foydalanuvchi kiritsa ishliydi else ok
# def kelmagan_talaba(ism,familiya , otasi_ismi=''):
#     """ ism familiyani qaytaruvchi  """
#     if otasi_ismi :
#         talaba_nomi = f'{ism } {familiya} {otasi_ismi}'
#     else :
#         talaba_nomi = f'{ism } {familiya} '
#     return talaba_nomi   # return talaba_nomi degan uzgazuvchimi qaytaradi
    
# talaba=kelmagan_talaba('obidov' ,'hakim')
# talaba1=kelmagan_talaba("asdfa",'adfaf','adfafafdasfasd')
# print(talaba , talaba1)

# ixtiyoriy argument None agar biron uzgaruvchi urniga hech narsa ciqarsak

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# car1 = avto_info('BMW',"x7",'oq','avtomat',2022,40000)
# car2 = avto_info('BMW',"x7",'oq','avtomat',2022)
# cars=[car1,car2]
# print(cars)

# for car in cars :
#     if car['narh']:
#         narh = car['narh']
#     else:
#          narh='Nomalum'   
#     print(f"{car['rang']} {car['model']}. Narhi: {narh}")

# range funksiyasining kodi 
# def rang(min,max,qadam=1):
#     sonlar = []
#     while max>min :
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# print(rang(1,8,2))

# print(list(range(1,8,2)))

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] 
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# for car in avtolar :
#     if car['narh']:
#         narh = car['narh']
#     else:
#           narh='Nomalum'   
#     print(f"{car['rang']} {car['model']}. Narhi: {narh}")


#                                   amalyot

# def qiymat_top(son1,son2,son3):
#     """ Sonning katta sonni topib beruvchi function """
    
#     if son1 > son2 and son1>son3 and son2>son3 :
#         son = f'{son1}>{son2}>{son3}'
#     elif son1==son2==son3 :
#         son = f'{son1}={son2}={son3}'
#     elif son1==son2 and son1>son3 :
#         son = f'{son1}={son2}>{son3}' 
#     elif son1 < son2 and son2<son3 :
#         son = f'{son1}<{son2}<{son3}'
#     elif son1>son2 and son2==son3 :
#         son = f'{son1}>{son2}={son3}'
#     elif son1==son2 and son2<son3 :
#         son = f'{son1}={son2}<{son3}'
#     elif son1<son2 and son2==son3 :
#         son = f'{son1}<{son2}={son3}'
#     elif son1>son2 and son2<son3 :
#         son = f'{son1}>{son2}<{son3}'
#     elif son1<son2 and son2<son3 :
#         son = f'{son1}>{son2}<{son3}'
#     else :
#         son = f'{son1}<{son2}>{son3}'
#     return son   
  
# son1 = input("1-son= ")
# son2 = input("2-son= ")
# son3 = input("3-son= ")

# qiymatlar = qiymat_top(son1,son2,son3)
# print(qiymatlar)


# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
                    
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar
# tub1 = tub_sonlar_top(1,100)
# print(tub1)

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1  :
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))