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

##### Initialize a total vote counter. #1
total_votes = 0

##### Declaring new list to get candidates
candidate_options = []

##### Declaring empty dictionary to add votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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


 # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. #1
        total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        # Print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


# Print total number of votes. #1
#print(candidate_votes)


# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote 

