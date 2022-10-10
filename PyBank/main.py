# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
print("Financial Analysis")
print("-----------------------------------------------")
total=0




with open(csvpath) as budgetFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)
    
    counter=0
    greatestIncreaseInProfit=0
    greatestDecreaseInProfit=0
    sumOfChangeInProfit=0
    firstRow=True
    for items in csvreader:
        if firstRow==True:
            total=total+int(items[1])
            previousRow=int(items[1])
            counter=counter+1
            firstRow=False
        else:
            total=total+int(items[1])
            netChange=int(items[1])-previousRow
            previousRow=int(items[1])
            sumOfChangeInProfit += netChange
            counter=counter+1
            if netChange > greatestIncreaseInProfit:
                greatestIncreaseInProfit = netChange
                greatestIncreaseInProfitmonth = items[0]
            elif netChange<greatestDecreaseInProfit:
                greatestDecreaseInProfit=netChange
                greatestDecreaseInProfitmonth=items[0]
        
        
       
    
    averageChange=sumOfChangeInProfit/counter-1
   

    print("Total : ",total)
    print(f"Average Change : ${round(averageChange,2)}")
    print(f'Greatest Increase In Profits : {greatestIncreaseInProfitmonth} (${greatestIncreaseInProfit})')
    print(f'Greatest Increase In Profits : {greatestDecreaseInProfitmonth} (${greatestDecreaseInProfit})')
    
    