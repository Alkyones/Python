import unittest

from circle_calculator import circle_area



class TestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle_area(2), 12)
        self.assertEqual(circle_area(3), 28) 
        self.assertEqual(circle_area(4), 50)

    def test_circle_area_negative(self):
        self.assertEqual(circle_area(-2), 0)
        self.assertEqual(circle_area(-3), 0)
        self.assertEqual(circle_area(-4), 0)
    
    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_circle_area_list(self):
        # unittest for list of values
        self.assertEqual(circle_area([2, 3, 4]), [12, 28, 50])    
        self.assertEqual(circle_area([2, 3, 4, 5]), [12, 28, 50, 78])
        self.assertEqual(circle_area([2,5,0,0,-1],), [12, 78, 0, 0, 0])

    def test_circle_area_tuple(self):   
        # unittest for tuple of values
        self.assertEqual(circle_area((2, 3, 4)), (12, 28, 50)), "Tuple is not equal"
        self.assertEqual(circle_area((2, 3, 4, 5)), (12, 28, 50, 78))
        self.assertEqual(circle_area((2,5,0,0,-1)), (12, 78, 0, 0, 0)) 

    def test_circle_area_dict(self):
        # unittest for dictionary of values
        self.assertEqual(circle_area({'radius': 2}), {'radius': 2, 'area': 12})
        self.assertEqual(circle_area({'radius': 3}), {'radius': 3, 'area': 28})
        self.assertEqual(circle_area({'radius': 4}), {'radius': 4, 'area': 50}) 
        self.assertEqual(circle_area({'radius': 0}), {'radius': 0, 'area': 0})
        self.assertEqual(circle_area({'radius': -2}), {'radius': -2, 'area': 0})
        self.assertEqual(circle_area({}), "No radius key in dictionary")
        self.assertEqual(circle_area({}), "No radius key in dictionary")

 