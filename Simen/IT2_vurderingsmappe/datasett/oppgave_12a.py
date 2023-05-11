import csv
import matplotlib.pyplot as plt

filnavn = "data.csv"


lønn_i_2015 = []
lønn_i_2022 = []
økning_i_prosent = []
kjønn = []
yrke = []
næring = []

fullstendig_liste = []


with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  tomlinje = next(filinnhold)
  tabelltittel11419 = next(filinnhold)
  
  for rad in filinnhold:
    lønn_i_2015.append(rad[5])
    lønn_i_2022.append(rad[12])
    kjønn.append(rad[3])
    yrke.append(rad[2])
    næring.append(rad[1])



i = 0
while i < len(lønn_i_2015):
  try:
    endring_i_prosent = int(lønn_i_2022[i]) / int(lønn_i_2015[i])
    økning_i_prosent.append(endring_i_prosent)
    i = i + 1
  except:
    i = i + 1


zipped_list = list(zip(kjønn, økning_i_prosent))

zipped_list2 = list(zip(yrke, zipped_list))

zipped_list3 = list(zip(næring, zipped_list2))

sorted_list = sorted(zipped_list3, key=lambda x: x[1][1])

print(sorted_list[-3:])




# Tegner grafen
# plt.plot(aarstall, befolkning)
# plt.grid()
# plt.show()