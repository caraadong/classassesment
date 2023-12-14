import sys
import pandas
import numpy 
import re

from calculate_statistics import calculate_statistics 

# Ensures that 'main' function is only called if this script is run as the main program
# If script is run directly, condition '__name__ == "__main__"' is true.
# If script is imported as module into another script, condition is false
if __name__ == "__main__":

    # Check if the user provided the CSV file path
    # Checks the length and if length is not equal to 2
    # Ensures script is used correctly with expected number of command-line arguments
    if len(sys.argv) !=2:
        print("Usage: python script.py <csv_file_path>")
        sys.exit(1)
    
    # Get the CSV file path from command line argument
    # Able to retrieve file path as command-line argument
    file_path = sys.argv[1]

    # string method to split string into list of smaller strings
    file_path_splits = file_path.split('/') 
    print(f'file name without directory is {file_path_splits[-1]}\n') # backslash in string to 'escape' special character
    print(r'\n is a new line', '\n') # 'raw' string in string to avoid needing backslashes

    m = re.match('(.*).csv$', file_path) # regular expression in order to check string matched certain pattern
    if m:
        print(f'file name without extension is {m.group(1)}') # regular expressions with grouping to extract or change parts of string
    else:
        print(f'{file_path} is not a csv file')

    # Loading data from CSV file using pandas
    try:
        df = pandas.read_csv(file_path) 
    # 'df' is DataFrame containing data from CSV file
        print(df)
    except FileNotFoundError: 
        print(f"Error: file at '{file_path}' was not found.") # error for user

    key_list = [] #creating list
    key_list.append('Pre-Assessment') # appending item to list
    key_list.append('Post-Assessment')

    key_copy = []

    for key in key_list: #appending item to list iteratively
        key_copy.append(key)

    print('key_copy', key_copy)
    
    #removing kets iteratively from copied list
    for key in key_list:
        key_copy.remove(key) 

    data_dict = {}                    

    #open output file in append mode
    output = open('output-stats.txt', 'a')
    
    #Processing each key in the key list
    for key in key_list:
        #creating dictionary entry for each key and storing corresponding values
        data_dict[key] = df[key].values
        # Calculating statistics for the data associated with the key
        mean_value, max_value, median_value, mode_value = calculate_statistics(data_dict[key])
        # Printing and writing statistics to the output file
        print(f"{key} Mean: {mean_value}, Max: {max_value}, Median: {median_value}, Mode: {mode_value}")
        output.write(f"Mean: {mean_value}, Max: {max_value}, Median: {median_value}, Mode: {mode_value}")
    # Closing output file
    output.close()

    #Calculating mean improvement using NumPy
    Pre_Assessment = numpy.array(data_dict['Pre-Assessment'])
    Post_Assessment = numpy.array(data_dict['Post-Assessment'])
    print('Mean Improvement from Pre to Post Assessment is', numpy.mean(Post_Assessment-Pre_Assessment)) 

    # Filtering rows where Post-Assessmenmt scores are greater than Pre-Assessment scores
    Improved = df[df['Post-Assessment'] > df['Pre-Assessment']] 

    print(f'{Improved.shape[0]} out of {df.shape[0]} students have improved scores from Pre_Assessment to  Post_Assessment')

    # Creating empty DataFrame for output
    output_df = pandas.DataFrame()
    #Processing each key in data dictionary
    for key in data_dict.keys():
        #Adding columns to the output DataFrame
        output_df[key] = data_dict[key] 
        #Ressetting data associated with each key to an empty list
        data_dict[key] = [] 

    #Writing output DataFrame to CSV file
    output_df.to_csv('output.csv')
