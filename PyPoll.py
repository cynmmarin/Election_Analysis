# Dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")

# Write three counties to the file.
outfile.write("Countries in the Election\n--------------------------\n")

# Write three counties to the file.
outfile.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()

# Open the election results and read the file.
with open(file_to_load) as election_data:
 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row in the CSV file.
    headers = next(file_reader)
    print(headers)