import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

total_months = 0
profit_loss = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_months += 1
        
        profit_loss.append(int(row[1]))
        
        
net_total = sum(profit_loss)  

print(total_months)
print(net_total)