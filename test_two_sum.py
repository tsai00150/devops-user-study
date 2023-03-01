import unittest
from code.two_sum import twoSum

class testTwoSum(unittest.TestCase):

    # the function name need to start with test_
    # more documentation can be seen here:
    # https://docs.python.org/3/library/unittest.html
    # https://www.dataquest.io/blog/unit-tests-python/

    def test_givenExample(self):
        msg = "Did not pass the given example. "
        self.assertEqual(twoSum([2,7,11,15], 9), [0,1], msg)

    def test_givenExample2(self):
        msg = "Did not pass another random example. "
        self.assertEqual(twoSum([2,7,11,15], 26), [2,3], msg)
    
    def test_none1(self):
        msg = "If there is no answer, return None"
        self.assertEqual(twoSum([2,3,4], 10), None, msg)
    
    def test_none2(self):
        msg = "If there is no answer, return None"
        self.assertEqual(twoSum([2,30,40], 100), None, msg)
    
    def test_duplicate1(self):
        msg = "Cannot return the same index"
        self.assertEqual(twoSum([3,3], 6), [0,1], msg)
    
    def test_duplicate2(self):
        msg = "Cannot return the same index"
        self.assertEqual(twoSum([10,10], 20), [0,1], msg)

    def test_input1(self):
        msg = "The input format is incorrect"
        self.assertEqual(twoSum([2,'7'], 9), None, msg)
    
    def test_input2(self):
        msg = "The input format is incorrect"
        self.assertEqual(twoSum([2,'a'], 9), None, msg)

    def test_output(self):
        msg = "The output format is incorrect"
        self.assertEqual(twoSum([2,7], '9'), None, msg)
    
    def test_zero(self):
        msg = "U should return Zero detected!"
        self.assertEqual(twoSum([2,7], 0), 'Zero detected', msg)

    # This is just a template; you can change the format whatever you want to have better communication with the developer. 
    # def test_<write the test name here>(self):
    #     msg = '''<message when there is an error>
    #     <try to communicate with the developer in this section>
    #     '''
    #     self.assertEqual(twoSum(<the nums array>, <target>), [-1], msg)


if __name__ == '__main__':
    unittest.main()