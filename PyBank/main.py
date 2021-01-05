import os 
import csv

#create a path to the csv
path = os.path.join("Resources", "budget_data.csv")

outfile = os.path.join("Analysis", "PyBank.txt")

#generate empty lists
total_months = []
profit_loss = []
monthly_change = []

#read csvs and append data to the empty lists
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_months.append(row[0])
        
        profit_loss.append(int(row[1]))
    
    for i in range(1, len(profit_loss)):
        monthly_change.append(int(profit_loss[i]) - int(profit_loss[i - 1]))
    
#calculate the average change and net total        
avg_change = sum(monthly_change) / len(monthly_change)       
net_total = sum(profit_loss)  

#calculate the greatest monthly increase and decrease
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)

#find the date of the greatest monthly increase and decrease
greatest_increase_date = monthly_change.index(max(monthly_change)) + 1
greatest_decrease_date = monthly_change.index(min(monthly_change)) + 1 


#generate output
output = f"""
Financial Analysis
----------------------------
Total Months: {len(total_months)}
Total: ${net_total}
Average  Change: ${avg_change: .2f}
Greatest Increase in Profits: {total_months[greatest_increase_date]} (${greatest_increase})
Greatest Decrease in Profits: {total_months[greatest_decrease_date]} (${greatest_decrease})
"""

print(output)

with open(outfile, "w") as output_file:
    output_file.write(output)