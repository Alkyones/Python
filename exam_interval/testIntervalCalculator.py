import unittest
from intervalCalculator import listSorter

class TestListSorter(unittest.TestCase):

    def test_list_sorter_success(self):
        self.assertEqual(listSorter([1,7,2,-2,1]), [-2,7,2,1,1])




if __name__ == '__main__':
    unittest.main()