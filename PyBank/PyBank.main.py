#PyBank
#Import the os module, Module for reading csv files

import os
import csv

csvpath = "C:/Users/mallo/Documents/python-challenge/PyBank/Resources/budget_data.csv.csv"

#print(csvpath)

 #Create lists to store data. Intialize the variables as required.
months= []
monthly_changes = []
date = []
total_revenue = 0
revenue_change = 0
revenue_change_values = []
revenue_change_average = []
count = 0
previous_revenue_value = 0

with open(csvpath) as csvfile:

    #CSV reader specifies delimter and varaible that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print (csvreader)

    #Read the header row first because there is a header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        #print(row)

        #Create For Loop

        #Calculate the total number of months included in the dataset
        count = count + 1

        #Calculate the net total amount of "Profit/Losses" over the entire period
        total_revenue = total_revenue + int(row[1])

        #Create list for dates       
        date.append(row[0])
        
        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        
        if previous_revenue_value == 0 : 
            previous_revenue_value = int(row[1])
        else:
             revenue_change = int(row[1]) - previous_revenue_value
             revenue_change_values.append(revenue_change)
             previous_revenue_value = int(row[1])

        #Calculate average of the revenue change over entire period
    revenue_change_average = float(sum(revenue_change_values)/len(revenue_change_values))
 
    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase_revenue = max(revenue_change_values)
    greatest_increase_date = date[revenue_change_values.index(max(revenue_change_values))+1]
    
    #greatest_increase_date = date[monthly_changes.index(greatest_increase_revenue)]
                
    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_revenue = min(revenue_change_values)
    greatest_decrease_date = date[revenue_change_values.index(min(revenue_change_values))+1]
    #greatest_decrease_date = date[monthly_changes.index(greatest_decrease_revenue)]

#print the results
print("")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months" + ": " + str(count))
print("Total: " + "$" + str(total_revenue))
print("Average Change: " + "$" + "{:.2f}".format(revenue_change_average))
print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_revenue) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_revenue)+ ")")


#print as a text file
with open('PyBank\Analysis\output.txt', 'w') as output_txt:
    output_txt.write("\n")
    output_txt.write("Financial Analysis\n")
    output_txt.write("----------------------------------------------------------\n")
    output_txt.write(("Total Months" + "+ " + str(count) + "\n" ))
    output_txt.write(("Total: " + "$" + str(total_revenue) + "\n"))
    output_txt.write("Average Change: " + "$" + "{:.2f}".format(revenue_change_average) + "\n")
    output_txt.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_revenue) + ")" + "\n")
    output_txt.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_revenue)+ ")" + "\n")
    