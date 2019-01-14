#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import re

f = open("infile.csv", "rb")
with open("outfile.csv", "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter = "\t")
    for line in f.readlines()[1:]:
        names_in_a_row = []
        line1 = line.replace('\n', ' ')
        #line2= line1.replace('\t', ' ')
        line2 = re.sub(' +', ' ', line1)
        line4 = line2.replace('\r', ' ')
        helmname = line4.split('\t')[3]
        names_in_a_row.append(helmname)
        name_list = line4.split('\t')[5]
        names = name_list.split(", ")
        for name in names:
            names_in_a_row.append(name)
        my_list = [(names_in_a_row[i], names_in_a_row[j]) for i in range(len(names_in_a_row)) for j in range(i + 1, len(names_in_a_row))]
        for row in my_list:
            writer.writerow(row)
        names_in_a_row = []
