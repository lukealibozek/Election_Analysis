import csv
import os
# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who receive votes.
# 3. The percentage of votes each cadidate won
# 4. The total number of votes each vandidate won
# 5. The winner of the election based on popular vote

cwd = os.getcwd()
files = os.listdir(cwd)
print(f"Files in {cwd}: {files}")

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)

#Close the file.
election_data.close()

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:
#     #Write some data
#     txt_file.write("Counties in the Election\n--------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# #Close the file
# .close()