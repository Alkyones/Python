import unittest
from  sum_args import sum_all

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test can sum of a list of integers :
        """
        self.assertEqual(sum_all([1,2,3,4]), 10, "Should be equal to 10")
        self.assertEqual(sum_all([1,2,3,4,5]), 15, "Should be equal to 15")
        self.assertEqual(sum_all([1,2,3,4,5,6]), 21, "Should be equal to 21")
        self.assertEqual(sum_all([1,2,3,4,5,6,7]), 28, "Should be equal to 28")
        self.assertEqual(sum_all([1,2,3,4,5,6,7,8]), 36, "Should be equal to 36")
    
    def test_sum_of_lists(self):
        """
        Test can sum of a list of lists of integers :
        """
        self.assertEqual(sum_all([[1,2,3,4],[5,6,7,8]]), 36, "Should be equal to 36")
        self.assertEqual(sum_all([[1,2,3,4], [5,7,8], [9,10,11,12]]), 72, "Should be equal to 72")
        self.assertEqual(sum_all([[1,2,3,4], [5,7,8], [9,10,11,12], [13,14,5,16]]), 120, "Should be equal to 120")
