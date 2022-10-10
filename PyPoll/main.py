# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')
print("Election Results")
print("-----------------------------------------------")
totalVotesEachCandidateWon=0
listOfCandidates=[]
totalVotesCandidateWon={}
totalVotes=0
i=0
with open(csvpath) as electionDataFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(electionDataFile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    counter=0
    for line in csvreader:
        line[0]
        counter+=1
        if (totalVotesCandidateWon.get(line[2]) == None):
            totalVotesCandidateWon[line[2]]=1
        else:
            totalVotesCandidateWon[line[2]]=totalVotesCandidateWon[line[2]]+1
    print(counter)
    print("---------------------------------------------")
    for key,value in totalVotesCandidateWon.items():
        percentageOfVotes=(value/counter)*100
        print(f'{key}: {round(percentageOfVotes,3)}% ({value})')
    print("---------------------------------------------")
    maxVotes=list(totalVotesCandidateWon.values())
    maxVotesWonBy=list(totalVotesCandidateWon.keys())
    print(maxVotesWonBy[maxVotes.index(max(maxVotes))])
    print("---------------------------------------------")
    
        
        

            
        
    
            

    
   
   
   
    
    