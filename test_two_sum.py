import unittest
from code.two_sum import twoSum


class testTwoSum(unittest.TestCase):

    # the function name need to start with test_
    # more documentation can be seen here:
    # https://docs.python.org/3/library/unittest.html
    # https://www.dataquest.io/blog/unit-tests-python/

    def test_givenExample(self):
        msg = "Did not pass the given example. "
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1], msg)

    def test_givenExample2(self):
        msg = "Did not pass another random example. "
        self.assertEqual(twoSum([2, 7, 11, 15], 26), [2, 3], msg)

    def test_givenExample3(self):
        msg = "Did not pass another random example. "
        self.assertEqual(twoSum([4, 17, 18, 21], 38), [1, 3], msg)

    def test_givenExample4(self):
        msg = "If two indexes are the same, return error."
        self.assertEqual(twoSum([2, 3, 5, 10], 4), [-1], msg)

    def test_givenExample5(self):
        msg = "If the input type is invalid, return error."
        self.assertEqual(twoSum([5, '6', 8, 9], 13), [-1], msg)

    # This is just a template; you can change the format whatever you want to have better communication with the developer.
    # def test_<write the test name here>(self):
    #     msg = '''<message when there is an error>
    #     <try to communicate with the developer in this section>
    #     '''
    #     self.assertEqual(twoSum(<the nums array>, <target>), [-1], msg)


if __name__ == '__main__':
    unittest.main()
