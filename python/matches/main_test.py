import unittest
from main import solve as func
class MainTest(unittest.TestCase):
    def test_when_there_are_no_values(self):
        values = []
        total_inches = 150
        self.assertEqual([], func(values, total_inches))
    def test_when_no_pair_matches(self):
        values = self.get_values()
        total_inches = 125
        self.assertEqual([], func(values, total_inches))
    def test_when_a_single_pair_matches(self):
        values = self.get_values()
        total_inches = 135
        self.assertEqual(1, len(func(values, total_inches)))
    def test_when_more_than_one_pair_matches(self):
        values = self.get_values()
        values.append({
                'first_name': 'Nay',
                'last_name': 'Goez',
                'h_meters': '1.96',
                'h_in': 68.0
            })
        total_inches = 135
        self.assertEqual(2, len(func(values, total_inches)))
        
    def get_values(self):
        return [
            {
                'first_name': 'John',
                'last_name': 'Feckir',
                'h_meters': '1.96',
                'h_in': 70.0
            },
            {
                'first_name': 'Alice',
                'last_name': 'Boer',
                'h_meters': '1.96',
                'h_in': 67.0
            },
            {
                'first_name': 'Maria',
                'last_name': 'Rodriguez',
                'h_meters': '1.96',
                'h_in': 65.0
            }
        ]
if __name__ == '__main__':
    unittest.main()