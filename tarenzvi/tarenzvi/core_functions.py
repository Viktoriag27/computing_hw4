# tarenzvi/core_functions.py
import pandas as pd
from functools import reduce
#from datetime import date
from geopy.distance import geodesic

def main_function():
    """A core function for the library."""
    return "Hello from the core function!"

# core_functions.py
# 1) Create a function called "count_simba" that counts and returns
# the number of times that "Simba" appears in a list of strings.
def count_simba(strings):
    """
    Count occurrences of the word "Simba" in a list of strings.
    
    Args:
        strings (list of str): List of strings to search for "Simba".
    
    Returns:
        int: Total count of "Simba" in the list.
    """
    # Use map to count "Simba" in each string
    simba_counts = map(lambda s: s.count("Simba"), strings)
    
    # Use reduce to sum up all counts of "Simba" in each string
    total_simba_count = reduce(lambda a, b: a + b, simba_counts)
    
    return total_simba_count


# 2) Create a function called "get_day_month_year" that takes 
# a list of datetime.date and returns a pandas dataframe
# with three columns: day, month, and year.
def get_day_month_year(dates):
    """
    Convert a list of datetime objects to a pandas DataFrame with day, month, and year columns.
    
    Args:
        dates: List of dates to extract day, month, and year.
    
    Returns:
        pd.DataFrame: DataFrame with day, month, and year columns.
    """
    # Use map to extract day, month, year from each date
    day_month_year = map(lambda d: {'day': d.day, 'month': d.month, 'year': d.year}, dates)
    
    # Use reduce to accumulate them into a list
    day_month_year_list = reduce(lambda acc, val: acc + [val], day_month_year, [])
    
    # Convert the list into a DataFrame
    df = pd.DataFrame(day_month_year_list)
    
    return df


# 3) Create a function called "compute_distance" that takes a list of tuple pairs with latitude
# and longitude coordinates and returns a list with the distance between the two pairs.
def compute_distance(coord_pairs):
    """
    Calculate the distance between pairs of latitude and longitude coordinates.
    
    Args:
        coord_pairs (list of tuples): Each tuple contains two coordinates (lat, long).
    
    Returns:
        list: A list of distances between the coordinate pairs, in kilometers.
    """
    # Use map to calculate the distance between each pair of coordinates
    distances = list(map(lambda pair: geodesic(pair[0], pair[1]).kilometers, coord_pairs))
    
    return distances


# 4) Create a recursive function called "sum_general_int_list" that takes a list which could
# contain integers, or other lists (possibly nested), and returns the sum of all integers.
def sum_general_int_list(lst):
    """
    Recursively sum all integers in a nested list structure.
    
    Args:
        lst (list): A list that may contain integers or nested lists.
    
    Returns:
        int: Sum of all integers within the nested list.
    """
    total_sum = 0
    
    for item in lst:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, list):
            total_sum += sum_general_int_list(item)
    
    return total_sum
