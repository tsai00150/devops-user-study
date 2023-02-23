import unittest
from code.two_sum import twoSum

class testTwoSum(unittest.TestCase):

    # the function name need to start with test_
    # more documentation can be seen here:
    # https://docs.python.org/3/library/unittest.html

    def test_givenExample(self):
        msg = '''Passed the given example. '''
        self.assertEqual(twoSum([2,7,11,15], 9), [0,1], msg)
    
    # This is just a template; you can change the format whatever you want to have better communication with the developer. 
    # def test_<write the test name here>(self):
    #     msg = '''<message when there is an error>
    #     <try to communicate with the developer in this section>
    #     '''
    #     self.assertEqual(twoSum(<the nums array>, <target>), [-1], msg)
    
    # 1
    def test_noAnswer(self):
        msg = '''Need to return [-1] if no answer found. 
        Input: [100, 100, 100], 9
        Expected output: [-1]
        '''
        self.assertEqual(twoSum([100, 100, 100], 9), [-1], msg)

    #2
    def test_duplicateIndex(self):
        msg = '''Might have duplicate index. Input: [3,4], 6 
        Expected output: [-1]
        '''
        self.assertEqual(twoSum([3,4], 6), [-1], msg)
    
    #3
    def test_wrongType(self):
        msg = '''If nums has a string that can be converted to integer type, 
        convert it and treat it as an integer; otherwise, return [-1]. 
        '''
        self.assertEqual(twoSum([2,'7',11,15], 9), [0, 1], msg)

if __name__ == '__main__':
    unittest.main()