# -*- coding: utf-8 -*-
"""
easy stuffs just for repeation 

"""  
# python 

#                                  lesson4


# o'zgaruchilar ustida amallar -> uzgaruvchi uzi nima va nimaga kerak 
# uzgaruvchilar shuchaki kichkila lotin haru=iflari bilan yasaladi masaln (ism)
# ularni ularni birmarta tanlab quyib keyin ishlaturamiz you cam see

# ism="something" => yasalishi shunaqa yana joy tashlash mumkun emas urniga __

#                  lesson5   https://quizlet.com/_dcdmkv?x=1jqt&i=52phgt

# string -> matn hullas bu matn bu bitta yoki holagancha harf bulishi can
# why need ular uzgaruvchilar ustida amallar or shunga uhshash narsalaga  

# ism="Javohir"
# familiya="Rashidov"
# print(ism+'  '+familiya)  joy tahlas kk bulsa
 
#  ( f" ) ikta uzgaruvchini birlashtradi or matn bilan bilan uzgni birlashtradi

# ism= "Asilbek"
# familya= "Rashidov"
# full_name= f"{ism} {familya}"
# print(full_name)

#also we can take we want sterkker or any belgiladdi from unicode-table.com  

#smile= "😉"
#print("Asilbek mol " + smile)
 
#maxsus belgilar \n  \t lar \n qator \t kottaro joy tashlaydi

#print("i will go to tashkent \r next week ")
 
#print("i will go to tashkent \tnext week ") 
  
#string metotlari niga kk uzgaruvchiladdi harflarini uzgartishi yoku shunga 
# uhshH narsalarga kk yasalishi matn.metod() 
 
#ism="javohir" 
#ism.upper() uzg dagi harfladdi kotta qiladi 
#ism.lower() hamma harfladdi kichik qiladi
#ism.title() bosh harladdi kotta qiladi

#keyin strip stripning vazifasi uzgchidan keyin yoki okdin bush joylar qolgan 
#bulasa olib tashkaydi faqat chapdagini olish kk bulsa last yani "lsrtip" 
#ung tomonni olish uchun right or "rstrip" quuysak buadi for ex

#fan="        english          "
#print(fan)
#print(" i know " + fan.strip() + " well")
#print(" i know " + fan.rstrip() + " well")
#print(" i know " + fan.lstrip() + " well")

# INPUT uta muhim narsa bu foydalanuvchidan malumot oladi isim deb uzimiz 
# kiriymaymizdda foydalanuvchidan qandaydur matn suraydi 

#ism=input("Ismingizni kiriting \n>>>") 
#print("Assalomu alaykum " + ism.upper())


#ism=input("Ismingizni kiriting \n>>>")
#print("Assalomu alaykum " + ism.title())

#Amalyot 

#kucha="Zamondosh"
#mahalla="yangi hayot"
#shahar="shahrisabz"
#print( kucha + " kuchasi, " +mahalla + " mahallasi, " + shahar + " shahri.")

#kucha= input("Kucha nomini kiriting \n>>>")
#mahalla=input("Mahalla nomini kiriting \n>>>")
#3shahar=input("Shahar nomini kiriting\n>>>")
#yangi_manzil=f" {kucha} kuchasi \n {mahalla} mahallasi \n {shahar} shahri \n"
#print( kucha + " kuchasi,\n" +mahalla + "mahallasi,\n" + shahar + "shahri.\n")
#print(yangi_manzil.title())
#print(yangi_manzil.upper())
#print(yangi_manzil.lower())

#                     lesson_6  -> raqam bilan ishlash          

# any uzg for ex a raqam bilan ishlagincha => a = 46 buladi we dont need qavs
# va "' lar kk emas 

#a = 6 -> print nersha ishluradi keyi butun sonlar int onli sonla float buladi
# bu ulani turi butun sonlani . bilan ajratamiz 6.8 ... 
# yana uzun raqamla qupol bulib qolmasligi uchun _ ishlatsak buladi 8_889_899

#x, y, c =4, 5, 6 # raqamlani kiritguncha new qatordan yozish shartmas can as it

#butun va onli sonlar ustida amallar bajarsak natija unli turiyam float buladi
 
#a, b,= 50, 6.9
#print(a*b)  #turini bilish uzchun type 

#contstanta bu uzgarmas dastur davimda ugartrilmaydi yani qaysi pragrammada 
#yozilyotgan busa usha dastur uni uzgartirmaydi lekin paytinda unaqa narsa yuq
# but dasturchila const ni kotta harfa bi yozib ketishishga kelishib olishgab 

#x=7
#PI= 3.14


#matn bilan raqamni boglash uladid bitta da bajarib bumaydi uning uchun yoki 
#raqamni matn yani string urniga ishalatish uchun olsiga str stringni qisqarma-
# sini yozamiz str(uzg) yoki 

#name="Jony"
#yosh=19 
#info=name + ' ' + str(yosh) +" yoshda"
#print(info)

#inputdan olingan malumotlarini hammasi str yani matn kurinishida eslab qoladi
# buni son sifatida qabul qilmoqchi bulasak oldiga int or onli son dib qabul
# qilmoqchi bulsak float belgilisini quyamiz int(uzg)  float(uzg)

#ism=input("ismingizni kiriting\n>>>")
#yosh=input("yoshingizni kiriting\n>>>")
#t_yil=(2022-int(yosh))

#print("salom " + ism.title() + " siz " + str(t_yil) + "-yili tugulgansiz")

#  AMALYOT

#son=input(" You can find any numbers ^2 and ^3 \n Any number write:  " )
#kvadrat=int(son)**2
#kub=int(son)**3

#print(son + " ning kvadrati " + str(kvadrat) + " ga teng " )
#print( son + " ning kubi " + str(kub) + " ga teng " )

#print("\n " + son + "^2=" + str(kvadrat) + "\n ")
#print( " " + son + "^3=" + str(kub)  )

#print(f"\n {son}^2={kvadrat} \n ") #tepadaki bilan bir xil natija chiqadi
#print(f" {son}^3={kub}  ")

# ism=input("ismingizni kiriting\n>>>")
# yosh=input("yoshingizni kiriting\n>>>")
# t_yil=(2023-int(yosh))

# print( "salom " + ism.title() + " siz " + str(t_yil) + "-yili tugulgansiz")

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# print(f"{a}+{b}=", a+b)
# print(f"{a}-{b}=", a-b)
# print(f"{a}x{b}=", a*b)
# print(f"{a}/{b}=", a/b)

#                         Lesson_7 -> list => ruyhat 
#  https://quizlet.com/_dcdt7d?x=1jqt&i=52phgt

# list -> bizga more uzgaruvchilar ochmasdan bitta uzgaruvchini ichida kk licha
# string int float larni kiritish imkonini beradi yasalishi 

# m_fanlar=['qorinli domla', 'kksiz fan', 'nimadurda']
# kkliyli_foizi=['30','10' , '?']
# hayotta_use=[] # bush ruyhat ham yaratsak buladi 

# print(m_fanlar[0]) #print qilish shunday buladi ichidagilar ketma ketligidagi
# tartib raqami bn keladi faqat 0 dan boshlab sanaladi 
# print(m_fanlar[-1]) # ohiridan sanomoqchi bulsak( - ) bersak buladi

#bularni metodlar (upper, title ...) yordamida print qigincha uzgartib chiqarsak
# buladi and we can sonlar bn ular ustida amallar bajarsak buladi

#print(m_fanlar[0].title())

#list ichidagilarni uzgartirsak buladi 

#m_fanlar[0]= 'material'
#print(m_fanlar)

#listga yana string or int qushmoqchi bulsak new metod [ .append() ] can use

# m_fanlar.append('english') 
# print(m_fanlar)

# append faqat list ohiridan qushadi ichida quchmoqchi bulsak [ .insert() ] 
# can use 

#m_fanlar.insert(2,'anything')
#print(m_fanlar)

#ruyhat ichidagi birortasini uchirmoqchi bulsak [ del ] from aperator can use

#del m_fanlar[2]
#print(m_fanlar)

# list uzun bulib ketsa uni index sini bilamasak [ .remove() ] metod use for del

#m_fanlar.remove('nimadurda')
#print(m_fanlar)

# listda bir xil strimlar bulsa remove boshdan boshlab bitta bitta uchiradi
# ular kup bulsa kodni takrorlaymiz until finished

# listdan birorta strimni sugurib ulish del dan farqi biz undan foydalanishimiz
# mumkun buning uchun [ .pop() ] metoddan foydalanamiz

#keraksiz = m_fanlar.pop(1)
#print(keraksiz)

#kerakli = m_fanlar.pop()  # index kiritmasak pop ohirgi strimni oladi
#print(kerakli)

# for me new metods are append , insert , romove , pop and new aperator is del.

# AMALYOT

#my_friends=['Jasur', 'Abbi' , 'Avaz' ]
#print(f"{ my_friends[0]} , kechga kapm borasanmi? " )
#print(f"{my_friends[1]} Jas kechga kam boreykan , borasan Avaz ushetda")

#sonlar= ['1', '2.9' , '-5']
#natija=int(sonlar[0])+float(sonlar[1])+16
#print(natija)
#manfiy = sonlar.pop(2)
#print(manfiy)

# t_shaxslar=['nyuton ' , ' amir temur ' ]
# z_shaxslar=["elon mask " , " kira " ]

#print(f"""\n Man holardimki {t_shaxslar[0].title()} bilan choy ichib,
# then together will go to {z_shaxslar[1].title()}'s lesson 👌😂""")

# exams= [ "nano", 'algo', 'ulchash', "zna"]


# exams.append("prakthis")
# tugagan =exams.pop(2)
# exams.insert(1, 'biijj')
# del exams[2]
# exams.remove('nano')


# ballar =['93', '96', '94', '92']

# ballar.insert(1, '92')

# tugagan= [exams.pop(0), exams[-1]]
# tup_bal= [ballar[0] , ballar[-1]]


# print(f" {tugagan[0]}={tup_bal[0]} \n {tugagan[-1]}={tup_bal[-1]} ")

# ism=['Jasur','Hakim', "Vali"]
# ism[2]='ahfla'

# friend=[]
# friend.append('Jasur', )
# friend.insert(1, 'bekki')
# friend.insert(2, 'umid' )

# friend.remove('bekki')

# """
# 09/11/2020

# Dasturlash asoslari

# #07-dars: Lists

# Muallif: Anvar Narzullaev

# Web sahifa: https://python.sariq.dev
# """


# #ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]
# #Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
# print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# # sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# print(sonlar)

# # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar[0] = sonlar[0]+sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 37
# del sonlar[5]
# print(sonlar)

# #t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

# #Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# suhbat qilishni istar edim\n")

# #friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# friends = []
# friends.append('John')
# friends.append('Alex')
# friends.append('Danny')
# friends.append('Sobirjon')
# friends.append('Vanya')
# print(friends)

# #Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove('John')
# friends.remove('Alex')
# print(friends)

# #Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.append('Hasan')
# friends.insert(0, 'Husan')
# friends.insert(2, 'Ivan')
# print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)



#                 lesson_8    https://quizlet.com/_dcdt7d?x=1jqt&i=52phgt

#sort() metodi buning vizifasi listni alfabet buyicha tartibga soladi agar ruyhat ichida 
# kotta harflar bulsa usha biirnchi keladi va bu raqamlar uchun ham huddi shunday ishlaydi 



# cars = ['bmw','mercedes benz','general motors', 'tesla', 'audi']

# cars.append('jentra')
# # cars.sort(reverse=True)
# print(sorted(cars, reverse=True))
# # print(cars)

# sonlar=['5','234', '452', '-45' , '53', '5334']

# sonlar.sort(reverse=True)

# sonlar bilan ishlash yani finksiyalar range(a,b) yani list yaratsa a dan b-1 gacha 
# agar range(a,b,c ) bulsa c buyersa qadam yani c cha sonlarni olib ketadi 
# list yaratish ucun list(range(a,b))

# sonlar=list(range(0,10))


# buyerda max , min , sum funksiyalni maksimal minimal qiymatini chiqarish yigindi sum 


# sonlar = list(range(1,10))
# max_son=max(sonlar)
# min_son=min(sonlar)
# soni=len(sonlar)
# sum_son=sum(sonlar)

# print('1 dan ungacha sonlar yigindisi =',sum_son , 'urta arifmetigi =', int(sum_son)//int(soni))



# list ichidagi narsalarni nusxalash yoki kesib olish sonlar = sonlar[1:8] yani 
# sonlar ichidagilarni 1 dan 8 chi elementgacha kesin oladi 

# sonlar = list(range(1,9))

# son_n = sonlar[1:3]
# cars = ['bmw','mercedes benz','general motors', 'tesla', 'audi']
# my_cars = cars[:]

# my_cars.append("lasetti") 
# selt_cars = my_cars [1:]
# stay_cars = my_cars [:1]

# tuple bu uzgarmas list yasalishi [] urniga () ishlatiladi va uni uzgartrib bulmaydi
# uzgartrish uchun listag utqazish 


# cars = ('bmw','mercedes benz','general motors', 'tesla', 'audi') # uzgarmas ruyhat
# carss = list(cars[1:5]) # listaga uzgardi 
# carss = tuple( carss) #   list uzgarmas ruyhatga uzgardi



#                                       Amalyot -> 8

# davlatlar=["USA", 'UK', 'UZB', 'RUS']
# print(sorted(davlatlar, reverse=True))
# len(davlatlar)
# davlatlar.reverse()
# print((davlatlar))

# davlatlar.sort(reverse=True)
# print(davlatlar)

# sonlar=list(range(120,1201,2))

# print(sonlar[-1])

# print(sum(sonlar))
# print(max(sonlar))
# print(min(sonlar))
# print(len(sonlar))


# print(sonlar[1:21])
# print(sonlar[1:21])
# print(sonlar[1:21])
# soni=len(sonlar)
# print(int(soni)/2)
# print(sonlar[270:291])
# print(sonlar[521:])

# taomlar=['osh', 'manti', 'somsa', 'norin', 'shorva']

# nonishta = taomlar[:]
# nonishta.remove('osh')
# nonishta.remove('norin')
# nonishta.append('sut')
# nonishta.append('qaymoq')

# nonishtal=('osh', 'manti', 'somsa', 'norin', 'shorva')

# nonishtal[0] = 'dfhsjkhfjkshd' 

#               lesson 9  https://quizlet.com/_defr0q?x=1jqt&i=52phgt

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




#                    lesson 10  https://quizlet.com/_defr0q?x=1jqt&i=52phgt


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



#             lesson 11 , Amalyot  https://quizlet.com/_defr0q?x=1jqt&i=52phgt


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



#            lesson 14 dictionary https://quizlet.com/_deyoqb?x=1jqt&i=52phgt

# ruyhatga uhshaydi yani bir soz ikkinchisiga thenglashtradi bu raqam bn ham bulish can  
# yasalishi {} bn  

# talaba = {'javohir':5 , 'hakim':5 , 'valijon':4}
# print('talabaning bahosi' ,  talaba['javohir'])

# talaba = {'Javohir':int(input('Javohirning bahosi >> ')),
# 'hakim':int(input('Hakimrning bahosi >> ')),
# 'vali':int(input('Valirning bahosi >> ' ))
#             }

# for baho in talaba :
#     print(baho)



# qushi , uzgartrish , uchirish

# talaba = {'javohir':5 , 'hakim':5 , 'valijon':4}
# talaba['hakim']=6
# talaba['jasur']=5
# del talaba['valijon']
# print(talaba)


# .get() vazifasi agar suralgan smt lugat ichida bulmasa keyingi kodni uqiydi 
# agar bulsa kiritilgan soz kalitini chiqaradi .
# talaba = {'javohir':5 , 'hakim':5 , 'valijon':4}
# print(talaba.get('jasur' ,'bunday narsa yoq'))


#                           amalyot

# lugat = {'can' : 'mumkun' , "if" : "agar" , 'else':'aks holda'}
# x = input("english word >> ").lower
# print (lugat.get( x , 'kechirasiz bunday soz mavjud emas'))


# lugat = {'can' : 'mumkun' , "if" : "agar" , 'else':'aks holda'}
# x = input("english word >> ").lower()
# tarjima = lugat.get(x)
# if tarjima == None :
#     print('kechirasiz bu sozni tarjima qila olmayman')
 # else :
#     print(lugat[x])



# otam = {"ismi": "mavlutdin", "tyil": 1954, "viloyat": "samarqand"}
# tyil = otam["tyil"]
# vil = otam["viloyat"]
# print(
#     f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan"
# )

# taomlar = {
#     "ali": "osh",
#     "vali": "shashlik",
#     "hasan": "lag'mon",
#     "husan": "mastava",
#     "olim": "somsa",
# }

# taom = taomlar["ali"]
# print(f"Alining sevimli taomi {taom}")

# python_izohli_lugati = {
#     "integer": "Butun son",
#     "float": "O'nlik son",
#     "string": "Matn",
#     "list": "Ro'yxat",
#     "tuple": "O'zgarmas ro'yxat",
# }
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

#                       Lasson 15 https://quizlet.com/_deyoqb?x=1jqt&i=52phgt



# .items() metodi manosi elementar  , lugatdagi narsalarni chiqaradi
# me = {
#      "ism" :"javohir",
#      "familiya ":"rashidov",
#      "yosh":17 , 
#      "tel_n":+998906675266
#      }
# for kalit,qiymat in me.items() :
#     print(f"kalit : {kalit} ")
#     print(f"qiymat : {qiymat}\n")

# tel = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in tel.items() :
#     print(f'{k.title()} ning telefoni {q}')

# .keys() metodi faqat kelitlarni chiqaradi , .values() qiymarlarni 

# me = {
#       "ism" :"javohir",
#       "familiya ":"rashidov",
#       "yosh":17 , 
#       "tel_n":+998906675266
#       }

# print(me.values())

# for k in me.keys() : # aagr .keys() bulmasa ham huddi shumday ishlardi
#     print(k)
# for q in me.values() : 
#     print(q)

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# bozorliq = ['olma' , 'uzum', 'ananas']

# for k in mahsulotlar.keys():
#     if k in bozorliq :
#         print(f'{k}ning narxi {mahsulotlar[k]}')

# for bor in bozorliq :
#     if bor not in mahsulotlar :
#         print(bor , 'bizda bunaqa mahsulot yoq')

# for k in sorted(mahsulotlar):
#     print (k)

# set yani sets bu ham hudi listga uhshaydi faqat buni ichidagilar
# takrorlanmaydi takrorlangan bulsa uqimaydi yasalishi  a={'b','c'}

# kitoblar={'math', 'kimyo', 'math', 'tarix'}
# print(kitoblar)

# yana sets -> set() ni boshqa metodlar kabi ishlatsa buladi yani 

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# for tel in set(telefonlar.values()):
#    print(tel)

#                           amalyot

# smt = {
#        'for': 'biror amalni qayta qayta bajarush sikli' ,
#        'in' : 'yuklaydi',
#        'set' :'takrorlanmaydi',
#        'if' : 'agar',
#        'append':'listga qiymat qushadi'
#        }

# for k,q in sorted(smt.items()):
#     print(k.title(),'->',q)


# count = {
#         'uk':'london',
#         'russia':'maskov',
#         'germany':'berlin',
#         'uzbekistan':'tashkent'
#         }
# print('Davlatlar ')
# for k in  sorted(count.keys()):
#     print( k.title(),)
# print('Poytaxtlar ruyhati ')
# for q in sorted(count.values()):
#     print(q.title())

# davlat =input('Istalgan davlat nomi kiriting ...').lower()
# x=count.get(davlat)
# print(count.get(davlat, 'kechirasiz buning qiymatini aniqlay olmayman'))
# if x==None :
#     print('Bunday malumot mavjud emas')
# else :
#     print(f'{davlat.upper()} davlatining poytaxti {x.upper()}')

# taomlar ={
#     'manti':15000,
#     'honim':15000,
#     'chuchvara':20000,
#     'osh':25000,
#     'beshteks':20000,
#     'lagmon':20000,
#     'moshhorda':20000,
#     'non':4000,
#     'choy':5000
#           }

# print('Bugun nima yeymiz  ')
# order =[]
# for x in range(3):
#     order.append(input(' >>> ').lower())

# for k in taomlar.keys():
#     if k in order :
#         print(f'{k.title()}ning narxi {taomlar[k]}')

# for x in order:
#     if x not in taomlar:
#         print(f'Bizda {x.title} qolmagan')


#         lesson 16 -> Nesting   https://quizlet.com/_deyoqb?x=1jqt&i=52phgt


# NESTING biron malumot ischiga boshqasi qushish yani list ichiga dict or aksi
#  list ichiga dict qushish
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }


# cars = [car0,car1,car2]
# cars[2]['rang']='qora'
# print(cars[2]['rang'] ,\
#       cars[1]['rang'])

# cars = [car0,car1,car2]
# for car in cars :
#     print(f"{car['rang']} , "
#           f"{car['narh']}"
#           )
# aim = []
# for n in range(4):
#     mark = {
#         'model':None,
#         'ramg':None,
#         'yil':2023,
#         'karobka':'avto'
#            }
#     aim.append(mark)
# for mark in aim[:2] :
#     mark['model']='BMW'
#     mark['ramg']='qora'
# for mark in aim[2:]:
#     mark['model']='lambo'
#     mark['ramg']='qizil'
#     mark['karobka']='mexanik'

# for mark in aim :
#     if mark['karobka']=='avto' :
#         mark['narx']=50000 
#     else :
#         mark['narx']=40000
    
# for x in aim :
#     for y in x :
#         print(f'{y.title()} --> {x[y]}')

#  dict ichiga list qushish

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for k, v in dasturchilar.items():
#     print(f'\n{k.title()} quyidagi dasturlash tilaarini biladi :' , end=' ')
#     for knows in v :
#         print(f'{knows.upper()} ' , end=' ')


# dict ichiga dict qushish va yan bu ishni hohlagainimizcha qilsak buladi 

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism , malumot in hamkasblar.items():
#     print(f'\n{ism.title()} ')
#     for k , v in malumot.items():
#         print(f"{k.title()} --> {v}" )
            

#                          praktis




# buxoriy = {
#     "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#     "tyil": 810,
#     "vyil": 870,
#     "tjoy": "Buxoro",
# }

# qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

# vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

# navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}


# grandpas = [buxoriy,qodiriy,vohidov,navoiy]
# for k in grandpas :
#     print(f"{k['ism'].title()} {k['tyil']}-yilda tug\'igan "
#           f"va {k['vyil']-k['tyil']} umur kurgan")

# grandpas[0]['asari']='albxoriy'
# grandpas[1]['asari']='alqodiriy'
# grandpas[2]['asari']='alvohidiy'
# grandpas[3]['asari']='alnavoiy'

# for k in grandpas:
#     ism = k['ism']
#     asari=k['asari']
#     print(ism, asari)

# davlatlar = {
#     "o'zbekiston": {
#         "poytaxt": "toshkent",
#         "maydon": 448978,
#         "aholi": 33_000_000,
#         "pul birligi": "so'm",
#     },
#     "rossiya": {
#         "poytaxt": "moskva",
#         "maydon": 17_098_246,
#         "aholi": 144_000_000,
#         "pul birligi": "rubl",
#     },
#     "aqsh": {
#         "poytaxt": "vashington",
#         "maydon": 9_631_418,
#         "aholi": 327_000_000,
#         "pul birligi": "dollar",
#     },
#     "malayziya": {
#         "poytaxt": "kuala-lumpur",
#         "maydon": 329750,
#         "aholi": 25_000_000,
#         "pul birligi": "rinngit",
#     },
# }
# order = input('Qaysi mamlakat haqida malumot izlaybsiz \n >>> ').lower()

# for k , v in davlatlar.items() :
#     if order in k :
#         print(order.upper() , 'ning')
#         for nom , mal in v.items() :
#             print(f'{nom.title()} ---> {mal}')
#     else :
#         print(f'sorry we dont have info about {order}')


# if order in davlatlar :
#    print(order.upper() , 'ning')
#    for nom , mal in davlatlar[order].items() : # mendan dangasa odam yuq 
#         print(f'{nom.title()} ---> {mal}')
# else :
#     print(f'sorry we dont have info about {order}')


# davlat = input("Davlat nomini kiriting: ").lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(
#         f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#         f"\nHududi: {info['maydon']} kv.km"
#         f"\nAholisi: {info['aholi']}"
#         f"\nPul birligi: {info['pul birligi']}"
#     )
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")


#             lesson 17 ( while ) https://quizlet.com/_dfd57j?x=1jqt&i=52phgt

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



















