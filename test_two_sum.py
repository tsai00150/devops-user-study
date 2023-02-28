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

    def test_no_ans1(self):
        msg = "In: [2,7,11,15] target: 100 out: None"
        self.assertEqual(twoSum([2,7,11,15], 100), None, msg)
        
    def test_no_ans2(self):
        msg = "In: [2,7,11,21] target: 100 out: None"
        self.assertEqual(twoSum([2,7,11,21], 100), None, msg)

    def test_same_ans1(self):
        msg = "In: [2,3] target: 4 out: None"
        self.assertEqual(twoSum([2, 3], 4), None, msg)

    def test_same_ans2(self):
        msg ="In: [3,3] target: 6 out: [0,1]"
        self.assertEqual(twoSum([3, 3], 6), [0, 1], msg)


    def test_diff_in_type(self):
        msg = "In: [\'3\',3] target: 6 out: [0,1]"
        self.assertEqual(twoSum(['3', 3], 6), [0, 1], msg)

    
    def test_increasing(self):
        msg = "In: [1,2,3,4,5] target: 5 out: [1,2]"
        self.assertEqual(twoSum([1,2,3,4,5], 5), [1, 2], msg)


    def test_zero(self):
        msg = "In: [1,2,3,4,5] target: 0 out: \'Zero detected!\'"
        self.assertEqual(twoSum([1,2,3,4,5], 0), 'Zero detected!', msg)

    # This is just a template; you can change the format whatever you want to have better communication with the developer. 
    # def test_<write the test name here>(self):
    #     msg = '''<message when there is an error>
    #     <try to communicate with the developer in this section>
    #     '''
    #     self.assertEqual(twoSum(<the nums array>, <target>), [-1], msg)


if __name__ == '__main__':
    unittest.main()