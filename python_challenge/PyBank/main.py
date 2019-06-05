# Dependencies
import statistics
import csv
import os

# Create the input file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open csv file
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    cvs_header = next(csvreader)

    # Create empty lists to store Dates and profits/losses
    dates = []
    profits_losses = []

    # Append info in the data file to appropriate lists
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Count the total number of months in the data set
month_num = len(dates)

# Find the net total amount of Profits/Losses
total = sum(profits_losses)

# CHANGE IN PROFITS/LOSSES
### Create an empty list to store change
change = []

### Append calculations to empty list
for i in range(1,len(profits_losses)):

    previous_PL = profits_losses[i-1]
    current_PL = profits_losses[i]
    current_change = current_PL-previous_PL

    change.append(current_change)

### Find the average change
average_change = round(statistics.mean(change), 2)

### Find the greatest increase - store in a dictionary that includes 
### month and value
month_index = change.index(max(change))
greatest_increase = {'month': dates[month_index],
                     'value': max(change)}

### Find the greatest decrease - store in a dictionary that includes 
### month and value
month_index = change.index(min(change))
greatest_decrease = {'month': dates[month_index],
                     'value': min(change)}

# PRINT RESULTS TO THE TERMINAL AND EXPORT RESULTS TO A TEXT FILE
### Create a list of strings with appropriate messages
lines = ["Financial Analysis", 
         "------------------------",
         f"Total Months: {month_num}", 
         f"Total: ${total}",
         f"Average Change: ${average_change}",
         f"Greates Increase in Profilts: {greatest_increase['month']} (${greatest_increase['value']})",
         f"Greates Decrease in Profilts: {greatest_decrease['month']} (${greatest_decrease['value']})",
]

### Open an output file
file1 = open(r"PyBank_results.txt",  'w+')

### Print lines ...
for line in lines:
    # ... to the terminal
    print(line)
    # ... to the text file
    file1.write(f"{line}\n")

### Close the text file
file1.close()
