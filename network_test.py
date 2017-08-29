#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import itertools

f = open("notices_cpv_decoded_test.csv", "rb")

notice_list = []
aktualis_notice = "15135-2016"
kategoria_list = []
with open("cpv_cpv_network_by_notice_test.csv", "w") as output:
    for line in f.readlines()[1:]:
        notice = line.split('\t')[0].lower()
        if notice != aktualis_notice:
            my_list = [(kategoria_list[i], kategoria_list[j]) for i in\
                   range(len(kategoria_list)) for j in range(i + 1, len(kategoria_list))]
            print str(my_list)
            kategoria = line.split('\t')[1].lower().rstrip("\n")
            kategoria_list.append(kategoria)
            aktualis_notice = notice

        elif notice == aktualis_notice:
            kategoria = line.split('\t')[1].lower().rstrip("\n")
            if kategoria not in kategoria_list:
                kategoria_list.append(kategoria)
            else:
                pass
        else:
            print "nem ok"

f.close()
