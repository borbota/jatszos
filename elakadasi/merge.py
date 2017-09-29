import pandas as pd

export = pd.read_csv("data_minta.csv", sep = "\t")
erd = pd.read_csv("erdekeltseg_2017_felev.csv", sep = "\t")

erdekeltseg_teszt = pd.merge(export, erd, left_on = "cegnev", right_on = "cegnev")
erdekeltseg_teszt.to_csv("export_erdekeltsegekkel.csv", sep = "\t", index = False)
