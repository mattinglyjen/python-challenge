# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 07:28:25 2021

@author: pulle
"""
import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# def print_percentages(budget_data):
#     months = str(budget_data[0])
#     profit = str(budget_data[1])


    
with open(budget_data_csv, "r", newline ='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    #recognize header in csv file
    csv_header = next(csvreader)
    months = []
    total_profit = 0
    increase = 0
    decrease = 0
    
    for row in csvreader:
        months.append(row[0])
        # month= len[0]
        #   
        
        print(f"Total Months: {len(months)}")


