import unittest
import userstory_2

class TestData2(unittest.TestCase):

    def test_check_valid_acc(self):
        filename ='entries2.txt'
        value = userstory_2.get_account_numbers_from_file(filename)
        self.assertEqual(value,'valid')
        
    def test_check_invalid_acc(self):
        filename ='entries2.txt'
        value = userstory_2.get_account_numbers_from_file(filename)
        self.assertEqual(value,'invalid')
        
        
if __name__ == '__main__':
    unittest.main()
