# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to existing count
        candidate_votes[candidate_name] += 1
# Vote analysis - percentage of votes for each candidate by looping through

# Iterate through the candidate list
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    #Calc %
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print name and % of votes
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote ({votes:,}).\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winner
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")

print(winning_candidate_summary)

# 3. Print the total votes.
#print(candidate_votes)