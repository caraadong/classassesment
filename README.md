Overview:

The script will load the user provided csv file and output statistics.

Calculates and outputs statistics such as mean, median, and mode for specified assessment categories.

Determines mean improvement from pre-assessment to post-assessment using NumPy identifying students who have shown improvement.

Features: 

- statistical analysis of assessment data

- calculation of mean improvement using NumPy

- identification of students with improvemed scores

- output of results to console and files

Prereqs:

- Python
- Pandas
- NumPy

(pip3 install pandas numpy)
- 'calculate_statistics' module (ensure it is present)

Usage: 

The user can provide the location of the csv as the first argument. 

For example, python classassessment.py tws-spreadsheet.csv

Outputs:

- mean, max, median, mode for assessment
- mean improvement from pre to post assessment using NumPy
- number of students who have improved

result are save to following files:
- 'output-stats.txt' (statistical summary)
- 'output.csv' (dataframe containing assessment data)

License:


