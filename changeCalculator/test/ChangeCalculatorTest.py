import unittest

from ChangeCalculator import ChangeCalculator


class ChangeCalculatorTest(unittest.TestCase):

    #Test out of bounds
    #Test zero

    def test_get_change_single_coin(self):
        changeCalculator = ChangeCalculator()
        self.assertTrue(changeCalculator.calculateSmallestChange(1) == [1])
        self.assertTrue(changeCalculator.calculateSmallestChange(2) == [2])
        self.assertTrue(changeCalculator.calculateSmallestChange(5) == [5])
        self.assertTrue(changeCalculator.calculateSmallestChange(10) == [10])
        self.assertTrue(changeCalculator.calculateSmallestChange(20) == [20])
        self.assertTrue(changeCalculator.calculateSmallestChange(50) == [50])
        self.assertTrue(changeCalculator.calculateSmallestChange(100) == [100])
        self.assertTrue(changeCalculator.calculateSmallestChange(200) == [200])

    def test_get_change_multiple_coins(self):
        changeCalculator = ChangeCalculator()
        self.assertTrue(changeCalculator.calculateSmallestChange(3) == [2,1])
        self.assertTrue(changeCalculator.calculateSmallestChange(4) == [2,2])
        self.assertTrue(changeCalculator.calculateSmallestChange(6) == [5,1])
        self.assertTrue(changeCalculator.calculateSmallestChange(17) == [10,5,2])
        self.assertTrue(changeCalculator.calculateSmallestChange(33) == [20,10,2,1])
        self.assertTrue(changeCalculator.calculateSmallestChange(84) == [50,20,10,2,2])
        self.assertTrue(changeCalculator.calculateSmallestChange(167) == [100,50,10,5,2])
        self.assertTrue(changeCalculator.calculateSmallestChange(465) == [200,200,50,10,5])

if __name__ == '__main__':
    unittest.main()