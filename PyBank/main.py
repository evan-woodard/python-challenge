import os
import csv

csv_path = os.path.join('Pybank', 'budget_data.csv')


with open(csv_path) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   header = next(csvreader)


   months = []
   profits = []


   for row in csvreader:
       months.append(row[0])
       profits.append(int(row[1]))


results = dict(zip(months, profits))


months_count = len(results)
total_profits = sum(profits)
#change_average = 
#change_best = 
#change_worst = 


print("Financial Analysis")
print("----------------------------------------------")
print("Total Months:", months_count)
print("Total: $", total_profits)
#print("Average Change: $", change_average)
#print("Greatest Increase in Profits: $", change_best)
#print("Greatest Decrease in Profits: $", change_worst)


#lines = ["Financial Analysis", "----------------------------------------------", ("Total Months:", months_count), ("Total: $", total_profits), \
 #       ("Average Change: $", change_average), ("Greatest Increase in Profits: $", change_best), ("Greatest Decrease in Profits: $", change_worst)]
#with open('textfile.txt', 'w') as f:
 #  f.write('\n'.join(lines))












