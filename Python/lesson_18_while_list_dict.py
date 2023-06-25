"""
Repeation for my self 

lesson lesson 18 while list va dict uchun

for repiation  thttps://quizlet.com/_dfd57j?x=1jqt&i=52phg

@author: rashidovj
"""

 
#                        lesson 18 while list va dict uchun

#  while sikli orqali listni tuldirish 

# print('dustlar ruyhatini tuzamiz')
# dustlar = []
# n = 1
# while  True  :
#     dust = input(f'{n}-dustingizni ismini kiriting   >> ')
#     a = input('davom etasizmi ha or no')
#     dustlar.append(dust)
#     n += 1
#     if a=='no' :
#       break 

# for dust in dustlar :
#     print(dust.title())

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)

# dustlar = {}
# ishora = True
# while ishora :
#     ism = input('dostingizni ismini kiriting >> ')
#     yosh = input (f'{ism.title()}ning yoshini kiriting >> ')
#     dustlar[ism]=int(yosh)
#     x = input('yana dost qushasizni ha or no')
#     if x!='ha':
#         ishora=False

# for k,v in dustlar.items() :
#     print(f'{k.title()} ning yoshi {v} da  ')

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# x = 'lacetti'
# while x in cars :
#     cars.remove(x)
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar :
#     talaba=talabalar.pop()
#     while True :
#          x = int(input(f' {talaba.title()}ning bahosini kiting >> '))
#          if x>=6 :
#              print(f'Maksimal bal 5 bal siz {x} ni kirittingiz' ,
#                    f'{talaba.title()}ning bahosini qayta kiriting')
#          else :
#             break
#     baholangan_talabalar[talaba] = x
    
# for k ,v in baholangan_talabalar.items() :
#     print(f"{k.title()} ning bahosi {v} ")

#                          amalyot  l 18

# mahsulotlar =[]
# while True :
#     mahsulot = input('Mahsulotni kiriting >> ')
#     mahsulotlar.append(mahsulot)
#     x = input('yana mahsulot qushasizmi ha bulsa istalgan tugmani bosing or no:')
#     if x == 'no':
#         break


# narxlar = {}
# while mahsulotlar :
#     mahsulot = mahsulotlar.pop()
#     narxlar[mahsulot]=int(input(f'{mahsulot}ning narxi = '))
# print('Mahsulotlar ruyhati tuzuldi ,')

# order = []
# while True :
#     order.append(input('\n Nima izlamoqdasiz >> '))
#     x = input('yana biron narsa izlayabsizmi ha or no >>')
#     if x == 'no' :
#         break
    
# for k in narxlar :
#     if k in order :
#         print(f'{k}ning narxi {narxlar[k]} ga teng')
# for x in order :
#     if x not in narxlar :
#         print(f'Bizda {x} mavjud emas')

