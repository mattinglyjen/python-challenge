# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 07:28:25 2021

@author: pulle
"""
import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

# def print_percentages(budget_data):
#     months = str(budget_data[0])
#     profit = str(budget_data[1])

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open election_data_csv

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #count number of votes
        count = count + 1
        # create and add list for candidates
        candidatelist.append(row[2])
    for x in set(candidatelist):
        unique_candidate.append(x)
        # set variable for number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # variable for percent of votes per candidate
        z = (y/count)*100
        round(z, 2)
        vote_percent.append(z)
        vote_percent_round = [round(y, 2) for y in vote_percent]  

     
        
     
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]


 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent_round[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")



with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent_round[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
