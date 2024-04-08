#Importing modules
import os
import csv

#Variables to store file paths
current_directory=os.getcwd()
csvpath=os.path.join('Resources','election_data.csv')
directorypath=os.path.join(current_directory,'Resources')
outputfile='PyPoll_Results.txt'
filepath=os.path.join(directorypath, outputfile)

#Creating lists to store the Votes and Candidate Data in
Vote=[]
Candidate=[]

#Reading in the data from the CSV file
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",") 
    csv_header=next(csvfile)
    for row in csvreader:
        Vote.append(row[0])
        Candidate.append(row[2])

#Creating a variable to store number of votes in
NumVotes=len(Vote)

#Dictionary to store and count candidate votes
Candidate_Votes={}

#Counting the candidate votes
for candidate_name in Candidate:
        if candidate_name not in Candidate_Votes:
            Candidate_Votes[candidate_name]=1
        else:
            Candidate_Votes[candidate_name]+=1

#Dictionary to store and calculate percentage of votes for each candidate in
Candidate_Percentages={}
for candidate, votes in Candidate_Votes.items():
     percentage = (votes/NumVotes)*100
     Candidate_Percentages[candidate]=percentage

#Finding the winner by popular vote
Winner=max(Candidate_Votes,key=Candidate_Votes.get)

#Printing results to the terminal
print(f"Election Results\n"+"-----------------------\n"+"Total Votes: "+str(NumVotes)+"\n-----------------------")

#Printing Candidate Vote Percentages
for candidate, votes in Candidate_Votes.items():
     percentage = Candidate_Percentages[candidate]
     print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-----------------------")
print("Winner: ", Winner)

#Writing results to .txt output file
with open(filepath, 'w') as file:
    file.write("Election Results\n")
    file.write("-----------------------\n")
    file.write("Total Votes: " + str(NumVotes) + "\n")
    file.write("-----------------------\n")
    for candidate, votes in Candidate_Votes.items():
        percentage = Candidate_Percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-----------------------\n")
    file.write(f"Winner: {Winner}")