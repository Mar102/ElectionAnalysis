# The data we need to retrieve 
#import csv
#dir (csv)
#print (CVS)

## Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
## Open the election results and read the file 
###election_data = open(file_to_load, 'r')
## To do perform analysis
## Close the file 
###election_data.close()

## REPLACE OPEN/CLOSE Files with a "with statement"
## Open the election results and read the file 
#with open(file_to_load) as election_data:
## To do perform analysis
#     print(election_data)
## Close the file 
###election_data.close()

##### Adding our dependencies.

## This is the MOST efficient and clean way to read the file with unknown path 
import csv
import os

##### Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
#     print(election_data)

##### Assign a variable to save the file to a path.

## Opening a file to write my analysis; blank folder 
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

##### Bring down the command from line #28 to #Open the election results and read the file

with open(file_to_load) as election_data:

##### To do: read and analyze the data here. 

# Using the open() and close() statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()

#Replace the open(), close() statement above with a "with" statement
# Open the election results and read the file.
#with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
#    txt_file.write("Counties in the Election\n----------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
#    for row in file_reader:
#        print(row)

 # Read and Print the header row.
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote 

