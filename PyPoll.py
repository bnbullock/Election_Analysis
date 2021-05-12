# The data we need to retrieve
# The Total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The winner of the election based on popular vote

#Import Dependencies
import os
import csv

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to save to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Perform analysis

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Skip the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidate to the candidate list
            candidate_options.append(candidate_name)
        
# Print the candidate list
print(candidate_options)
