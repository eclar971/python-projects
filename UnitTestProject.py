
# Ernest Clark
# Software and App development
# 1/28/22

import unittest


class Test(unittest.TestCase):
    # test that the sum of the given list is 6
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # test that the phase YOUR MOM is the upper cased of your mom
    def test_upper(self):
        self.assertEqual('your mom'.upper(), 'YOUR MOM', 'haha funny lmao')

    # test that the phase your mom is the phrase YOU'RE MOM lower cased
    def test_lower(self):
        self.assertEqual('your mom', "YOU'RE MOM".lower(), 'grammar time')

    # test if the float of a string is the same as a float
    def test_float(self):
        self.assertEqual(float('32.323'), 32.323, 'come on man')



if __name__ == '__main__':
    unittest.main()