#calculate_statistics.py
from statistics import mean, median, mode, StatisticsError

def calculate_statistics(data):
    """
    Calculate mean, max, median, and mode of the given data.

    Arguments:
        data (list): List of numeric values
    
    Returns:
        tuple: A tuple containing mean, max, median, and mode (message if mode does not exist).

    """
    # calculating mean, max, median, and mode from data in given csv file
    mean_value = mean(data)
    max_value = max(data)
    median_value = median(data)

    # mode might not exist, handling that excpetion
    mode_value = None
    try:
        mode_value = mode(data)
    except StatisticsError:
        mode_value = "No mode found"

    results = (mean_value, max_value, median_value, mode_value)

    return results