"""
Repeation for my self   https://quizlet.com/_dcdt7d?x=1jqt&i=52phgt

lesson 8 ruhyatlar bn ishlash

@author: rashidovj
"""

"""                              lesson_8

sort() metodi buning vizifasi listni alfabet buyicha tartibga soladi agar ruyhat ichida 
kotta harflar bulsa usha biirnchi keladi va bu raqamlar uchun ham huddi shunday ishlaydi """



cars = ['bmw','mercedes benz','general motors', 'tesla', 'audi']

cars.append('jentra')
# cars.sort(reverse=True)
print(sorted(cars, reverse=True))
# print(cars)

sonlar=['5','234', '452', '-45' , '53', '5334']

sonlar.sort(reverse=True)

"""sonlar bilan ishlash yani finksiyalar range(a,b) yani list yaratsa a dan b-1 gacha 
agar range(a,b,c ) bulsa c buyersa qadam yani c cha sonlarni olib ketadi 
list yaratish ucun list(range(a,b))"""

sonlar=list(range(0,10))


# buyerda max , min , sum funksiyalni maksimal minimal qiymatini chiqarish yigindi sum 


sonlar = list(range(1,10))
max_son=max(sonlar)
min_son=min(sonlar)
soni=len(sonlar)
sum_son=sum(sonlar)

print('1 dan ungacha sonlar yigindisi =',sum_son , 'urta arifmetigi =', int(sum_son)//int(soni))



"""list ichidagi narsalarni nusxalash yoki kesib olish sonlar = sonlar[1:8] yani 
sonlar ichidagilarni 1 dan 8 chi elementgacha kesin oladi """

sonlar = list(range(1,9))

son_n = sonlar[1:3]
cars = ['bmw','mercedes benz','general motors', 'tesla', 'audi']
my_cars = cars[:]

my_cars.append("lasetti") 
selt_cars = my_cars [1:]
stay_cars = my_cars [:1]

"""tuple bu uzgarmas list yasalishi [] urniga () ishlatiladi va uni uzgartrib bulmaydi
uzgartrish uchun listag utqazish """


cars = ('bmw','mercedes benz','general motors', 'tesla', 'audi') # uzgarmas ruyhat
carss = list(cars[1:5]) # listaga uzgardi 
carss = tuple( carss) #   list uzgarmas ruyhatga uzgardi



"""                                     Amalyot -> 8                       """

davlatlar=["USA", 'UK', 'UZB', 'RUS']
print(sorted(davlatlar, reverse=True))
len(davlatlar)
davlatlar.reverse()
print((davlatlar))

davlatlar.sort(reverse=True)
print(davlatlar)

sonlar=list(range(120,1201,2))

print(sonlar[-1])

print(sum(sonlar))
print(max(sonlar))
print(min(sonlar))
print(len(sonlar))


print(sonlar[1:21])
print(sonlar[1:21])
print(sonlar[1:21])
soni=len(sonlar)
print(int(soni)/2)
print(sonlar[270:291])
print(sonlar[521:])

taomlar=['osh', 'manti', 'somsa', 'norin', 'shorva']

nonishta = taomlar[:]
nonishta.remove('osh')
nonishta.remove('norin')
nonishta.append('sut')
nonishta.append('qaymoq')

nonishtal=('osh', 'manti', 'somsa', 'norin', 'shorva')

nonishtal[0] = 'dfhsjkhfjkshd' 