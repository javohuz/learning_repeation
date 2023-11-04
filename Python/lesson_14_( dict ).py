
"""
Repeation for my self 

lesson lesson 14 dictionary

for repiation  https://quizlet.com/_deyoqb?x=1jqt&i=52phgt

@author: rashidovj
"""

"""
            lesson 14 dictionary 

ruyhatga uhshaydi yani bir soz ikkinchisiga thenglashtradi bu raqam bn ham bulish can  
yasalishi {} bn  
"""
talaba = {'javohir':5 , 'hakim':5 , 'valijon':4}
print('talabaning bahosi' ,  talaba['javohir'])

talaba = {'Javohir':int(input('Javohirning bahosi >> ')),
'hakim':int(input('Hakimrning bahosi >> ')),
'vali':int(input('Valirning bahosi >> ' ))
            }

for baho in talaba :
    print(baho)



"""qushi , uzgartrish , uchirish"""

talaba = {'javohir':5 , 'hakim':5 , 'valijon':4}
talaba['hakim']=6
talaba['jasur']=5
del talaba['valijon']
print(talaba)

"""
.get() vazifasi agar suralgan smt lugat ichida bulmasa keyingi kodni uqiydi 
agar bulsa kiritilgan soz kalitini chiqaradi .
"""
talaba = {'javohir':5 , 'hakim':5 , 'valijon':4}
print(talaba.get('jasur' ,'bunday narsa yoq'))


"""                                  amalyot """

lugat = {'can' : 'mumkun' , "if" : "agar" , 'else':'aks holda'}
x = input("english word >> ").lower
print (lugat.get( x , 'kechirasiz bunday soz mavjud emas'))


lugat = {'can' : 'mumkun' , "if" : "agar" , 'else':'aks holda'}
x = input("english word >> ").lower()
tarjima = lugat.get(x)
if tarjima == None :
    print('kechirasiz bu sozni tarjima qila olmayman')
else :
    print(lugat[x])



otam = {"ismi": "mavlutdin", "tyil": 1954, "viloyat": "samarqand"}
tyil = otam["tyil"]
vil = otam["viloyat"]
print(
    f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan"
)

taomlar = {
    "ali": "osh",
    "vali": "shashlik",
    "hasan": "lag'mon",
    "husan": "mastava",
    "olim": "somsa",
}

taom = taomlar["ali"]
print(f"Alining sevimli taomi {taom}")

python_izohli_lugati = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
