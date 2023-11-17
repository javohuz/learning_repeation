"""
Repeation for my self 

lesson 34 JSON 

for repiation  https://quizlet.com/813737119/python-files-flash-cards/?i=52phgt&x=1qqt

@author: rashidovj
"""

"""                             lesson 34                                   """


""" 
JSON (JavaScript Object Notation) bugungi kunda ma'lumotlarni saqlash va internet
 orqali uzatish uchun qo'llaniladigan eng mashxur format hisoblanadi.
 """

import json
x=5
x_json = json.dumps(x)

ism = "Javohir"
ism_json = json.dumps(ism)

sonlar = [12, 45, 23, 67]
sonlar_json = json.dumps(sonlar)

m = True
m_json = json.dumps(m)

"""
 json.dumps(x) — berilgan x o'zgaruvchini JSON matniga o'zgartiradi
 json.dump(x,fayl) — berilgan x o'zgaruvchini JSON ga o'zgartirib, ko'rsatilgan faylga saqlaydi.
 jsonga yuklangan malumotlar avvlar javascript tiliga utkazildi keyin matnga utgaziladi 
"""

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

# bemor_json = json.dumps(bemor)

bemor_json = json.dumps(bemor , indent=4)

# print(bemor_json)
""" indent=a  a any number jsonga  malumot yuklanayotganda har bir list ili dickt 
boshlanish oldidan a ta joytashlaydi sal tshunarli tartibda buladi 
""" 

"""
json ni file shaklida saqlash bunish uchun .dumps()ni urniga ,dump() use
"""

with open('bemor.json' , 'w') as file :
    json.dump(bemor,file)

""" 
jsonga utkazilgan malumotlarni qaytarib python tiliga utkazish uchun .loads() use
"""
bemor1= json.loads(bemor_json)

"""
json kurinishida fileni oshishni uchun .load() foydalanamiz 
"""
with open('bemor.json' ) as file:
    bemor = json.load(file )

# print(bemor)


"""                               Amalyot                                   """

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data)

data1= json.loads(data_json)

with open('data.json' , 'w') as  file:
    json.dump(data,file)
    
with open ('data.json') as f:
    data =  json.load(f)


print(data)

with open('any_file' ,'w') as file:
    file.write('someone' +'\n' )
    file.write('2020')


with open('any_file') as file:
    ism = file.readlines()

print(ism)

with open('students.json' ) as f :
    students = json.load(f)


for student in students['student']:
    name = student['name']
    lastname = student['lastname']

with open('studentlar' , 'w') as file:
    for student in students['student']:
        name = student['name']
        lastname = student['lastname']
        file.write(name+' ')
        file.write(lastname + '\n')
        
with open('studentlar') as f :
    student_name = f.readlines()

print(student_name)


data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
students

data_json = json.dumps(data)
students_json = json.dumps(students)
print(data_json)
print(students_json)

with open('ex_there.json' ,'w' ) as file :
    json.dump(data,file )


with open('ex_there.json') as file:
    data_json = json.load(file)

print(data_json)


with open('students.json' ) as f :
    students = json.load(f)
talabalar = []

for studentlar in students['student']:
    name = student['name']
    lastname = student['lastname']
    id_numb = student['id']
    year = student['year']
    faculty = student['faculty']
    talaba = f'{name.title()} {lastname.title()}  {year}-yildan beri {faculty} fakultatida uqiydi ' 
    talabalar.append(talaba) 
        
        
print(talabalar[1])       