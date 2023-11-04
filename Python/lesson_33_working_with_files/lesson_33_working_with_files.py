"""
Repeation for my self 

lesson lesson 33 working with files 

for repiation  https://quizlet.com/813737119/python-files-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""
"""                         lesson 33                                       """

""" falylardan katta hajmdaki mulumotlarni yuklab undan dasturda foydalanish 
mumkun tayyor faylni ochish uchun open('file_name') funksiyasidan can use 
file ichidagi malumotni uqish uchun .read() funksiysidan foydalaniladi
dastrun ohirida filene close() funk bn yopish kerak else file shikas yeydi
fileni uqish uchun ular bir papkad bulishi kk 
"""

file = open('pi.txt')
PI = file.read()
print(PI)
file.close()

""" yuqoridagi usul orqali fileni chaqrib undan can use lekin bu usul tafsiya qilinmaydi 
"""

with open('pi.txt') as file :
    pi = file.read()

print(pi)

""" ikkalal usul ham bir vazifani bajaradi lekin with funksiyasi tafsiya qilinadi 
with operatorining vazifasi biz fayl bilan ishlab bo'lganimizdan so'ng faylni
  yopish. Yuqoridagi misolda, 2-qatordan so'ng Python zudlik bilan faylni yopadi.
 
  malumotga ishlob berish metodlari
  .rstrip() => qator ohiridagi bo'shliqlarni olib tashlaymiz
  .replace('\n','') => qator tashlash belgisini almashtiramiz
"""

pi = pi.rstrip()
pi = pi.replace('\n','')
pi = float(pi)
print(pi)

""" fayl ichidan fayl malumotlarini olish ucni file nomi / keyin kkli file nome 
"""

#  fileni qatorma qator uqish uchun 
filename = 'data/talabalar.txt'
with open(filename) as file :
    for line in file:
        print(line)
        
"""       
file ichidagi malumotlarni list kurinishida saqlash
.readlines() => Qatorlarni ro'yxat ko'rinishida saqlab olish uchun
"""  

filename = 'data/talabalar.txt'
with open(filename) as file :
    talabalar = file.readlines()
    
print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)


""" 
yangi file yaratish     with open(file_name,'w') as file: => "w" - write
'w'agar file biz yaratmoqshi bulgan file nomi avval mavjud bulgan bulsa 
fileni uchirib tashlaydi
filega mlumot qushish   with open(file_name,'a') as file: => "a" - append
"a" yani filega malumot qushmoqchi bulsagu file mavjud bulmasa new file ochadi
"""
# yangi file yaratish
file_name = 'new_file.txt' 
ism = 'javohir rashidov'
tyil = 2004
with open(file_name,'w') as file:
    file.write(ism +'\n')
    file.write(str(tyil)+'\n')
    
# filega mlumot qushish
with open(file_name,'a') as file:
    file.write( 'javohir rashidov')
    file.write('2004')

""" yuqoridagilar faqat matn shaklida edi yani str , filega uzgaruvchi yoki 
boshqaobyekt yoki dict larni qushishni kuramiz bunish uchun pickle modulidan 
foydalanamiz tarjimasi kanservalash Pickle ma'lumotlarni biz qanday ko'rinishda
bersak, shunday ko'rinishda faylga yozadi. Yuqoridagi usuldan farqli ravishda, 
pickle yordamida yozilgan fayllarning tarkibini Pythondan tashqarida cant see
"""
import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info' , 'wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
    
""" 'wb' ( write binery) 2li sanoq setemasida saqla 
pickle dan malumot uqish Pickle fayldan o'qish uchun open() funksiyasini
  'rb' (read binary) argumenti bilan chaqiramiz. 
"""

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)

"""                              Amalyot                         """

with open('pi_million.txt') as file:
    pi = file.read()
    
pi = pi.rstrip()
pi = pi.replace('\n','')
print(pi)
    
with open('pi_million.txt') as file:
    for line in file:
        print(line)
    
with open('pi_million.txt') as file:
    qatorlar = file.readlines()
    qatorlar = [qator.rstrip() for qator in qatorlar]
print(qatorlar)
    
with open('pi_million.txt') as file:
    pi = file.read()
    
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(' ','')
print(pi)
my_day = '020504'

if my_day in pi:
    print('ha')
else:
    print('no')
    
import pickle

pi = float(pi)
    
with open('info_dat','wb') as file:
    pickle.dump(pi,file)
    

with open('info_dat','rb') as file:
    pi = pickle.load(file)
    
print(pi)
    
    
    
    
    
    
    
    
    