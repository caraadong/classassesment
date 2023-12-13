import sys
import pandas
from statistics import mean, max, median, mode, StatisticsError

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

        return mean_value, max_value, median_value, mode_value

def main():
    # Check if the user provided the CSV file path
    if len(sys.argv)!=2: 
        print("Usage: python script.py <csv_file_path>")
        sys.exit(1)

    # Get the CSV file path from command line argument
    file_path = sys.argv[1]

    # Loading data from CSV file using pandas
    try:
        df = pandas.read_csv(file_path)
        data = df.values.flatten().tolist()
    # 'df' is DataFrame containing data from CSV file
        print(df)
    except FileNotFoundError:
        print(f"Error: file at '{file_path}' was not found.")

    # Calculate and print statistics
    mean_value, max_value, median_value, mode_value = calculate_statistics(data)

    # Print statistics
    print(f"Mean: {mean_value}, Max: {max_value}, Median: {median_value}, Mode: {mode_value}")

    # Print Statistics using f-string
    print(f"Mean: {mean_value}, Max: {max_value}, Median: {median_value}, Mode: {mode_value}")

    # Append results to a list iteratively inside a loop
    results = [mean_value, max_value, median_value]
    for item in results:
        # Append item to the list
        results.append(item)
    

# Ensures that 'main' function is only called if this script is run as the main program
# If script is run directly, condition '__name__ == "__main__"' is true.
# If script is imported as module into another script, condition is false
if __name__ == "__main__":
    main()
