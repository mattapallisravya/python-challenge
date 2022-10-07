# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print("Financial Analysis")
print("-----------------------------------------------")
with open(csvpath) as budgetFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for items in csvreader:
        print(f'Total Months: {len(items)}')
        totalAmount=sum(items[1])

