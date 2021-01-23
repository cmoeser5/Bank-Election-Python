# Background

This project utilized Python to analyze company financial records and election voting records.

## PyBank
* Analyzed company financial records.

* Created a Python script that analyzes the records to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
  
 * In this script:
   * Paths were created using os.join for both the .csv and .txt files
   * For loops were utilized to iterate over the rows of the dataset and appended to empty lists
   * Calculations were used to create new variables
   * Generated an output with the analysis results
   
``` python
#create empty lists
total_votes = 0
Khan_votes = []
Correy_votes = []
Li_votes = []
OTooley_votes = []

#generate paths to the data csv
path = os.path.join("Resources", "election_data.csv")
        
outfile = os.path.join("Analysis", "PyPoll.txt")

#read csv and append data to the empty lists
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
        
#calculate the percentages of total votes per candidate
Khan_percent = (total_Khan_votes / total_votes) * 100
Correy_percent = (total_Correy_votes / total_votes) * 100
Li_percent = (total_Li_votes / total_votes) * 100
OTooley_percent = (total_OTooley_votes / total_votes) *100

#create a dictionary with the candidates and their total votes       
dict_winner = {
    "Khan": int(total_Khan_votes),
    "Correy": int(total_Correy_votes),
    "Li": int(total_Li_votes),
    "O'Tooley": int(total_OTooley_votes)
    }
#create variables to show the keys and values of the candidates and votes
candidates = list(dict_winner.keys())
votes = list(dict_winner.values())

#generate winner variable with the candidate with the highest vote count
winner = candidates[votes.index(max(votes))]
```
```

         Financial Analysis
        ----------------------------
        Total Months: 86
        Total: $38382578
        Average  Change: $-2315.12
        Greatest Increase in Profits: Feb-2012 ($1926159)
        Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

## PyPoll
* Analyzed an election dataset to modernize the vote counting process.

* Created a Python script that analyzes the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote
  
* In this script:
  * Paths were created using os.join for both the .csv and .txt files
  * For loops were utilized to iterate over the rows of the dataset and appended to empty lists
  * Calculations were used to create new variables
  * Generated an output with the analysis results
  
```python
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
```
  
```
        Election Results
        -------------------------
        Total Votes: 3521001
        -------------------------
        Khan:  63.000% (2218231)
        Correy:  20.000% (704200)
        Li:  14.000% (492940)
        O'Tooley:  3.000% (105630)
        -------------------------
        Winner: Khan
        -------------------------
```
