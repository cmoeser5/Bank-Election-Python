import os
import csv

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

path = os.path.join("Resources", "election_data.csv")

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        
        if row[2] == "Khan":
            Khan_votes += 1
            
        elif row[2] == "Correy":
            Correy_votes += 1
            
        elif row[2] == "Li":
            Li_votes += 1
            
        else:
            OTooley_votes += 1
            

print(Khan_votes)
print(Correy_votes)
print(Li_votes)
print(OTooley_votes)
        