#Importing modules
import os
import csv

#Variables to store file paths - received tutoring help on how to get this working
current_directory=os.getcwd() # <-- Tutor John helped me write this line
csvpath=os.path.join('Resources','budget_data.csv')
directorypath=os.path.join(current_directory,'Resources')
outputfile='PyBank_Results.txt'
filepath=os.path.join(current_directory, outputfile)

#Creating lists to store the Date and Profit/Loss data in
Date=[]
ProfitLoss=[]

#Reading in the data from the CSV file
with open(csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",") 
    csv_header=next(csvfile)
    for row in csvreader:
        Date.append(row[0])
        ProfitLoss.append(int(row[1]))

#Loop for Profit/Loss Change value in all rows
PLchange=[ProfitLoss[i+1]-ProfitLoss[i] for i in range(len(ProfitLoss)-1)]

#Identifying the maximum increase along with the date
Max_increase =max(PLchange)
max_increase_index = PLchange.index(Max_increase)
Max_increase_date = Date[max_increase_index+1]

#Identifying the maximum decrease along with the date
Max_decrease =min(PLchange)
max_decrease_index = PLchange.index(Max_decrease)
Max_decrease_date = Date[max_decrease_index+1]

#Identifying the change average
Avg_change = sum(PLchange)/len(PLchange)
Avg_change_round=round(Avg_change,2)

#Identifying variables for Number of Months and Profit/Loss Net Total
Datelistlen=len(Date)
PLNetTotal=sum(ProfitLoss)

#Printing results to the terminal
print("Financial Analysis\n"+"-----------------------\n"+"Total Months: "+str(Datelistlen)+"\nTotal: $"+str(PLNetTotal))
print("Average Change: "+"$"+str(Avg_change_round))
print("Greatest Increase in Profits: "+Max_increase_date,"($" + str(Max_increase)+")")
print("Greatest Decrease in Profits: "+Max_decrease_date,"($" + str(Max_decrease)+")")

#Writing results to .txt output file
with open(filepath, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------\n")
    file.write("Total Months: " + str(len(Date)) + "\n")
    file.write("Total: $" + str(sum(ProfitLoss)) + "\n")
    file.write("Average Change: $" + str(Avg_change_round) + "\n")
    file.write("Greatest Increase in Profits: " + Max_increase_date + " ($" + str(Max_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + Max_decrease_date + " ($" + str(Max_decrease) + ")\n")



      
      


