"""
Repeation for my self 

lesson 10 , 11 if, elif, else 

@author: javokhirdeveloper
"""


#                                       lesson 10


# if else agar yoki aks holda shun C++ ga uhshiydi faqat new suffs :
# yozilishi yakumida : quyiladi blok sxemada rom shaklida buladi 
# yana buni phytonda bir qatorda yozish mumkun 

# a = int(input("yoshizni kiriting >>> "))
# print(f"yoshiz {a} da ekan kirishiz mumkun emas  ") if a<18 else print('welcome')

# passcode = 'asdfghjkl'
# kod = input("Iltimos kirish uchun kodni kiriting >>>")

# if kod != passcode :
#     imkoniyatlar=[1]
#     for x in imkoniyatlar :
      
#         print(f"Xato  {x} imkoniyat qoldi")
#         passcode = 'asdfghjkl'
#         kod = input("Iltimos kirish uchun kodni kiriting >>>")
        
#     if kod == passcode :        
#         print("HUSH KELIBSIZ")
#     else :
#         print('Urinishlar soni ortib ketti')
# else :        
#     print("HUSH KELIBSIZ")
#                                       Amalyot -> 10

# son = float(input('istalgan sonni kiriting >>>'))
# if son > 0:
#     print("Kiritgan soninggiz musbat son")

# else :
#     print("kritgan soninggiz manfiy")


#                                       lesson 11 , Amalyot


# if va else faqat 1 ta shartni bajaroladi kuproq shart uchun else if elif ni kiritamiz :
# va hohlaganimizcha kiritishimiz mumkun 

# or va and aperotorlarin bir vaqtda ikkita sharni tekshiradi 

# yosh = int(input('Yoshingizni kirting >> '))
# ielts = float(input("\nIELTS balingizni kiriting>> "))

# if yosh >=18 or yosh==17 and ielts>=5.5 :
#   a='\nUniversetetutga kirishiz mumkun'
# elif yosh==16 and ielts>=5.5 :
#   a='\nkelasi yil qayta uriniib kuring'
# else :
#   a = '\nMalumotingiz universetetut uchun yetarli emas'
# print(a)


# BOOLEAN MALUMOTLAR TURIN YANI TRUE IF OR FOLSE  ELSE

# narx = int(input('OVQATNING NARXINI KIRITNG >> '))
# choy = input('intemolci choy oldimi ha yoki yoq >> ')
# if choy.lower() == 'ha' :
#     narx = narx+5000
# else :
#     narx=narx
# non = input('intemolci non oldimi ha yoki yoq >> ')
# if non.lower() == 'ha' :    
#     soni = int(input('Nechta nonni paqqos tshurdiz >> '))
# if non.lower() == 'ha' and soni>0 :
#     narx = narx+5000*soni
# else :
#     narx=narx
# print(narx)





# taom = ['shashlik', 'manti' , 'somsa', 'shorva']
# mijoz = input('nima yiysan bitch >> ')
# if mijoz.lower() in taom :

#     print('ozroq kutibtur keladi hozir') 
# else :
#     print('qatta kurvossan 5 yulduli restaranni tur yuqol')

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

