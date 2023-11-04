
""" 
funksiyalarni tekshirish , dasturlash davomida katta jamoa bn ishlaganda boshqalr 
yaratgan funksiyalar siga kk bulishi yoki siz uz funksiyangiz tugri ekanligini albatta 
takshirib kurish kk bu jaroyonni uzimiz qulda kodga qiymat berib amalga oshirish mumkun 
lekin bu juda noqulay va kod katta buladigan bulsa kup vat ketadi 
Pythonda bu jarayonni osonlashtirish uchun maxsus unittest moduli mavjud.
 unittest yordamida alohida funksiya, obyekt yoki butun boshli modulni ham 
 tekshirshimiz mumkin. Lekin, tavsiya qilingan usuli bu testni dastavval kichik 
 qismlardan boshlab, kengaytirib borish tacsiya qilinadi 
"""

import unittest
from name import fullname , fullname_with_sharf , getArea , getPerimeter

class TestName(unittest.TestCase):
    def test_fullname(self):
        test_funck = fullname('javohir' , 'rashidov')
        self.assertEqual(test_funck , 'Javohir Rashidov')
        
    def test_fullname_with_sharf(self):
        test_func = fullname_with_sharf('javohir','rashidov','hasan ugli')
        self.assertEqual(test_func , 'Javohir Rashidov Hasan Ugli')
        


""" yuqoridagilardan shablon sifatida foydalansa buladi deyarli har doim shu kod yoziladi 
faqatgina self.assertEqual(first , sekond) metodini uzgartrish orqali boshqa
funksiyalrni uzimiz ga moslab tekshirsak buladi  

self.assertEqual(first , second) => first tekshiriladigan function second kerakli natija 

self.assertAlmostEqual(firt , second , qadam ) bu metod sonlarni tekshirganda kk buladi 
yani qadam buyerda nechcha xona aniqlikda tekshirishi agar qadam bulmasa mln da aniqlikda oladi

asosiy tekshiriladiganlari shular agar boshqa hollarni tekshirish kk bulsa shablonni qidirish kk
"""

class Testdoira(unittest.TestCase):
    def test_doira(self):
        test_getPerimeter = getPerimeter(10)
        self.assertAlmostEqual(test_getPerimeter , 62.8318 )
        self.assertAlmostEqual(getPerimeter(4) , 25.13272 ,4) # 4 buyerda qadan 

    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3),28.27431)
   
    
unittest.main()


    

