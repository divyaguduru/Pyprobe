import unittest
import userstory_3

class TestData3(unittest.TestCase):
       
    def test_accounts(self):
        filename = 'entries3.txt'
        valueop = userstory_3.get_account_numbers_from_file(filename)
        self.assertEqual(valueop,'no error')    

        
if __name__ == '__main__':
    unittest.main()
