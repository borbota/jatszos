#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import itertools
import csv

f = open("notices_cpv_decoded_just_main_cpvcategory.csv", "rb")

notice_list = []
aktualis_notice = "27086-2016"

with open("cpv_cpv_network_by_notice.csv", "wb") as output:
    csv_out = csv.writer(output)
    kategoria_list = []
    for line in f.readlines()[1:]:
        notice = line.split('\t')[0].lower()
        kategoria = line.split('\t')[1].rstrip("\n")
        if notice != aktualis_notice:
            if len(kategoria_list) > 1:
                my_list = [(kategoria_list[i], kategoria_list[j]) for i in\
                       range(len(kategoria_list)) for j in range(i + 1, len(kategoria_list))]
                for row in my_list:
                    csv_out.writerow(row)
                kategoria_list = []
                kategoria_list.append(kategoria)
            else:
                pass
        elif notice == aktualis_notice:
            if kategoria not in kategoria_list:
                kategoria_list.append(kategoria)
            else:
                pass
        else:
            print "nem ok"
        aktualis_notice = notice

f.close()
