import unittest 
from practice_functions import getLargest ,title_string ,juft_son ,fibonachchi

class TestPractice(unittest.TestCase):
    
    def test_getLargest(self):
        self.assertEqual(getLargest(3, 7, 2) , 7)
        self.assertEqual(getLargest(9, 1, 6) , 9)
        self.assertEqual(getLargest(4, 15, 32) , 32)
        
    def test_title_tring(self):
        self.assertEqual(title_string('salom','hayr') , ['Salom' , 'Hayr'])
        self.assertEqual(title_string('Javohir','rashidov') , ['Javohir' , 'Rashidov'])

    
    def test_juft_son(self):
        self.assertEqual(juft_son(2,4,6,3,9,4,5) , [2,4,6,4])
        
        
    def test_fibonachchi(self):
        self.assertTrue(fibonachchi(2,3,5,8) )
        
unittest.main()



