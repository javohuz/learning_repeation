"""
Repeation for my self 

lesson lesson 21 , 22 funksiyalar dict and list

for repiation  https://quizlet.com/_dfgct2?x=1qqt&i=52phgt

@author: rashidovj
"""
#                               lessson 21

#  finction dict qushish 

# def  talabalar_list(names):
#     """ talabalar bahosi kirish uchun """
#     talabalar_bahosi = {}
#     while names :
#         name = names.pop()
#         talabalar_bahosi[name] = int(input(f'{name.title()}ning bahosini kiriting '))
#     return talabalar_bahosi

# students =['Hakim' , 'Vali' , 'Javohir' , 'Avaz']
# bahosi = talabalar_list(students[:])
# print(bahosi)
# print(students)

#                       amalyot

# def katta_harf(lists) :
#     """ list ichidagilarni katta harf qiladi"""
#     for n in range(len(lists)) :
#         lists[n] = lists[n].title()
#     return lists


# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)


# def katta_harf(lists) :
#     """ list ichidagilarni katta harf qiladi"""
#     katta =[]
#     listn = lists[:]
#     for n in range(len(listn)) :
#         listn[n] = listn[n].title()
#         katta.append(listn[n])
#     return katta


# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)


#  finction dict qushish 

# def  talabalar_list(names):
#     """ talabalar bahosi kirish uchun """
#     talabalar_bahosi = {}
#     for n in range(len(names) ):
#         name = names[n]
#         talabalar_bahosi[name] = int(input(f'{name.title()}ning bahosini kiriting '))
#     return talabalar_bahosi

# students =['Hakim' , 'Vali' , 'Javohir' , 'Avaz']
# bahosi = talabalar_list(students[:])
# print(bahosi)
# print(students)

#                           lesson 22 uzgaruvchan finction

#  * va ** yani *args va ** kwargs kw = kayword 
# *args bu tuple shaklida yukliydi yani finction yaratganda istagancha qiymat
#  kiritsh mumkun kiritilaganlar tuple yani uzgarmas ruyhat
#  **kwargs bu dict shaklida yuklaydi 

# def summa(x,y,*sonlar):
#     """ sonlar yigindisi hisoblasvchi finction """
#     yigindi = x + y
#     for n in sonlar:
#         yigindi += n
#     return yigindi     # return x=y=sum(sonlar)
# son =summa(5,5,5,6,6,7,1)   
# print(son)

#   **kwargs bu dict shaklida yuklaydi 
# def avto_info(**malumot):
#     """Avtomobil haqida malumot tuplaydigan finction """
#     return malumot
# car1 = avto_info(turi='gm' ,)


#                               practice


# def summa(x,y,*sonlar):
#     """ sonlar yigindisi hisoblasvchi finction """
#     yigindi = x*y
#     for n in sonlar:
#         yigindi *= n
#     return yigindi     
# son =summa(5,5,5,6,6,7,1)   
# print(son)

# def info_talaba(ism , familiya , **talaba_info ):
#     """talabalar haqida balumot yigivchi function """
#     talaba_info["ismi"]=ism
#     talaba_info["familiyasi"]=ism
#     return talaba_info

# talaba = info_talaba("javohir","rashidov",yosh=19)
# print(talaba)
