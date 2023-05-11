import csv
import matplotlib.pyplot as plt

filnavn = "roboter.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
industri_roboter =  []

roboter_i_bruk_2018 = []
roboter_i_bruk_2018_sum = 0

roboter_i_bruk_2020 = []
roboter_i_bruk_2020_sum = 0

roboter_i_bruk_2022 = []
roboter_i_bruk_2022_sum = 0

total_sum = []

aarstall = [2018, 2020, 2022]

with open(filnavn, encoding="latin-1") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  
  for rad in filinnhold:
    roboter_i_bruk_2018.append(int(rad[2] + rad[5]))
    roboter_i_bruk_2020.append(int(rad[3] + rad[6]))
    roboter_i_bruk_2022.append(int(rad[4] + rad[7]))

for ele in range(0, len(roboter_i_bruk_2018)):
  roboter_i_bruk_2018_sum = roboter_i_bruk_2018_sum + roboter_i_bruk_2018[ele]
total_sum.append(roboter_i_bruk_2018_sum)

for ele in range(0, len(roboter_i_bruk_2020)):
  roboter_i_bruk_2020_sum = roboter_i_bruk_2020_sum + roboter_i_bruk_2020[ele]
total_sum.append(roboter_i_bruk_2020_sum)

for ele in range(0, len(roboter_i_bruk_2022)):
  roboter_i_bruk_2022_sum = roboter_i_bruk_2022_sum + roboter_i_bruk_2022[ele]
total_sum.append(roboter_i_bruk_2022_sum)



plt.figure(figsize=(10, 5))          # Angir dimensjoner for figure-objektet
plt.barh(aarstall, total_sum)  # Lager stolpediagrammet
plt.subplots_adjust(left=0.4)        # Øker plassen på venstre side av diagrammet
plt.grid(axis="x")                   # Legger til rutenett (bare vertikale linjer)
plt.show()




#Tegner grafen
plt.plot(aarstall, total_sum, color="red")
plt.grid()
plt.show()