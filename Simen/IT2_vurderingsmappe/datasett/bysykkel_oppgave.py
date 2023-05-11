import csv
import matplotlib.pyplot as plt

filnavn = "sykkeldata.csv"


startlokasjon_mengde = []

startlokasjoner = []

startsted_bruk = []


with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=",")

  overskrifter = next(filinnhold)
  
  for rad in filinnhold:
    startlokasjon_mengde.append(rad[4])

y = 0
while y < len(startlokasjon_mengde):
    if startlokasjon_mengde[y] not in startlokasjoner:
        startlokasjoner.append(startlokasjon_mengde[y])
    y = y+ 1

for k in startlokasjoner:
     x = startlokasjon_mengde.count(k)
     startsted_bruk.append(x)  
fullstendig_liste = list(zip(startlokasjoner, startsted_bruk))
fullstendig_liste.sort(key=lambda y:y[1])
print(fullstendig_liste[-3:])
#print(startlokasjoner)

