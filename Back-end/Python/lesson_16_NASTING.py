
"""
Repeation for my self 

lesson lesson 16 NASTING 

for repiation  https://quizlet.com/_deyoqb?x=1jqt&i=52phgt

@author: rashidovj
"""
"""
        lesson 16 -> Nesting   https://quizlet.com/_deyoqb?x=1jqt&i=52phgt


NESTING biron malumot ischiga boshqasi qushish yani list ichiga dict or aksi
  list ichiga dict qushish"""
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }


cars = [car0,car1,car2]
cars[2]['rang']='qora'
print(cars[2]['rang'] ,\
      cars[1]['rang'])

cars = [car0,car1,car2]
for car in cars :
    print(f"{car['rang']} , "
          f"{car['narh']}"
          )
aim = []
for n in range(4):
    mark = {
        'model':None,
        'ramg':None,
        'yil':2023,
        'karobka':'avto'
            }
    aim.append(mark)
for mark in aim[:2] :
    mark['model']='BMW'
    mark['ramg']='qora'
for mark in aim[2:]:
    mark['model']='lambo'
    mark['ramg']='qizil'
    mark['karobka']='mexanik'

for mark in aim :
    if mark['karobka']=='avto' :
        mark['narx']=50000 
    else :
        mark['narx']=40000
    
for x in aim :
    for y in x :
        print(f'{y.title()} --> {x[y]}')

"""  dict ichiga list qushish
"""
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for k, v in dasturchilar.items():
    print(f'\n{k.title()} quyidagi dasturlash tilaarini biladi :' , end=' ')
    for knows in v :
        print(f'{knows.upper()} ' , end=' ')

"""
dict ichiga dict qushish va yan bu ishni hohlagainimizcha qilsak buladi 
"""
hamkasblar = {
    'ali':{'familiya':'valiyev',
            'tyil':1995,
            'malumot':'oliy',
            'tillar':['python','c++']
            },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
              'tyil':1999,
              'malumot':'maxsus',
              'tillar':['python','php']}
    }

for ism , malumot in hamkasblar.items():
    print(f'\n{ism.title()} ')
    for k , v in malumot.items():
        print(f"{k.title()} --> {v}" )
            
"""
                          praktis
"""



buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
}

qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}


grandpas = [buxoriy,qodiriy,vohidov,navoiy]
for k in grandpas :
    print(f"{k['ism'].title()} {k['tyil']}-yilda tug\'igan "
          f"va {k['vyil']-k['tyil']} umur kurgan")

grandpas[0]['asari']='albxoriy'
grandpas[1]['asari']='alqodiriy'
grandpas[2]['asari']='alvohidiy'
grandpas[3]['asari']='alnavoiy'

for k in grandpas:
    ism = k['ism']
    asari=k['asari']
    print(ism, asari)

davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}
order = input('Qaysi mamlakat haqida malumot izlaybsiz \n >>> ').lower()

for k , v in davlatlar.items() :
    if order in k :
        print(order.upper() , 'ning')
        for nom , mal in v.items() :
            print(f'{nom.title()} ---> {mal}')
    else :
        print(f'sorry we dont have info about {order}')


if order in davlatlar :
    print(order.upper() , 'ning')
    for nom , mal in davlatlar[order].items() : # mendan dangasa odam yuq 
        print(f'{nom.title()} ---> {mal}')
else :
    print(f'sorry we dont have info about {order}')


davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
        f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydon']} kv.km"
        f"\nAholisi: {info['aholi']}"
        f"\nPul birligi: {info['pul birligi']}"
    )
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")


