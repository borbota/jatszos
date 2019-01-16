#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import re

f = open("without_stopwords.csv", "r")
with open("outfile.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter = "\t")
    for line in f.readlines()[1:]:
        names_in_a_row = []
        line1 = line.replace('\n', ' ').strip()
        line2 = re.sub(' +', ' ', line1)
        line4 = line2.replace('\r', ' ')
        names_in_a_row = []
        names = line4.split(" ") # or whatever
        for name in names:
            names_in_a_row.append(name)
        my_list = [(names_in_a_row[i], names_in_a_row[j]) for i in range(len(names_in_a_row)) for j in range(i + 1, len(names_in_a_row))]
        names_in_a_row = []
        for row in my_list:
            print(row)
            writer.writerow(row)
        
