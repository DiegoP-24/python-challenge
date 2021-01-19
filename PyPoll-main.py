import os
import csv

output_file = os.path.join("..","Resources", "election_data.csv")

total_votes = 0
candidate = " "
candidate_list = []
vote_list = []
percent_list = []
winner = " "

with open(output_file, n=" ") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    # Read row after the header
    for row in csvreader:
        # count number of months
        total_votes += 1
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1

# voting percentage            
percent_list = [(100/total_votes) * x for x in vote_list]

# winner candidate
winner = candidate_list[vote_list.index(max(vote_list))]

