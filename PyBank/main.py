# Python HW

from audioop import avg
import os
import csv

months = []
profit_losses = []
profit_change = []
total_months = 0
total_net = 0

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    previous_net = int(first_row[1])
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])

    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        net_change = int(row[1]) - previous_net
        months.append(row[0])
        profit_losses.append(net_change)
        previous_net = int(row[1])
    print(profit_losses)
    
    greatest_increase = max(profit_losses)
    month_increase = months[profit_losses.index(greatest_increase)]
    greatest_decrease = min(profit_losses)
    month_decrease = months[profit_losses.index(greatest_decrease)]
    net_monthly_avg = 0
    net_monthly_avg = sum(profit_losses) / len(profit_losses)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {month_increase} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n")

print(output)

with open("output.csv", "w") as txt_file:
    txt_file.write(output)
