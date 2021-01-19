import os
import csv

output_file = os.path.join("..","Resources", "budget_data.csv")

total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
total_month_change = 0
average_month_change = 0
greatest_increase= 0
greatest_increase_month = " "
greatest_decrease = 0
greatest_increase_month = " "

with open(output_file, n=" ") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        
        # monthly change in profit
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss
            
        # monthly change
        total_month_change += month_change
        
        # profit/loss value for previous month
        prev_profit_loss = int(row[1])
        
        # greatest increase in profits
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        
        # greatest decrease in losses
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]
            
# average monthly change         
average_month_change = total_month_change / (total_months - 1)