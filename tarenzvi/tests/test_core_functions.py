# tests/test_core_functions.py
import unittest
from tarenzvi.core_functions import main_function,count_simba, get_day_month_year, compute_distance, sum_general_int_list
from datetime import date
import pandas as pd
from geopy.distance import geodesic

class TestCoreFunctions(unittest.TestCase):

    def test_main_function(self):
        self.assertEqual(main_function(), "Hello from the core function!")

if __name__ == '__main__':
    unittest.main()
    
    
    # Test for count_simba
    def test_count_simba(self):
        strings = [
            "Simba and Nala are lions.",
            "I laugh in the face of danger.",
            "Hakuna matata",
            "Timon, Pumba and Simba are friends, but Simba could eat the other two."
        ]
        self.assertEqual(count_simba(strings), 3)

    # Test for get_day_month_year
    def test_get_day_month_year(self):
        dates = [
            date(2023, 10, 17),
            date(2022, 5, 23),
            date(2024, 12, 1)
        ]
        expected_df = pd.DataFrame({
            'day': [17, 23, 1],
            'month': [10, 5, 12],
            'year': [2023, 2022, 2024]
        })
        pd.testing.assert_frame_equal(get_day_month_year(dates), expected_df)

    # Test for compute_distance
    def test_compute_distance(self):
        coords = [
            ((41.23, 23.5), (41.5, 23.4)),
            ((52.38, 20.1), (52.3, 17.8))
        ]
        expected_distances = [
            geodesic((41.23, 23.5), (41.5, 23.4)).kilometers,
            geodesic((52.38, 20.1), (52.3, 17.8)).kilometers
        ]
        self.assertEqual(compute_distance(coords), expected_distances)

    # Test for sum_general_int_list
    def test_sum_general_int_list(self):
        list_1 = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
        self.assertEqual(sum_general_int_list(list_1), 46)

if __name__ == '__main__':
    unittest.main()
