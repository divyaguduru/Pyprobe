import unittest
import userstory_1

class TestData(unittest.TestCase):
       
    def test_get_account_numbers_from_file(self):
        filename = 'entries.txt'
        value = userstory_1.get_account_numbers_from_file(filename)
        self.assertTrue(value == 'noerr')

if __name__ == '__main__':
    unittest.main()
