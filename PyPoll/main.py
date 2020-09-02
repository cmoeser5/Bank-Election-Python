import os
import csv

total_votes = 0
Khan_votes = []
Correy_votes = []
Li_votes = []
OTooley_votes = []

path = os.path.join("Resources", "election_data.csv")
        
outfile = os.path.join("Analysis", "PyPoll.txt")


with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
                                  
        if row[2] == "Khan":
            Khan_votes.append(row[2])
        total_Khan_votes = len(Khan_votes) 
                                  
        if row[2] == "Correy":
            Correy_votes.append(row[2])
        total_Correy_votes = len(Correy_votes)
        
        if row[2] == "Li":
            Li_votes.append(row[2])
        total_Li_votes = len(Li_votes)
        
        if row[2] == "O'Tooley":
            OTooley_votes.append(row[2])
        total_OTooley_votes = len(OTooley_votes)
        

Khan_percent = (total_Khan_votes / total_votes) * 100
Correy_percent = (total_Correy_votes / total_votes) * 100
Li_percent = (total_Li_votes / total_votes) * 100
OTooley_percent = (total_OTooley_votes / total_votes) *100

        
dict_winner = {
    "Khan": int(total_Khan_votes),
    "Correy": int(total_Correy_votes),
    "Li": int(total_Li_votes),
    "O'Tooley": int(total_OTooley_votes)
    }

candidates = list(dict_winner.keys())
votes = list(dict_winner.values())

winner = candidates[votes.index(max(votes))]


output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {Khan_percent: .3f}% ({total_Khan_votes})
Correy: {Correy_percent: .3f}% ({total_Correy_votes})
Li: {Li_percent: .3f}% ({total_Li_votes})
O'Tooley: {OTooley_percent: .3f}% ({total_OTooley_votes})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)


with open(outfile, "w") as output_file:
    output_file.write(output)