#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.kdnuggets.com/companies/consulting.html

from bs4 import BeautifulSoup
import csv

f = csv.writer(open("results.csv", "w"))

url = "kdnuggets.html"
soup = BeautifulSoup(open(url).read())

links = soup.find_all("a")
#elements = soup.find("li")
soap = soup.select('li.text')

for link in links:
    text = [s.find('li').text for s in soap]
    url, name = link.get("href"), link.text
    f.writerow([url, name, text])
