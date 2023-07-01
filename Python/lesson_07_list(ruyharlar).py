"""
Repeation for my self    https://quizlet.com/_dcdt7d?x=1jqt&i=52phgt

   Lesson_7 -> list => ruyhat

@author: rashidovj
"""

"""                        Lesson_7 -> list => ruyhat                       """

"""list -> bizga more uzgaruvchilar ochmasdan bitta uzgaruvchini ichida kk licha
string int float larni kiritish imkonini beradi yasalishi """

m_fanlar=['qorinli domla', 'kksiz fan', 'nimadurda']
kkliyli_foizi=['30','10' , '?']
hayotta_use=[] # bush ruyhat ham yaratsak buladi 

print(m_fanlar[0]) #print qilish shunday buladi ichidagilar ketma ketligidagi
# tartib raqami bn keladi faqat 0 dan boshlab sanaladi 
print(m_fanlar[-1]) # ohiridan sanomoqchi bulsak( - ) bersak buladi

"""bularni metodlar (upper, title ...) yordamida print qigincha uzgartib chiqarsak
buladi and we can sonlar bn ular ustida amallar bajarsak buladi"""

print(m_fanlar[0].title())

# list ichidagilarni uzgartirsak buladi 

m_fanlar[0]= 'material'
print(m_fanlar)

"""listga yana string or int qushmoqchi bulsak new metod [ .append() ] can use """

m_fanlar.append('english') 
print(m_fanlar)

"""append faqat list ohiridan qushadi ichida quchmoqchi bulsak [ .insert() ] 
can use """

m_fanlar.insert(2,'anything')
print(m_fanlar)

"""ruyhat ichidagi birortasini uchirmoqchi bulsak [ del ] from aperator can use"""

del m_fanlar[2]
print(m_fanlar)

"""list uzun bulib ketsa uni index sini bilamasak [ .remove() ] metod use for del"""

m_fanlar.remove('nimadurda')
print(m_fanlar)

"""listda bir xil strimlar bulsa remove boshdan boshlab bitta bitta uchiradi
ular kup bulsa kodni takrorlaymiz until finished

listdan birorta strimni sugurib ulish del dan farqi biz undan foydalanishimiz
mumkun buning uchun [ .pop() ] metoddan foydalanamiz"""

keraksiz = m_fanlar.pop(1)
print(keraksiz)

kerakli = m_fanlar.pop()  # index kiritmasak pop ohirgi strimni oladi
print(kerakli)

"""for me new metods are append , insert , romove , pop and new aperator is del.
 
                                    AMALYOT                         """

my_friends=['Jasur', 'Abbi' , 'Avaz' ]
print(f"{ my_friends[0]} , kechga kapm borasanmi? " )
print(f"{my_friends[1]} Jas kechga kam boreykan , borasan Avaz ushetda")

sonlar= ['1', '2.9' , '-5']
natija=int(sonlar[0])+float(sonlar[1])+16
print(natija)
manfiy = sonlar.pop(2)
print(manfiy)

t_shaxslar=['nyuton ' , ' amir temur ' ]
z_shaxslar=["elon mask " , " kira " ]

print(f"""\n Man holardimki {t_shaxslar[0].title()} bilan choy ichib,
then together will go to {z_shaxslar[1].title()}'s lesson 👌😂""")

exams= [ "nano", 'algo', 'ulchash', "zna"]


exams.append("prakthis")
tugagan =exams.pop(2)
exams.insert(1, 'biijj')
del exams[2]
exams.remove('nano')


ballar =['93', '96', '94', '92']

ballar.insert(1, '92')

tugagan= [exams.pop(0), exams[-1]]
tup_bal= [ballar[0] , ballar[-1]]


print(f" {tugagan[0]}={tup_bal[0]} \n {tugagan[-1]}={tup_bal[-1]} ")

ism=['Jasur','Hakim', "Vali"]
ism[2]='ahfla'

friend=[]
friend.append('Jasur', )
friend.insert(1, 'bekki')
friend.insert(2, 'umid' )

friend.remove('bekki')
