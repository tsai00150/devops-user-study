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

    # This is just a template; you can change the format whatever you want to have better communication with the developer. 
    # def test_<write the test name here>(self):
    #     msg = '''<message when there is an error>
    #     <try to communicate with the developer in this section>
    #     '''
    #     self.assertEqual(twoSum(<the nums array>, <target>), [-1], msg)

    def test_givenExample2(self):
        msg = "Did not pass the given example. "
        self.assertEqual(twoSum([2,7,11,15], 26), [2,3], msg)
    
    def test_givenExample3(self):
        msg = "Did not pass the given example. "
        self.assertEqual(twoSum([3, 4], 6), [-1], msg)



if __name__ == '__main__':
    unittest.main()