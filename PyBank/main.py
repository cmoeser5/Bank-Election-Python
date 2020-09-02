import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

total_months = 0

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_months += 1
        
print(total_months)