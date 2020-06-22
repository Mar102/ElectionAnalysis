
## This is the MOST efficient and clean way to read the file with unknown path 
import csv
import os

##### Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

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

##### Declaring new list to get counties 
county_options = []

##### Declaring empty dictionary to add votes per county 
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning Candidate and Winning Count Tracker 
winning_county= ""
winning_county_count= 0
winning_county_percentage = 0

##### Open the election results and read the file

with open(file_to_load) as election_data:

##### To do: read and analyze the data here. 

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. #1
        total_votes +=1
        # Get the candidate name from each row
        candidate_name = row[2]
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

##### Save the results to text file    
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    countyHeader = (f"\nCounty Votes:\n")
    print(countyHeader)
    txt_file.write(countyHeader)

    # Confirm the voter turnout for each county that voted
    for county in county_votes:
        voteCounty = county_votes[county]
        voteCounty_percentage = float(voteCounty) / float(total_votes) * 100
        voteCounty_results = (f"{county}: {voteCounty_percentage:.1f}% ({voteCounty:,})\n")
        print(voteCounty_results)
        txt_file.write(voteCounty_results)
        # Determine winning county 
        if (voteCounty > winning_county_count) and (voteCounty_percentage > winning_county_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_county_count = voteCounty
            winning_county_percentage = voteCounty_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_county = county
    # Print the winning candidate's results to the terminal.
    winning_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        # Print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)