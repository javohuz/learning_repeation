"""
Repeation for my self 

   Lesson_7 -> list => ruyhat

@author: javokhirdeveloper
"""

#                         Lesson_7 -> list => ruyhat

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