import csv
import matplotlib.pyplot as plt

filnavn = "roboter.csv"

valgt_år = []

næring = []


with open(filnavn, encoding="latin-1") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  
  for rad in filinnhold:
    næring.append(rad[1])
    valgt_år.append(int(rad[2]))


fullstendig_liste = list(zip(næring, valgt_år))


sorted_list = sorted(fullstendig_liste, key=lambda x: x[1])


#print(sorted_list)
print(sorted_list[-3:])




