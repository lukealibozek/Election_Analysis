# Election_Analysis

**Resources**:
* **Data Source**: election_results.csv
* **Analysis Output**: election_analysis.txt
* **Script**: PyPoll_Challenge.py 


## Overview of Election Audit: 
This project involved the construction of a python script that analyzed raw election output to perform the following analyses:
* A count of total votes cast
* A count of votes per candidate, along with percentage of total
* A count of votes by county, along with percentage of total.
* A determination of the county with the largest voter turnout
* A determination of the winning candidate

**Data Source**: election_results.csv
* A CSV file containing 369,712 rows of information
* The data contained the following headers:
    * Ballot ID
    * County
    * Candidate Name
* Each row represented one unique vote

###  **Script Breakdown**

PyPoll_Challenge.py

#### 1. Setup
Adding dependencies, establishing path variables, and initializing lists, arrays, and variables to hold vote counts and calculations

```python
# Import dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
winning_county = ""
winning_county_turnout = 0
```
#### 2. Read the results, count the votes

```python
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header, skip using next()
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # CANDIDATE COUNT: If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # COUNTY COUNT: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
#### 3. Run analysis to find winners, write to file
```python
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"Votes by County:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # COUNTY RESULTS: Write a for loop to get the county from the county dictionary.
    for county_name in county_list:
        # Retrieve the county vote count.
        c_vote_count = county_votes[county_name]
        # Calculate the percentage of votes for the county.
        c_vote_percentage = float(c_vote_count) / float(total_votes) * 100

        # Print the county results to the terminal.
        county_results = f"{county_name}: {c_vote_percentage:.1f}% ({c_vote_count:,})\n"
        print(county_results,end="")
        # Save the county votes to a text file.
        txt_file.write(county_results)
        # WINNING COUNTY: Write an if statement to determine the winning county and get its vote count.
        if (c_vote_count > winning_county_turnout):
            winning_county_turnout = c_vote_count
            winning_county = county_name
            winning_county_percentage = c_vote_percentage

    # Print the county with the largest turnout to the terminal.
    winning_county_statement = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n\n"
    )
    print(winning_county_statement,end="")

    # Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_statement)

    # CANDIDATE RESULTS: Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # WINNING CANDIDATE: Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```

### **Challenges**

What we were not able to determine from this information:
* The voter turnout per county as a percentage of **total registered voters per county**. It is possible that, despite one county having the highest voter count of total votes cast, that other counties could have had 100% voter turnout but were too small to outweigh a larger county. 

## Election Audit Results:
---
**Total Votes**: 369,711

---

**Votes by County**:
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

**Largest County Turnout**: Denver

---
**Votes by Candidate**:
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)
---
**Election Winner**:  
* **Diana DeGette**
* 272,892 Votes
* 73.8% of Total Votes


## Election-Audit Summary: 
This script was successfully able to analyze a considerable amount of data in a short amount of time and produce results in an orderly manner. This script can be reusable with a few minor tweaks.

The source file has three data points that need to be maintained in structure, but can be tweaked to accept alternate data:
* **Ballot ID**: This column contains a unique identifier for each row of data. Required.
* **County**: This column contains metadata for the data that is to be counted.
* **Candidate**: This contains the primary value to be counted. 

The script will automatically create a list of items found in columns 2 and 3, so the only tweaks necessary  are to change the naming conventions.

For example: To run a survey to determine the most popular donut.
1. Find and replace the word "candidate" for the word "donut"
2. Find and replace the word "county" for the word "store"
3. Ensure the paths point to the correct locations (lines 6 and 8)
4. Ensure the election/survey results have "store" in column 2, and "donut" in column 3.

The resulting script will tally vote counts for the most popular donut, and provide additional statistics regarding the most popular donut store. Of course, with a survey such as this, it is important to limit input to a list of options, as custom input can result in inaccurate analysis (misspellings or extra spaces, for example, would result in multiple list entries for a single item, splitting votes).