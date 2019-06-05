# Dependencies
import statistics
import csv
import os

# Create the input file path
csvpath = os.path.join('Resources', 'election_data.csv')

# Open csv file
with open(csvpath, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    cvs_header = next(csvreader)

    # Create empty lists to store Voter IDs and Candidates
    voter_ids = []
    candidates = []

    # Append info in the data file to appropriate lists
    for row in csvreader:
        voter_ids.append(row[0])
        candidates.append(row[2])

# BUILD A LIST OF UNIQUE CANDIDATES - REMOVE DUPLICATES IN ORIGINAL LIST
### Create an empty list to store unique candidates
unique_candidates = []

### Iterate through candidates
for candidate in candidates:
    # If candidate is already in unique_candidates, proceed to the next one
    # Otherwise, append candidate to unique_candidates
    if candidate in unique_candidates:
        continue
    else:
        unique_candidates.append(candidate)

# PROCESS VOTING RESULTS
### Find the total number of votes cast
total_votes = len(voter_ids)

### Create empty lists to store the votes each candidate received
candidates_votes = []
voting_percentages = []

### Iterate through the candidates and ... 
for candidate in unique_candidates:
    # ... count the number of votes 
    num_votes = candidates.count(candidate)
    # ... find the percentage of votes
    percent_vote = round((num_votes/total_votes) * 100, 3)
    # ... add the number of votes and the voting percentage to lists
    candidates_votes.append(num_votes)
    voting_percentages.append(percent_vote)

### Determine winner
winner_idx = candidates_votes.index(max(candidates_votes))
winner = unique_candidates[winner_idx]

# PRINT RESULTS TO TERMINAL AND EXPORT TO A TEXT FILE
### Create a list of strings with appropriate messages
lines = ["Election Results", 
         "------------------------",
         f"Total Votes: {total_votes}",
         "------------------------", 
]
for i in range(0,len(unique_candidates)):
    lines.append(f"{unique_candidates[i]}: {voting_percentages[i]}% ({candidates_votes[i]})")
lines.append("------------------------")
lines.append(f"Winner: {winner}")
lines.append("------------------------")

### Open an output file
file1 = open(r"PyPoll_results.txt",  'w+')

### Print lines ...
for line in lines:
    # ... to the terminal
    print(line)
    # ... to the text file
    file1.write(f"{line}\n")

### Close the text file
file1.close()