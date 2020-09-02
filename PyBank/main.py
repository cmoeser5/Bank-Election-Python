import os 
import csv

path = os.path.join("Resources", "budget_data.csv")

total_months = 0
profit_loss = []
monthly_change = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_months += 1
        
        profit_loss.append(int(row[1]))
    
    for i in range(1, len(profit_loss)):
        monthly_change.append(int(profit_loss[i]) - int(profit_loss[i - 1]))
    
    
        
        
avg_change = sum(monthly_change) / (total_months - 1)       
net_total = sum(profit_loss)  

print(total_months)
print(net_total)
print(avg_change)