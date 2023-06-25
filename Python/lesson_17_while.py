"""
Repeation for my self 

lesson lesson 17 ( while ) 

for repiation  thttps://quizlet.com/_dfd57j?x=1jqt&i=52phg

@author: rashidovj
"""

#             lesson 17 ( while ) 

# ism = input('ismingiz nima')
# savol = f'salom {ism} yoshingiz nechida'
# yosh = input(savol)
# print (ism , ' siz bilan tanishganimdan hursandman ')

#  while sikli : manosi toki or davomida  bu sikli bir shart tugri kelmagunga
#  dastur ishlay veradi forga uhshaydi farqi for malumot tugagunga qadar 
#  while esa kiritilgan shartga qadan shart tugri kelmasa abadiy dastur buladi

# son = 1 
# while son <=5 :
#     print(son )
#     son += 1 
# print('Dastur tugadi')
#  son = son+1 == son += 1 , A = A + B == A += B

# while and input

# savol ='son kiriting kvadratini topib beraman '
# savol += '(dasturni tuxtatish ucun "stop") \n >>> '
# qiymat = ''
# while qiymat != 'stop' : 
#     qiymat = input(savol)
#     if qiymat != 'stop' : # nega if bcs biz pastda int dan foydalandaldik 
#         kvadrat = int(qiymat)**2
#         print(kvadrat)
# print('Dastur tugadi')

# ishora orqali stop berish

# savol ='son kiriting kvadratini topib beraman '
# savol += '(dasturni tuxtatish ucun "stop") \n >>> '
# ishora = True
# while ishora :
#     qiymat=input(savol)
#     if qiymat == 'stop' or qiymat == 'exit' :
#         ishora = False 
#     else :
#         print(float(qiymat)**2)
# print('Dastur tugadi')
    
# #    break  sindirish yani kod shuyerda tuhtahdi 
 
# savol ='son kiriting kvadratini topib beraman '
# savol += '(dasturni tuxtatish ucun "stop") \n >>> '

# while True : # abadiy sikl
#     qiymat=input(savol)
#     if qiymat == 'stop' or qiymat == 'exit' :
#         break
#     else :
#         print(float(qiymat)**2)
# print('Dastur tugadi')
      
# break bu for aperatori uchin ham ishliydi if bn 

# for n in range(1,9):
#     if n==5 :
#         break
#     print (n)

# break ning sinonimi continue bu  davomiy yani qaysidir operator bajarilganda 
#  keyingi kodni uqimay kod boshiga qaytib ketadi

# for n in range(1,9):
#     if n==5 : 
#         continue # n = 5 bulganda kod shetta tuhtiydi i boshiga qaytadi 
#     print (n)

 
#                              praltise  17


# kitob  = []
# mal = ''
# while mal != 'no' :
#     kitob.append(mal)
#     mal = input('qanaqa kitoblar uqigansiz (davom etamizmi ha or no ) >>> ')
    
# print ('siz uqigan kitoblar ruyxati ', end='')   
# for done in kitob :
#         print(done.title() , end='  ,' )
        
# print('Dastur tugadi')

# savol = 'yoshingizni kiting (stop => exit or quit ) >>> '
# ishora = True
# while ishora :
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit' :
#         ishora = False
#     elif int(yosh) < 7 :
#         print("siz uchun chipta narxi 2000 so\'m") 
#     elif int(yosh) >= 7 and int(yosh) < 18  :
#         print("siz uchun chipta narxi 3000 so\'m")
#     elif int(yosh) >= 18 and int(yosh) < 65  :
#          print("siz uchun chipta narxi 10000 so\'m")  
#     else :
#         print('sizga kirish bepul')

# print('Dastur tugadi')

# savol = 'yoshingizni kiting (stop => exit or quit) >>> '
# while True :
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit' :
#         break
#     elif int(yosh) < 7 :
#         print("siz uchun chipta narxi 2000 so\'m") 
#     elif int(yosh) >= 7 and int(yosh) < 18  :
#         print("siz uchun chipta narxi 3000 so\'m")
#     elif int(yosh) >= 18 and int(yosh) < 65  :
#          print("siz uchun chipta narxi 10000 so\'m")  
#     else :
#         print('sizga kirish bepul')

# print('Dastur tugadi')

# savol = 'yoshingizni kiting (stop => exit or quit) >>> '
# yosh = ""
# while yosh !='exit' :
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit' :
#         yosh='exit'
#     elif int(yosh) < 7 :
#         print("siz uchun chipta narxi 2000 so\'m") 
#     elif int(yosh) >= 7 and int(yosh) < 18  :
#         print("siz uchun chipta narxi 3000 so\'m")
#     elif int(yosh) >= 18 and int(yosh) < 65  :
#           print("siz uchun chipta narxi 10000 so\'m")  
#     else :
#         print('sizga kirish bepul')

# print('Dastur tugadi')

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if float(qiymat)<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

