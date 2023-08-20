import os
import csv

csv_path = os.path.join("PyPoll", "election_data.csv")


with open(csv_path) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   header = next(csvreader)


   charles = 0
   diana = 0
   raymon = 0


   for row in csvreader:
       if row[2] == "Charles Casper Stockham":
           charles = charles + 1
       if row[2] == "Diana DeGette":
           diana = diana + 1
       if row [2] == "Raymon Anthony Doane":
           raymon = raymon + 1


   total_count = charles + diana + raymon
   total_count_list = [charles, diana, raymon]


   for names in total_count_list:
       if (charles > diana) & (charles > raymon):
           winner = "Charles Casper Stockham"
       elif (diana > charles) & (diana > raymon):
           winner = "Diana DeGette"
       elif (raymon > charles) & (raymon > diana):
           winner = "Raymon Anthony Doane"




   print("Election Results")
   print("--------------------------------")
   print("Total Votes:", total_count)
   print("--------------------------------")
   print("Charles Casper Stockham", (charles / total_count) * 100, "%", " (", charles, ")")
   print("Diana DeGette", ((diana / total_count) * 100), "%", " (", diana, ")")
   print("Raymon Anthony Doane", (raymon / total_count) * 100, "%", " (", raymon, ")")
   print("--------------------------------")
   print("Winner:", winner)
   print("--------------------------------")