import unittest

from ChangeCalculator import ChangeCalculator


class ChangeCalculatorTest(unittest.TestCase):

    if __name__ == '__main__':
        unittest.main()

    changeCalculator = ChangeCalculator()

    def test_get_change_out_of_range(self):
        with self.assertRaises(ValueError) as context:
            self.changeCalculator.calculateSmallestChange(5000)

        self.assertTrue("Total must not be greater than 4999" in str(context.exception))

    def test_get_change_Negative_input(self):
        with self.assertRaises(ValueError) as context:
            self.changeCalculator.calculateSmallestChange(-1)

        self.assertTrue("Total must be 0 or greater" in str(context.exception))

    def test_get_change_zero(self):
        self.assertTrue(self.changeCalculator.calculateSmallestChange(0) == [])

    def test_get_change_single_coin(self):
        self.assertTrue(self.changeCalculator.calculateSmallestChange(1) == [1])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(2) == [2])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(5) == [5])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(10) == [10])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(20) == [20])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(50) == [50])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(100) == [100])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(200) == [200])

    def test_get_change_multiple_coins(self):
        self.assertTrue(self.changeCalculator.calculateSmallestChange(3) == [2,1])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(4) == [2,2])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(6) == [5,1])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(17) == [10,5,2])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(33) == [20,10,2,1])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(84) == [50,20,10,2,2])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(167) == [100,50,10,5,2])
        self.assertTrue(self.changeCalculator.calculateSmallestChange(465) == [200,200,50,10,5])

    def test_get_change_upper_boundary(self):
        self.assertTrue(self.changeCalculator.calculateSmallestChange(4999) == [200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,200,100,50,20,20,5,2,2])

