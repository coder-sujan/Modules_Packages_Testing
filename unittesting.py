#importing the unit test framework
import unittest

#importing the module that we have created
from testing import add , sub

#defined a class that inherits from unittest.TestCase
class TestCalc(unittest.TestCase):
    
    # 1st case is for add () function 
    def test_add(self):
        #this part of code deals with checking 2 args value outputs 2 +3 = 5 
        self.assertEqual(add(2,3), 5)
    
     # 2nd case is for sub () function 
    def test_sub(self):
        #this part of code deals with checking 2 args value outputs 10-4 = 6
        self.assertEqual(sub(10,4), 6)
        
             
#this ensures the test runs only when the script gets executed directly,
# and not whne its imported as a module somewhere else.
if __name__ == '__main__':
    unittest.main()
        
        
        
        
