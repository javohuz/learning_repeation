
"""
Repeation for my self 

lesson lesson 15 dictionary

for repiation  https://quizlet.com/_deyoqb?x=1jqt&i=52phgt

@author: rashidovj
"""

"""
                      Lasson 15 



.items() metodi manosi elementar  , lugatdagi narsalarni chiqaradi
"""
me = {
      "ism" :"javohir",
      "familiya ":"rashidov",
      "yosh":17 , 
      "tel_n":+998906675266
      }
for kalit,qiymat in me.items() :
    print(f"kalit : {kalit} ")
    print(f"qiymat : {qiymat}\n")

tel = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in tel.items() :
    print(f'{k.title()} ning telefoni {q}')
"""
.keys() metodi faqat kelitlarni chiqaradi , .values() qiymarlarni 
"""
me = {
      "ism" :"javohir",
      "familiya ":"rashidov",
      "yosh":17 , 
      "tel_n":+998906675266
      }

print(me.values())

for k in me.keys() : # aagr .keys() bulmasa ham huddi shumday ishlardi
    print(k)
for q in me.values() : 
    print(q)

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
bozorliq = ['olma' , 'uzum', 'ananas']

for k in mahsulotlar.keys():
    if k in bozorliq :
        print(f'{k}ning narxi {mahsulotlar[k]}')

for bor in bozorliq :
    if bor not in mahsulotlar :
        print(bor , 'bizda bunaqa mahsulot yoq')

for k in sorted(mahsulotlar):
    print (k)

"""set yani sets bu ham hudi listga uhshaydi faqat buni ichidagilar
takrorlanmaydi takrorlangan bulsa uqimaydi yasalishi  a={'b','c'}
"""
kitoblar={'math', 'kimyo', 'math', 'tarix'}
print(kitoblar)
"""
yana sets -> set() ni boshqa metodlar kabi ishlatsa buladi yani 
"""
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

for tel in set(telefonlar.values()):
    print(tel)

"""                          amalyot
"""
smt = {
        'for': 'biror amalni qayta qayta bajarush sikli' ,
        'in' : 'yuklaydi',
        'set' :'takrorlanmaydi',
        'if' : 'agar',
        'append':'listga qiymat qushadi'
        }

for k,q in sorted(smt.items()):
    print(k.title(),'->',q)


count = {
        'uk':'london',
        'russia':'maskov',
        'germany':'berlin',
        'uzbekistan':'tashkent'
        }
print('Davlatlar ')
for k in  sorted(count.keys()):
    print( k.title(),)
print('Poytaxtlar ruyhati ')
for q in sorted(count.values()):
    print(q.title())

davlat =input('Istalgan davlat nomi kiriting ...').lower()
x=count.get(davlat)
print(count.get(davlat, 'kechirasiz buning qiymatini aniqlay olmayman'))
if x==None :
    print('Bunday malumot mavjud emas')
else :
    print(f'{davlat.upper()} davlatining poytaxti {x.upper()}')

taomlar ={
    'manti':15000,
    'honim':15000,
    'chuchvara':20000,
    'osh':25000,
    'beshteks':20000,
    'lagmon':20000,
    'moshhorda':20000,
    'non':4000,
    'choy':5000
          }

print('Bugun nima yeymiz  ')
order =[]
for x in range(3):
    order.append(input(' >>> ').lower())

for k in taomlar.keys():
    if k in order :
        print(f'{k.title()}ning narxi {taomlar[k]}')

for x in order:
    if x not in taomlar:
        print(f'Bizda {x.title} qolmagan')


