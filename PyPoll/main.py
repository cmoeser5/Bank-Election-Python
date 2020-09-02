import os
import csv

total_votes = 0

path = os.path.join("Resources", "election_data.csv")

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1

print(total_votes)
        