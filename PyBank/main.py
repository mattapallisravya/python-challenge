# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Specifying the path to write the output to file 
output_path = os.path.join("..", "PyBank", "Analysis", "output.txt")

# Path to access budget_data.csv file
csvpath = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
    
counter=0
greatestIncreaseInProfit=0
greatestDecreaseInProfit=0
sumOfNetChangeInProfit=0
firstRow=True
total=0
dots="-----------------------------------------------"



# Opening the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as outputFile:
     
    outputFile.writelines(f'Financial Analysis\n{dots}\n')

    #opening the file budget_data.csv by specifying path variable and storing it in a variable
    with open(csvpath) as budgetFile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(budgetFile, delimiter=',')

        # Skipping the header and storing in a variable
        csv_header = next(csvreader)
        
        # Reads each row of data after header
        for items in csvreader:

            # Exectes if condition is true
            if firstRow==True:
                # Finds total profis/loss
                total=total+int(items[1])

                # To count number of rows
                counter+=1
                
                # Assigning 1st value of profit/loss column to a variable
                previousRow=int(items[1])
                
                # Assiging variable to false so that if statement won't execute in next loop
                firstRow=False
            
            else:
                # Finds total profis/loss
                total=total+int(items[1])

                # To count number of rows
                counter+=1
                
                # Calculates net change in profit/loss
                netChange=int(items[1])-previousRow

                # Reassigning previuos row value each time loop runs
                previousRow=int(items[1])

                # Calculating sum of net change in profit
                sumOfNetChangeInProfit += netChange
                
                # calculates greatest increase in profit and corresponding month and year
                if netChange > greatestIncreaseInProfit:
                    greatestIncreaseInProfit = netChange
                    greatestIncreaseInProfitmonth = items[0]
                
                # calculates greatest decrease in profit and corresponding month and year
                elif netChange<greatestDecreaseInProfit:
                    greatestDecreaseInProfit=netChange
                    greatestDecreaseInProfitmonth=items[0]
            
        # Calculating averageChange in profit/loss 
        averageChange=sumOfNetChangeInProfit/(counter-1)

        #Writing to output.csv
        outputFile.writelines(f'Total Months : {counter}\n')
        outputFile.writelines(f"Total : {total}\n")
        outputFile.writelines(f"Average Change : ${round(averageChange,2)}\n")
        outputFile.writelines(f'Greatest Increase In Profits : {greatestIncreaseInProfitmonth} (${greatestIncreaseInProfit})\n')
        outputFile.writelines(f'Greatest Decrease In Profits : {greatestDecreaseInProfitmonth} (${greatestDecreaseInProfit})')
        
        # Printing the values to terminal
        print("Financial Analysis\n",dots)
        print(f'Total Months : {counter}')
        print("Total : ",total)
        print(f"Average Change : ${round(averageChange,2)}")
        print(f'Greatest Increase In Profits : {greatestIncreaseInProfitmonth} (${greatestIncreaseInProfit})')
        print(f'Greatest Decrease In Profits : {greatestDecreaseInProfitmonth} (${greatestDecreaseInProfit})')
       
        
        