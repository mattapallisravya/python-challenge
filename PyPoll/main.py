# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#Specifying the path to write the output to file 
output_path = os.path.join("..", "PyPoll", "Analysis", "output.txt")

#Specifying the path to read the data and to analyse
csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

#Variables
dots="-----------------------------------------------\n" 
counter=0
listOfCandidates=[]
totalVotesCandidateWon={}
totalVotes=0

print(f"Election Results\n{dots}")

# Opening the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as outputFile:
   
    #Writing to output.csv
    outputFile.writelines(f"Election Results\n{dots}")
    
    #opening the file to read data
    with open(csvpath) as electionDataFile:

        # CSV reader specifies delimiter and variable that holds the content
        csvreader = csv.reader(electionDataFile, delimiter=',')
        
        # Skipping the header and storing it in a variable
        csv_header = next(csvreader)
        
        # Reads each row of data after the header
        for line in csvreader:
            
            # To count total number of votes
            counter+=1

            # Appending candidate name and number of votes each candidate won to the dictionary(totalVotesCandidateWon={}).
            if (totalVotesCandidateWon.get(line[2]) == None):
                totalVotesCandidateWon[line[2]]=1
            else:
                totalVotesCandidateWon[line[2]]=totalVotesCandidateWon[line[2]]+1
        
        # Writing to output.csv
        outputFile.writelines(f'Total Votes : {counter}\n{dots}')
        
        # Print total votes to terminal
        print(f'Total Votes : {counter}\n{dots}')
        
        # looping through dictionary to find percentage of votes each candidate won
        for key,value in totalVotesCandidateWon.items():
            
            percentageOfVotes=(value/counter)*100
            
            # Writing Candidate name, percentage of votes each candidate won and total votes each candidate won to output.csv 
            outputFile.writelines(f'{key} : {round(percentageOfVotes,3)}% ({value})\n')
            
            # Printing the Candidate name, percentage of votes each candidate won and total votes each candidate won to terminal
            print(f'{key} : {round(percentageOfVotes,3)}% ({value})')
        
        outputFile.writelines(dots)
        
        print(dots)
        
        # Created two lists from dictionary and getting the winner name using the index of max votes
        maxVotes=list(totalVotesCandidateWon.values())
        maxVotesWonBy=list(totalVotesCandidateWon.keys())
        
        # Writing winner name to output.csv
        outputFile.writelines(f'Winner : {maxVotesWonBy[maxVotes.index(max(maxVotes))]}\n{dots}')

        # Printing the winner name to output.csv
        print(f'Winner : {maxVotesWonBy[maxVotes.index(max(maxVotes))]}\n{dots}')

        
        

    
    
        

   
        

            
        
    
            

    
   
   
   
    
    