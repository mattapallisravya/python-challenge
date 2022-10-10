# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
print("Financial Analysis")
print("-----------------------------------------------")
numberOfMonths=[]
amount=[]
changeInProfit=[]
total=0
#greatestIncreaseInProfits=0
#greatestDecreaseInProfits=0



with open(csvpath) as budgetFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budgetFile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    counter=0
    for items in csvreader:
        total=total+int(items[1])
        counter=counter+1
        amount.append(int(items[1]))
        numberOfMonths.append(items[0])
    print("Total Months : ", len(numberOfMonths))
    
    for num in range(0,len(amount)-1):
        #total=total+amount[num]
        change=amount[num+1]-amount[num]
        changeInProfit.append(change)
    averageChange=sum(changeInProfit)/len(changeInProfit)
    greatestIncreaseInProfits=max(changeInProfit)
    greatestDecreaseInProfits=min(changeInProfit)

    print("Total : ",total)
    print(f"Average Change : ${round(averageChange,2)}")
    print(f"Greatest Increase In Profits : {numberOfMonths[changeInProfit.index(greatestIncreaseInProfits)+1]} (${greatestIncreaseInProfits})")
    print(f"Greatest Decrease In Profits : {numberOfMonths[changeInProfit.index(greatestDecreaseInProfits)+1]} (${greatestDecreaseInProfits})")
    #print(len(changeInProfit))
    #print(len(numberOfMonths))
            
       
        

    



