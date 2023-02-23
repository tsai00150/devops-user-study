import unittest
from code.two_sum import twoSum

class testTwoSum(unittest.TestCase):

    # the function name need to start with test_
    # more documentation can be seen here:
    # https://docs.python.org/3/library/unittest.html

    def test_givenExample(self):
        msg = "Passed the given example. "
        self.assertEqual(twoSum([2,7,11,15], 9), [0,1], msg)
    
    def test_noAnswer(self):
        msg = '''Need to return [-1] if no answer found. 
        Input: [100, 100, 100], 9
        Expected output: [-1]
        '''
        self.assertEqual(twoSum([100, 100, 100], 9), [-1], msg)


    def test_duplicateIndex(self):
        msg = '''Might have duplicate index. Input: [3,4], 6 
        Expected output: [0, 1]
        '''
        self.assertEqual(twoSum([3,4], 6), [0,1], msg)


if __name__ == '__main__':
    unittest.main()