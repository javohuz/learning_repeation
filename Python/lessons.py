# -*- coding: utf-8 -*-
# """
# easy stuffs just for repeation 

# """  
# python 

#                                  lesson4


# o'zgaruchilar ustida amallar -> uzgaruvchi uzi nima va nimaga kerak 
# uzgaruvchilar shuchaki kichkila lotin haru=iflari bilan yasaladi masaln (ism)
# ularni ularni birmarta tanlab quyib keyin ishlaturamiz 

# ism="something" => yasalishi shunaqa yana joy tashlash mumkun emas urniga __
# mavzularni takrorlash uchun link
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

# # .starswith(smt) smt qandaydir  harf agat matn smt bn boshlangan bulsa 
# # True qiymat qaytaradi else False
# my_friends=['Jasur', 'Abbi' , 'Avaz' ]
# x=[]
# for my_friend in my_friends:
#     x.append(my_friend.startswith('A'))
#     print(x)
    
# for me new metods are append , insert , romove , pop and new aperator is del.

#                        AMALYOT

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


#         lesson 19 funksiyalar    https://quizlet.com/_dfgct2?x=1qqt&i=52phgt

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

#                           lesson 23  modullar

# Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida
#   yashirishimiz va kerak bo'lgan murojat qilishimiz mumkinligida. Maqsadimiz
#   dasturimizni ixcham va tushunarli qilib, kelajakda o'zimiz yoki boshqalar 
#   uchun ham "toza" kod qoldrisih. Bu yo'nalishda yana bir qadam qo'yib, 
#   dasturimizni modullarga ajratimshimiz mumkin. 

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")


# import bu 1- fayldagi kodni 2-chisiga imposrt qilish uchun use buning uchun 
# ikala kod yozilgan fayllar bitta papkani ichiki bulishi kk
 
# import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

# import smt as smt funksiya nomini har doim yozib yotish shart emas uni boshqa nomga birlashtrsa buladi

# import avto_info_mod as aim
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)

# modulni ichidagi functions ni asosiy koodga kuchirib oslish

# from avto_info_mod import avto_info, avto_kirit ,info_print
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# agar funksiya nomini kodda yana ishlatadigan bulsak finction nomi uzgartrish can

# from avto_info_mod import avto_info as ai , avto_kirit as ak , info_print as ip
# avto1 = ai("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# ip(avto1)



# * modul ichidagi functions ni bitta chiqarim oladi lekin bu kichik modullar uchun 
# katto modullarda hamma funksiyalar kup bulishi umkun bu esa dastur sekin 
# ishlashi yoki birxil nomli uzgaruvchilar hosil bulib dasturn hato ishlashi mumkun 


# from avto_info_mod import *
# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

# python tayyor modullar ruyhati => https://docs.python.org/3/py-modindex.html
#   foydali modullar
# import math 
# print(math.pow(3,4))
# print(math.sin(0.5))
# print(math.sqrt(100))


# import random  as r

# randint(a,b)  # rendit  a va b oralig'ida tasodifiy son
# son = r.randint(0,100) 
# print(son)

# choice(list) list ichidan rendomly tanlaydi
# sonlar =list(range(2,30,2))
# x = r.choice(sonlar)   
# print(x)

# shuffle(x) x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya
# listni mixed qiladi
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# sample(population, k) => population ruyhatdan k ta sini tanlab oladi list shaklida 
# sonlar = r.sample(range(1000),10 )
# print(sonlar)

#                               lesson 24 nomsiz funksiya


# lambda =>Pythonning o'ziga xos xususiyatlaridan biri, nomsiz vaqtinchalik
# funksiyalar yaratish imkoniyati. Bunday funksiyalarni yaratishda def
# operatori o'rniga lambda operatori ishlatilgani uchun ham lambda funskiyalar
# deb ataladi


# x = int(input("any numcer = "))
# son = lambda x : x**2  # nomsiz funktsiyaga nom berdik 
# print(son(x))


# funktiya yasovchi funksiya

# def any_numbers (n ):
#     return lambda x :x**n

# son = any_numbers(2)
# son (8)

#   map() FUNKSIYASI =>Bu funksiya argument sifatida ro'yxat (yoki lug'at) va
# boshqa bir funksiyani qabul qilib, ro'yxat elementlariga qabul qilingan
# funksya yordamida ishlov beradi
# map(a,b) a biron funksiya b list or dict , list or dict ni qiymatini a ga junatadi

# sonlar=list(range(10))
# son_kvadrati = list(map(lambda x :x**2 , sonlar))
# print(sonlar)
# print(son_kvadrati)

# from math import sqrt

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz

# map funksiyasi orqali bir nechta qiymatalr junatish
# a = list(range(5))
# b = list(range(6,11))
# print(a,'\n',b)
# print(list(map(lambda x,y : x*y , a , b)))

# map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:
# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda take :take.upper(),ismlar)))

# filter(a,b) funksiyasi map() ga uhshiydi a funksiya bilan b ni tekshiradi
# true bulda yoki a funk ni qanoatlantirsa qabul qiladi else unkazmakdi
 
# import random  as r
# sonlar = r.sample(range(1000),10 )
# print(sonlar)

# def juft(n):
#     return n%2==0

# juft_sonlar = list(filter(juft,sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda n:n%2==0,sonlar))
# print(juft_sonlar)

# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

# mevalar_b = list(filter(lambda matn : matn.startswith('o'),mevalar))
# print(mevalar_b)


# .startswith(smt) smt qandaydir harf agat matn smt bn boshlangan bulsa 
# True qiymat qaytaradi else False


#                          mustaqil ish lesson 25 

# """
# son topish uyini 

# @author: User rashidovj
# """

# import random as r
# print('Salom son topish uyini uynaymiz ')
# while True :

#     k = r.choice(list(range(1,11)))
#     user = int(input('1 dan 10 gacha son uyladim topishga harakat qiling \n >>> '))
#     soni =[]
#     soni.append(user)
    
#     while k!=user :
        
#         if k > user :
#             user=int(input('XATO!, Men uylagain son bundan kata , yana harakat qilib kuring >> '))
#             soni.append(user)

#         if k < user :
#             user=int(input('XATO!,Men uylagain son bundan kachik , yana harakat qilib kuring >> '))
#             soni.append(user)

        
#     print(f"Tabreklayman {len(soni)} urinishida topdingiz men {k} sonini uylagan edim !!!")
#     print('Endi sizni galingiz 1 dan 10 gacha son uylang ')
#     keraksiz=input('agar uylagan bulsangiz istalgan tugmani boshing : ')
    
#     soni2=[]
#     x=1
#     y=10
#     while True :

#         n = r.randint(x,y)
#         soni2.append(n)
#         check = input(f'siz {n} sonini uyladingiz , agar tugri bulsa (t) , katta bulsa (+) , kichik bulsa (-) ni bosing > ')


#         if check=='+' :
#             x=n+1
                
#         elif check=='-':
#             y=n-1
#         else:
#             break
        
#     b = len(soni2)
#     a=len(soni)
#     if a>b :
#         print(f'YUTQAZDINGIZ !!! \n Siz {a} ta urinishda toptingiz men esa {b} ta shunish uchun yutqazdingiz ')
#     elif a<b:
#         print(f'QOYIL YUTDINGIZ  !!! \n Siz {a} ta urinishda toptingiz men esa {b} ta shunish uchun YUTDINGIZ ')
#     else :
#         print(f'DURRANG ! urinishlar soni teng yani {a} tadan')
    
#     stop = input('Yana uynashni hohlaysizmi yes/no : ')
#     if stop=='no' :
#         break

# """                        lesson 28 class
#  OOP obyektga yunaltrilgan dasturlash
# """
# # https://quizlet.com/812922417/oop-flash-cards/?i=52phgt&x=1qqt

# """ 
# obyekt nima => obyekt bu bir nechta funksiyalar va uzgaruvchilar jamlanmasi 
# class nima => class bu obyekt yaratish ycun shablon 
# """

# """ 
# obyekt yaratish uchun birinchi class yash kk chunki class obyekt uchun qolib 
# """

# class BIO:   
#     def __init__(self,name,familiya,yosh):#__init__ yzilishi kk
#         self.name = name
#         self.familiya= familiya
#         self.yosh=yosh
#         self.tyil = 2004
        
#     def tanishtir(self):# buyerda self obyektni ichidagilrni uiga yukliydi
#         tanishtir=f'my name is {self.name}'
#         return tanishtir

#     def get_tyil(self,yil):
#         return yil-self.yosh
    
    
# info1=BIO('Jasur','rashidov',19)
# info2=BIO('Javohir','rashidov',19)
# info3=BIO('Nurbek','rashidov',16)
# info3.yosh
# print(info1.tanishtir())
# print(info2.get_tyil(2023))

# """
# __init__(self,a,b,c,d)  init xsusyatlarni yozish uchun
# a,b,c,d lar buyerda xsusiyatlari
# self obyektning xsusiyatlariga murojat qilishimiz uchun yani self manisi uzi 
# xsusiyatlarni nomini ( uzin uziga yuklash uchun )
# def __init__(self) — klassga tegishli xususiyatlarni saqlovchi maxsus metod 
# (funksiya). self kalit so'zi ingliz tilidan "o'zi" deb tarjima qilinadi,
#   va bu klassdan yaratilgan obyektning o'ziga ishora qiladi. Ya'ni keyinchalik
#   biz obyekt ichidagi metodga murojat qilganimizda shu obyektning o'zi birinchi 
#   bo'lib funksiyaga argument sifatida uzatiladi, obyket ustida turli amallar
#   bajarish imkonin beradi
# """

# """                 Amalyot                      """


# class user:
#     def __init__(self,nick,name,age,email,exemail=None):
#         self.nick =nick
#         self.name = name
#         self.age = age
#         self.email = email
#         self.exemail =exemail
        
#     def info(self):
#         return f'foydalanivchi {self.nick}, ismi:{self.name.upper()},yoshi :{self.age},email :{self.email} , exemail : {self.exemail} '

# user1 = user('javohir5266', 'javohir',19,'rashidovjavohir33@gmail.com')
# user2 = user('jasur5266', 'jasur',19,'rashidovjavohir33@gmail.com')

# print(user2.info())


# """                 lesson 29 obyektlar                         """

# """ qiymatlarni (smt.yosh) yuli bn chaqirish mumkun lekin bu tafsiya qilinmaydi bu 
# faqat python tiliga mos ularni chaqirish uchun alohida metod chaqirish kk 
# """

# class BIO:   
#     def __init__(self,name,familiya,yosh):#__init__ yzilishi kk
#         self.name = name
#         self.familiya= familiya
#         self.yosh=yosh
#         self.bosqich = 1  # standard qiymat
        
#     def tanishtir(self):# buyerda self obyektni ichidagilrni uiga yukliydi
#         tanishtir=f'my name is {self.name}'
#         return tanishtir
    
#     def set_bosqish(self,new_bosqich):
#         """ set_smt bu hsusiyatni uzgartrish uchun """
#         self.bosqich=new_bosqich
    
#     def get_name(self):
#         """get_smt bu kk li hsusiyatni chaqrib olish uchun """
#         return self.name
#     def get_fullname(self):
#         return f'{self.name} , {self.familiya}'
    
#     def  update_bosqich(self):
#         """ update_smt bu qandaydir amal bajaradi yoki update qiladigan """
#         self.bosqich += 1
    
#     def get_yosh(self):
#         return self.yosh
        
# """
# get_smt , set_smt , update_smt => bular shunchaki nom yuqoridagi vazifalarni 
# bajarayotganda shulardan foydalanish tafya qilinadi
# """

# info1=BIO('Jasur','rashidov',19)
# info2=BIO('Javohir','rashidov',19)
# info3=BIO('Nurbek','rashidov',16)

# info3.get_name()
# info2.get_yosh()

# info3.update_bosqich()

# info2.set_bosqish(3)
# info3.bosqich

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar = []
#         self.talaba_soni = 0

#     def add_talaba(self,talaba):
#         """talaba qushish """
#         self.talabalar.append(talaba)
#         self.talaba_soni += 1 
        
#     def get_talaba(self):
#         # talaba_name =[]
#         # for talaba in self.talabalar:
#         #     talaba_name.append(talaba.get_fullname().title())
#         # return talaba_name
#         return [talaba.get_fullname().title() for talaba in self.talabalar ]
    

# matem = Fan('Matematika')
# matem.add_talaba(info1)
# matem.add_talaba(info2)
# matem.get_talaba()

# """
# dir() FUNKSIYASI
# dir() funksiyasi yordamida istalgan obyekt yoki klassning xususiyatlari va 
# metodlarini ko'rib olishimiz mumkin:
# """
# dir(BIO)

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(BIO),dir(BIO))

# """                         amalyot                     """

# class Avto():
#     def __init__(self, model, rang, karobka ,narx ):
#         self.model =model
#         self.rang =rang
#         self.karobka = karobka
#         self.narx=narx
#         self.kilometr = 0
    
#     def get_model(self):
#         return self.model
    
#     def get_rang(self):
#         return self.rang
    
#     def get_karobka(self):
#         return self.karobka
    
#     def get_narx(self):
#         return self.narx
    
#     def set_kilometr(self,kilometri):
#         self.kilometr = kilometri
        
#     def update_narx(self,foizi):
#         """avtomobil narxi % uzgarganini hisoblaydi agar kamaygan bulsa (-) ishora bilan yozing"""
#         self.narx += self.narx*foizi/100
    
#     def get_avto_info(self):
#         return f' Modeli : {self.model.title()} \n Rangi : {self.rang} \n Karobkasi : {self.karobka} \n Narxi : {self.narx} \n Yurilgan kilometri : {self.kilometr} '

# avto1 = Avto('jentra','oq','mexanik',15000)
# avto2 = Avto('jentra','qora','mexanik',15000)
# avto3 = Avto('jentra','qora','avtomat',17000)
# avto4 = Avto('jentra','qora','avtomat',17000)
# avto5 = Avto('jentra','qora','avtomat',17000)
# avto6 = Avto('jentra','qora','avtomat',17000)
# avto7 = Avto('jentra','qora','avtomat',17000)
# avto8 = Avto('jentra','qora','avtomat',17000)
# avto9 = Avto('jentra','qora','avtomat',17000)

# avto1.get_narx()
# avto2.update_narx(-10)
# avto2.get_narx()
# avto1.set_kilometr(5000)
# # print(avto1.get_avto_info())

# class Avtosalon():
#     def __init__(self,salon_nomi , salon_manzili , avtamobillari  ):
#         self.salon_nomi =salon_nomi
#         self.salon_manzili = salon_manzili
#         self.avtamobillari = [avtamobillari]
    
#     def add_car(self, new_car):
#         return self.avtamobillari.append(new_car) 
    
#     def get_cars(self):
#         return self.avtamobillari
    
#     def get_info(self):
#         car_list = [ car_info.get_avto_info() for car_info in self.avtamobillari ]
#         n=len(car_list)+1
#         info = []
#         while car_list : 
#             n-=1
#             x= f'     car{n} \n{car_list.pop()}'
#             info.append(x)
#         return info
            
# avto6.update_narx(50)
# salon1 = Avtosalon('GM', 'Andijon', avto1)
# salon1.add_car(avto2)
# salon1.add_car(avto3)
# salon1.add_car(avto4)
# salon1.add_car(avto5)
# salon1.add_car(avto6)
# salon1.add_car(avto7)
# salon1.add_car(avto8)
# salon1.add_car(avto9)


# for x in salon1.get_info():
#     print(x)

# print(dir(Avto),'\n',dir(Avtosalon),Avto.__dict__)



# """                         lesson 30                         

# vorislik va polimorfizm => vorislik bu otak class or( super class ) dan yaratilgan 
# yangi class polimorfizm bu yangi classda sper klassning funksiyalarni uzgartrish 
# """

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
    
# """ Voris yasash """

# class Talaba(Shaxs): # shaxs ni metodlarini meros qil
#     def __init__(self ,ism, familiya, pasport , tyil , idraqam , manzil):
#         """Talaba haqida malumot """
#         super().__init__(ism,familiya,pasport,tyil) 
#         self.idraqam = idraqam
#         self.bosqich = 1 
#         self.manzil = manzil

#""" super().__init__(ism,familiya,pasport,tyil) == 
#        { self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil} """


#     def get_id(self):
#         return self.idraqam
    
#     def get_bosqich(self):
#         return self.bosqich
    
#     def set_bosqich(self,new_corse):
#         self.bosqich = new_corse

# # """ polimorifzm yani super fazadagi metodni uzgartiramiz shu """
        
#     def get_info(self): 
#         """Talava haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Bpsqich:{self.bosqich} , ID_raqam: {self.idraqam}"
#         return info
    
        
# """ buyerda Talaba voris ,Shaxs super class , super() => vazifasi super classdan 
# __init__ ichida kiritilgan qiymatlarni super classdan meros qiladi va super class
# ning metodlari voris klacda ham ishlaydi
# Yana istalgan class boshqa class uchun super class bulishi mumkun 
# Birvaqqtda bitta klasda 2 ta super class ni voris qilish mumkun faqat kod
# murakkablashadi bu usul unchalik tavsiya qilinmaydi
# """

# """ bazida classning xsusiyatlari kupayib ketishi mumkun bu xatalikka yoki 
# noqulaylikka olib kelishi mumkun bu hollarda yangi class yaratib u klasning 
# malumotlarini boshqa klacda foydalanish mumkun 
# """
# # Talaba klasiga manzil degan xsusiyat qushdik 
# class Manzil:
#     def __init__(self,uy,kuchasi,tuman,viloyat):
#         self.uy=uy
#         self.kuchasi = kuchasi
#         self.tuman = tuman 
#         self.viloyat =viloyat
    
#     def get_manzil(self):
#         manzil= f'{self.uy}-Uy , Ko\'chasi : {self.kuchasi} ,'
#         manzil += f"Tumani : {self.tuman} , Vilayati : {self.viloyat}"
#         return manzil

# talaba1_manzil= Manzil(17 ,'Zamondosh','SHahrizabz','Qashqadaryo' )
# talaba1 = Talaba('Javohir','Rashidov','AD0056845',2004,'N00011251',talaba1_manzil)
# talaba1.manzil.get_manzil()


# """                     Amalyot                             """


# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil


# class Talaba(Shaxs): 
#     def __init__(self ,ism, familiya, pasport , tyil , idraqam ,fanlar):
#         """Talaba haqida malumot """
#         super().__init__(ism,familiya,pasport,tyil) 
#         self.idraqam = idraqam
#         self.bosqich = 1 
#         self.fanlar = []
        
#     def get_id(self):
#         return self.idraqam
    
#     def get_bosqich(self):
#         return self.bosqich
    
#     def set_bosqich(self,new_corse):
#         self.bosqich = new_corse
        
#     def get_info(self): 
#         """Talava haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Bpsqich:{self.bosqich} , ID_raqam: {self.idraqam}"
#         return info
    
#     def fanga_yozil(self,fan):
#         return self.fanlar.append(fan)
    
#     def remove_fan(self,x_fan):
#         if x_fan not in self.fanlar :
#             natija= f'Siz {x_fan} faniga yozilmagansiz ' 
#         else :
#             natija=self.fanlar.remove(x_fan) 
#         return natija
    
# class Fan():
    
#     def __init__(self,fan):
#         self.fan = fan
        
#     def get_fan(self):
#         return self.fan
    
    
# fan1 = Fan('Matematika')
# fan2 = Fan('Fizika')
# talaba1 = Talaba('Javohir','Rashidov','AD0056845',2004,'N00011251',"fanlar")

# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)

# talaba1.remove_fan(fan1)
# print(talaba1.fanlar)

# class User(Shaxs):
#     def __init__(self,ism,familiya,passport,tyil,idraqam):
#         super().__init__(ism,familiya,passport,tyil)
#         self.idraqam = idraqam
#     def get_info(self): 
#         """Talava haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"ID_raqami: {self.idraqam}"
#         return info
    
# user1 = User('Javohir','Rashidov','ND15641540',2004,323211112200)
# user1.get_info()

# class Admin(User):
#     def __init__(self,ism,familiya,passport,tyil,idraqam):
#         super().__init__(ism,familiya,passport,tyil,idraqam)
    
#     def ban_user(self,user_name):
#         return f'{user_name} bloklandi'
    
# user2 = Admin('Javohir','Rashidov','ND15641540',2004,323211112200)
# user2.ban_user('Javohir')

# """                          lesson 31 
# INKAPSULYATSIYA
# Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya
#   ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat 
#   qilishni va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda 
#   bunday yopiq xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi: 
# """
# """ uuid  moduli ning uuid4 funksyasi orqali id raqam olish mumkun id raqam har
#   doim turlicha buladi from uuid import uuid4
# """
# """ klaslarning yana qulayliklaridan biri uzgarmas xsusiyatlar qushishimiz 
# mumkun yani __init__ qilib hsusiyat qushmasdan uzgarmasni __init__dan oldin 
# yozishimiz kerak """

# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     __number_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__number_avto +=1
        
# # """yuqpridi Avto,number_avto +=1 har safar classdan foydalanganda 1 qushadi"""
 
#     def add_km(self,km):
#         if km >= 0:
#             self.__km + km
#         else :
#             print('avtomobil km ni kamaytrib bumaydi')
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__number_avto 
    
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.get_num_avto())


# """ class larni modul qilish huddi funksiyaday amalga oshiriladi faqat class  
# nomi bn chaqiriladi """ 



# """                          amalyot                                        """


# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     __shaxs_soni = 0
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#         Shaxs.__shaxs_soni +=1 
        
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
    
    
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
#     @classmethod
#     def get_Shaxs_num(cls):
#         return cls.__shaxs_soni
        
# talaba1 = Shaxs('Javohir','Rashidov','AD0056845',2004)
# talaba1.get_Shaxs_num()


# """                          lesson 32                              """

# """MAXSUS METODLAR    double underscore yoki qisqa qilib dunder 
# Dunder metolar yordamida obyektlarga qo'shimcha qulayliklar va vazifalar 
# qo'shishimiz mumkin. Klass yoki obyektga oid dunder metodlar ro'yxatini ko'rish
# uchun dir() funksiyasidan foydalanamiz:
# """
# """
# __init__ Bu metod klassdan obyekt yaratishda chaqiriladi va obyektning 
# xususiyatlarini belgilaydi
# """

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narh
#         Avto.__num_avto += 1
        
# # """ __str__ dunder motodi bu metod orqali obyektni biz hohlhlagandek chaqiradi 
# # yani obyektga murojan qilganimizda biz kititgan kodni qaytaradi """

#     def __str__(self):
#         return f"Avto : {self.make} , {self.model} "
    
#     def __repr__(self):
#         """ obyekt haqida malumot qaytaradi """
#         return f"Avto : {self.make} , {self.model} "

# # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # print(avto1)

# # """ yani oldin obyektga mirojat qilganimizda mana bunday mal qaytarardi 
# # <__main__.Avto object at 0x00000277A4127610> , endi , obyektga mirojat qilsak 
# # Avto : GM , Malibu """
# # __str__ == __repr__ ikalasni vazifasi bir lekin __repr__ tavsiya qilinadi
# # murojat qilish uchun print() yoki str(object) agar __repr__ bulsa repr(object) deb

# #  """ taqqoslash metodlari ular oltita yani hammasni >= == ... 
# # x.__lt__(self,y)  =>  x<y
# # x.__le__(self,y)  =>  x<=y
# # x.__gt__(self,y)  =>  x>y
# # x.__ge__(self,y)  =>  x>=y
# # x.__eq__(self,y)  =>  x==y
# # x.__ne__(self,y)  =>  x!=y

# # lekin kodda ularni  armini yozish kifoya 
# # yani < ekanligini bilsa > ni ham biladi teskarisini oladi """

#     def __eq__(self,y):
#         return self.narx == y.narx
    
#     def __gt__(self,y):
#         return self.narx > y.narx
    
#     def __ge__(self,y):
#         return self.narx >= y.narx

# # avto1 = Avto("GM","Malibu","Qora",2020,40000)
# # avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# # print(avto1<avto2)

# """ new matod obyektni klassga tegishli yoki yuligini tekshiradi 
# isinstance(obyekt,class) 
# isinstance(avto1, Avto) """

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self,index):
#         return self.avtolar[index]
    
#     def __setitem__(self,index,qiymat):
#         self.avtolar[index] =qiymat

#     def add_avto(self,*qiymat):
#         for avto in qiymat :
#             if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyketini kiriting")
            
#     def __call__(self,*new_info):
#         if new_info:
#             for avto in new_info:
#                 self.avtolar.append(avto)
                
#         return [avto for avto in self.avtolar]
       
#     def __add__(self,y):
#         if isinstance(y,AvtoSalon):
#             new_one = AvtoSalon(f" {self.name} {y.name}")
#             new_one.avtolar = self.avtolar + y.avtolar
#             return new_one
#         elif isinstance(y,Avto ):
#              self.avtolar.append(y)
            
            
# salon1 = AvtoSalon("GM")
# # Avto obyektlarini yaratamiz
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)

# salon1.add_avto(avto1 , avto2 )
# salon1[:]

# salon1[1]=avto3
# len(salon1)
# # salon1(avto4 , avto5 , avto6)
# salon2=AvtoSalon('BMW')
# salon2(avto4 , avto5 , avto6)
# salon3 = salon1+salon2
# print(salon3,salon3())

# # """
# # __getitem__ bu lugat bulsa ushani kiritilgan index qiymatini chiqaradi 
# # __setitem__ kiritilgan index qiymatini urnatadi 
# # __len__  len() metodi ishlatilganda __len__ ichidagi kodni chiqaradi
# # __repr__ obyektga mirojat qilganda biz hohlagan malumotni chiqaradi or __str__
# # __call__ obyektni chaqiradigan yani salon1() qilganda malum bir funksiya 
# # bajaradigan yoki biz hohlagan matnni qaytaradigan qilishimiz mumkun 
# # mat amallar bajarish metodlarin 
# # __add__ ==> ( + )
# # __sub__ ==> ( - )
# # __mul__ ==> ( * )
# # __div__ ==> ( : )
# # __pow__ ==> ( ** )
# # """

# """                              Amalyot                         """



# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

#     def __repr__(self):
#         return f"{self.ism} ismli shaxs"


# class Talaba(Shaxs): 
#     def __init__(self ,ism, familiya, pasport , tyil , idraqam ,fanlar):
#         """Talaba haqida malumot """
#         super().__init__(ism,familiya,pasport,tyil) 
#         self.idraqam = idraqam
#         self.bosqich = 1 
#         self.fanlar = []
        
#     def get_id(self):
#         return self.idraqam
    
#     def get_passport(self):
#         return self.passport
    
#     def get_bosqich(self):
#         return self.bosqich
    
#     def set_bosqich(self,new_corse):
#         self.bosqich = new_corse
        
#     def get_info(self): 
#         """Talava haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Bpsqich:{self.bosqich} , ID_raqam: {self.idraqam}"
#         return info
        
#     def fanga_yozil(self,fan):
#         return self.fanlar.append(fan)
    
#     def __eq__(self,y):
#         return self.bosqich == y.bosqich
    
#     def __lt__(self,y):
#         return  self.bosqich < y.bosqich
    

# class Fan:
#     def __init__(self,name_fan):
#         self.name_fan = name_fan
#         self.talabalar = []

#     def add_talaba (self,*talabalar):
#         for talaba in talabalar :
#             self.talabalar.append(talaba)
    
#     def __repr__(self):
#         return self.name_fan
    
#     def __call__(self,*y):
#         for c in y :
#             if isinstance(c,Talaba):
#                 self.talabalar.append(c)
#         return self.talabalar
    
#     def __getitem__(self,index):
#         return self.talabalar[index]
    
#     def __setitem__(self,index,new_one):
#         self.talabalar[index]=new_one
    
#     def __len__(self):
#         return len(self.talabalar)
    
#     def __add__(self,y):
#         if isinstance(y,Talaba):
#             return self.talabalar.append(y)
#         elif isinstance(y,Fan):
#             new_fan = Fan(f"{self.name_fan} va {y.name_fan}")
#             new_fan.talabalar = self.talabalar + y.talabalar
#             return new_fan
   
#     def __sub__(self,y):
#         for talaba in self.talabalar :
#             if talaba in y :
#                 return self.talabalar.remover(talaba)

# shaxs1 = Shaxs('Javohir',"Rashidov","AD4324686",2004)
# talaba1 = Talaba('Javohir',"Rashidov","AD4324686",2004,"AD6726773","matem")
# talaba2 = Talaba('Jasur',"Rashidov","AD4324686",2004,"AD6726773","matem")
# print(talaba1==talaba2)
# talaba2.set_bosqich(4)
# print(talaba1<talaba2)
                
# fan1 = Fan("Matem")
# # fan1.add_talaba(talaba1)
# fan2 = Fan ('fizika')
# # fan1(talaba2)
# # fan1[1] = talaba1
# # fan1[1]
# # len(fan1)


# fan1+talaba2
# fan2+talaba1

# fan3 = fan1+fan2
# fan3()
# fan3-'AD4324686'
# fan3()


# """                         lesson 33                                       """

# """ falylardan katta hajmdaki mulumotlarni yuklab undan dasturda foydalanish 
# mumkun tayyor faylni ochish uchun open('file_name') funksiyasidan can use 
# file ichidagi malumotni uqish uchun .read() funksiysidan foydalaniladi
# dastrun ohirida filene close() funk bn yopish kerak else file shikas yeydi
# fileni uqish uchun ular bir papkad bulishi kk 
# """

# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

# """ yuqoridagi usul orqali fileni chaqrib undan can use lekin bu usul tafsiya qilinmaydi 
# """

# with open('pi.txt') as file :
#     pi = file.read()

# print(pi)

# """ ikkalal usul ham bir vazifani bajaradi lekin with funksiyasi tafsiya qilinadi 
# with operatorining vazifasi biz fayl bilan ishlab bo'lganimizdan so'ng faylni
#   yopish. Yuqoridagi misolda, 2-qatordan so'ng Python zudlik bilan faylni yopadi.
 
#   malumotga ishlob berish metodlari
#   .rstrip() => qator ohiridagi bo'shliqlarni olib tashlaymiz
#   .replace('\n','') => qator tashlash belgisini almashtiramiz
# """

# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)

# """ fayl ichidan fayl malumotlarini olish ucni file nomi / keyin kkli file nome 
# """

# # #  fileni qatorma qator uqish uchun 
# # filename = 'data/talabalar.txt'
# # with open(filename) as file :
# #     for line in file:
# #         print(line)
        
# """       
# file ichidagi malumotlarni list kurinishida saqlash
# .readlines() => Qatorlarni ro'yxat ko'rinishida saqlab olish uchun
# """  

# filename = 'data/talabalar.txt'
# with open(filename) as file :
#     talabalar = file.readlines()
    
# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)


# """ 
# yangi file yaratish     with open(file_name,'w') as file: => "w" - write
# 'w'agar file biz yaratmoqshi bulgan file nomi avval mavjud bulgan bulsa 
# fileni uchirib tashlaydi
# filega mlumot qushish   with open(file_name,'a') as file: => "a" - append
# "a" yani filega malumot qushmoqchi bulsagu file mavjud bulmasa new file ochadi
# """
# # yangi file yaratish
# file_name = 'new_file.txt' 
# ism = 'javohir rashidov'
# tyil = 2004
# with open(file_name,'w') as file:
#     file.write(ism +'\n')
#     file.write(str(tyil)+'\n')
    
# # filega mlumot qushish
# with open(file_name,'a') as file:
#     file.write( 'javohir rashidov')
#     file.write('2004')

# """ yuqoridagilar faqat matn shaklida edi yani str , filega uzgaruvchi yoki 
# boshqaobyekt yoki dict larni qushishni kuramiz bunish uchun pickle modulidan 
# foydalanamiz tarjimasi kanservalash Pickle ma'lumotlarni biz qanday ko'rinishda
# bersak, shunday ko'rinishda faylga yozadi. Yuqoridagi usuldan farqli ravishda, 
# pickle yordamida yozilgan fayllarning tarkibini Pythondan tashqarida cant see
# """
# import pickle

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info' , 'wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)
    
# """ 'wb' ( write binery) 2li sanoq setemasida saqla 
# pickle dan malumot uqish Pickle fayldan o'qish uchun open() funksiyasini
#   'rb' (read binary) argumenti bilan chaqiramiz. 
# """

# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
    
# print(talaba1)


# """                              Amalyot                         """

# with open('pi_million.txt') as file:
#     pi = file.read()
    
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# print(pi)
    
# with open('pi_million.txt') as file:
#     for line in file:
#         print(line)
    
# with open('pi_million.txt') as file:
#     qatorlar = file.readlines()
#     qatorlar = [qator.rstrip() for qator in qatorlar]
# print(qatorlar)
    
# with open('pi_million.txt') as file:
#     pi = file.read()
    
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = pi.replace(' ','')
# print(pi)
# my_day = '020504'

# if my_day in pi:
#     print('ha')
# else:
#     print('no')
    
# import pickle

# pi = float(pi)
    
# with open('info_dat','wb') as file:
#     pickle.dump(pi,file)
    

# with open('info_dat','rb') as file:
#     pi = pickle.load(file)
    
# print(pi)

# """                             lesson 34                                   """


# """ 
# JSON (JavaScript Object Notation) bugungi kunda ma'lumotlarni saqlash va internet
#  orqali uzatish uchun qo'llaniladigan eng mashxur format hisoblanadi.
#  """

# import json
# x=5
# x_json = json.dumps(x)

# ism = "Javohir"
# ism_json = json.dumps(ism)

# sonlar = [12, 45, 23, 67]
# sonlar_json = json.dumps(sonlar)

# m = True
# m_json = json.dumps(m)

# """
#  json.dumps(x) — berilgan x o'zgaruvchini JSON matniga o'zgartiradi
#  json.dump(x,fayl) — berilgan x o'zgaruvchini JSON ga o'zgartirib, ko'rsatilgan faylga saqlaydi.
#  jsonga yuklangan malumotlar avvlar javascript tiliga utkazildi keyin matnga utgaziladi 
# """

# bemor = {
#   "ism": "Alijon Valiyev",
#   "yosh": 30,
#   "oila": True,
#   "farzandlar": ("Ahmad","Bonu"),
#   "allergiya": None,
#   "dorilar": [
#     {"nomi": "Analgin", "miqdori": 0.5},
#     {"nomi": "Panadol", "miqdori": 1.2}
#   ]
# }

# # bemor_json = json.dumps(bemor)

# bemor_json = json.dumps(bemor , indent=4)

# # print(bemor_json)
# """ indent=a  a any number jsonga  malumot yuklanayotganda har bir list ili dickt 
# boshlanish oldidan a ta joytashlaydi sal tshunarli tartibda buladi 
# """ 

# """
# json ni file shaklida saqlash bunish uchun .dumps()ni urniga ,dump() use
# """

# with open('bemor.json' , 'w') as file :
#     json.dump(bemor,file)

# """ 
# jsonga utkazilgan malumotlarni qaytarib python tiliga utkazish uchun .loads() use
# """
# bemor1= json.loads(bemor_json)

# """
# json kurinishida fileni oshishni uchun .load() foydalanamiz 
# """
# with open('bemor.json' ) as file:
#     bemor = json.load(file )

# # print(bemor)


# """                               Amalyot                                   """

# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

# data_json = json.dumps(data)

# data1= json.loads(data_json)

# with open('data.json' , 'w') as  file:
#     json.dump(data,file)
    
# with open ('data.json') as f:
#     data =  json.load(f)


# print(data)

# with open('any_file' ,'w') as file:
#     file.write('someone' +'\n' )
#     file.write('2020')


# with open('any_file') as file:
#     ism = file.readlines()

# print(ism)

# with open('students.json' ) as f :
#     students = json.load(f)


# for student in students['student']:
#     name = student['name']
#     lastname = student['lastname']

# with open('studentlar' , 'w') as file:
#     for student in students['student']:
#         name = student['name']
#         lastname = student['lastname']
#         file.write(name+' ')
#         file.write(lastname + '\n')
        
# with open('studentlar') as f :
#     student_name = f.readlines()

# print(student_name)


# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# students

# data_json = json.dumps(data)
# students_json = json.dumps(students)
# print(data_json)
# print(students_json)

# with open('ex_there.json' ,'w' ) as file :
#     json.dump(data,file )


# with open('ex_there.json') as file:
#     data_json = json.load(file)

# print(data_json)


# with open('students.json' ) as f :
#     students = json.load(f)
# talabalar = []

# for studentlar in students['student']:
#     name = student['name']
#     lastname = student['lastname']
#     id_numb = student['id']
#     year = student['year']
#     faculty = student['faculty']
#     talaba = f'{name.title()} {lastname.title()}  {year}-yildan beri {faculty} fakultatida uqiydi ' 
#     talabalar.append(talaba) 
        
        
# print(talabalar[1])       
        
        
# """                              lesson 35                                 """

# """
# pythonda kod xato bulganda yoki malumot qabul qilganda turli xil xatoliklar kelib 
# chiqishi mumkum misol uchun Run time error yoki shunga uhshash bu vaqtta dastur 
# ishlashdan tuhtaydi  buning oldini olish uchun try: except: else : operatorlaridan 
# foydalaniladi  
# """

# yosh = input('yoshingizni kiriting >> ')
# yosh = int(yosh)
# try :  
#     yosh = int(yosh) 

# except:
#     print('siz butun son kiritmadingiz ')
    
# else :  
#     print(f'siz {2023-yosh} yilda tugilgansiz ')
        
# """ try : => manosi harakat qil yani xatolik yuzaga kelishi mumkun bulgan kod yoziladi 
#     except : => agar try ichidagi kodda xatolik bulsa except ichidaki kod bajarildi
#     yana except KeyError : yani expect ichida kelib chiqadigan xatolikni nomini ham yozish 
#     mumkun bu holda except faqat kiritilgan xatolik bulganda bajarildi
#     else: => yani agar xatolik bulmasa else : ichidagi kod bajarildi 
    
# buning qulay tomini agar xatolik bulsa ham dasturn tuhtab qolmaydi yani 
# xato bulgan kodlar pastidagi kodlar bajarila veradi 
# """

# """
# bir nechta xatolar bn ishlash try-except ketma-ketligida bir nechta except
#  operatorlari ham bo'lishi mumkin. Ularning har biri ma'lum turdagi xatolik uchun 
#  javobgar bo'ladi:
# """
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")
        
        
# """ pass operatori => Hech qanday ma'lumot ko'rsatmay, dasturni davom etish uchun
#  pass operatoridan foydalanamiz.
# """  
# yosh = input('yoshingizni kiriting >> ')

# try :  
#     yosh = int(yosh) 
# except:
#     pass      
# else :  
#     print(f'siz {2023-yosh} yilda tugilgansiz ')
            
# """
# agar xatolikni oldini oshin mumkun bulsa (while , if ..) xatolikni oldini olygan yaxshiroq buladi   
# """       
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break        
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")      


# """                             lesson 38                                   """
    
# """ datetime Ushbu modul yordamida Pythonda sanalar bilan ishlashimiz mumkin"""
    
# import datetime as dt 

# hozir = dt.datetime.now()

# """agar kerakli vaqt kiritish kk bulsa qulda kiritamiz """
# ertaga = dt.date(2023,7,27)

# # print(hozir , ertaga)     
 
# print(hozir.date() , hozir.time()) 

# """ 
# dt.date.today() => agar faqat hozirgi kun kerak bulsa 
# dt.date.now()  => hozirgi vaqtni kun soat min sec ml sek bn chiqaradi 
# """

# qoldi = ertaga-hozir.date()
# # print(qoldi.days)

# aksiya = dt.datetime(2023,7,16,16,59,00,00)
# qoldi1= aksiya-hozir

# secondlar = qoldi1.seconds
# minutlar = int(secondlar/60)

# # print(minutlar)
# print(hozir.time())

# """ chala secundamer for 59 seconds """
# n= hozir.second
# while aksiya != hozir :
#     hozir = dt.datetime.now()
#     qoldi = aksiya -hozir
#     if  hozir.second > n :
#         n = hozir.second
#         print(qoldi)
#     else:
#         pass


# """ pprint malumotlarni tartiblab konsulga chiqaradi """
# from pprint import pprint
# import json 

# with open('bemor.json') as file:
#     bemor = json.load(file)

# pprint(bemor)


# """ 
# RegEx - ANDOZA YORDAMIDA MATN IZLASH 
# re (regular expressions) moduli.
# """
# import re

# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"

# andoza = "^т...р$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

# """
# So'zlarni andozaga solishtirish uchun re.match() funksiyasidan foydalanamiz.
#   Agar tekshirgan so'zimiz andozaga mosh tushsa, re.match() metodi so'zni o'zini 
#   qaytaradi, aks holda None qiymatini qaytaradi.
# """

# """
# andozalardan matndan uzimizga kerakli emile adres yoki sana shunga uhshash malumotlarni 
# sugurib olishmiz mumkun 
# https://ihateregex.io/ sahifasidan esa loyihangiz uchun tayyor andozalarni topishingiz mumkin. 
# """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)

# """
# Keling, yuqoridagi andoza asosida biror matndan email manzilini ajratib olamiz.
#   Buning uchun re.findall() funksiyasidan foydalanamiz
# """


# """                         practice                                        """

# import datetime as dt 

# now = dt.datetime.now()
# now_year = now.year
# now_month = now.month
# now_day = now.day

# for n in range(13):  
#     dates = dt.date( now_year , now_month , now_day)
#     print(dates)
#     now_day += 14
#     if now_day > 30:
#         now_month += 1
#         now_day -= 30

#     if now_month > 12:
#         now_year += 1
#         now_month -= 12
        
# a=int(input("tug'ilgan yilingizni kiriting > "))
# b=int(input("tug'ilgan oyingizni  kiriting > "))
# c=int(input("tug'ilgan kuninggizni kiriting > "))
# y = now_year-a
# m = now_month -b
# d = now_day -c
# if d<=0:
#     m -=1 
#     d +=30
# if m <= 0 :
#     y-=1 
#     m +=12

# vaqt = dt.date( y , m , d)

# print(f'tugulganizga {y} yil {m} oy {d} kun bulubdi hayotni qadriga yeting u bir marotaba beriladi ')

# import re

# tel_number = input('Telefon raqamingizni kiriting (998.......)  > ')
# andoza = '^998.........$'

# if re.match(andoza, tel_number)==None :
#     print('Xato raqamingizni (998906675266) shaklda kiriting')

# else :
#     print('Malumot SMS tarda yuboriladi ')

# string = """
# Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://www.youtube.com/watch?v=vsxJPRLXpgI 
# Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va https://github.com/geongeorge/i-hate-regex
# metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
#         """

# andoza1 = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
# linklar = re.findall(andoza1,string)

# print(linklar)



# """                             lesson 39                                   """
# import requests
# from pprint import pprint

# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)


# import requests
# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)


# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
# print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz

# from fuzzywuzzy import fuzz
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))



