# Background

It's time to put away the Excel sheet and enter the world of programming with Python. This assignment requires using
Pythons concepts to complete two separate challenges: PyBank and PyPoll. Both of challenges encompasses a real-world
situation where Python scripting skills can come in handy.

# Technologies Used
* Python

## PyBank
* In this challenge, you are tasked with creating a Python script for analyzing the financial records of a company, using the dataset called budget_data.csv.

* Your task is to create a Python script that analyzes the records to calculate each of the following:
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
* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process using the dataset called election_data.csv.

* Your task is to create a Python script that analyzes the votes and calculates each of the following:
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
