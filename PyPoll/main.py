import os
import csv

total_votes = 0
Khan_votes = []
Correy_votes = []
Li_votes = []
OTooley_votes = []

path = os.path.join("Resources", "election_data.csv")

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

print(total_Khan_votes)
print(total_Correy_votes)
print(total_Li_votes)
print(total_OTooley_votes)

Khan_percent = (total_Khan_votes / total_votes) * 100
Correy_percent = (total_Correy_votes / total_votes) * 100
Li_percent = (total_Li_votes / total_votes) * 100
OTooley_percent = (total_OTooley_votes / total_votes) *100

print(Khan_percent)
print(Correy_percent)
print(Li_percent)
print(OTooley_percent)