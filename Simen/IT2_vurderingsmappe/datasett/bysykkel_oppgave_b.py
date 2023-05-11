import csv
import matplotlib.pyplot as plt

filnavn = "sykkeldata.csv"


dato_for_start_ufiltrert = []

dato_for_start_filtrert = []

dager_brukt = []

søndag_brukt = []
søndag_bruk_sum = 0

lørdag_brukt = []
lørdag_bruk_sum = 0

fredag_brukt = []
fredag_bruk_sum = 0

torsdag_brukt = []
torsdag_bruk_sum = 0

onsdag_brukt = []
onsdag_bruk_sum = 0

tirsdag_brukt = []
tirsdag_bruk_sum = 0

mandag_brukt = []
mandag_bruk_sum = 0

total_sum = []
ukedager = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=",")

  overskrifter = next(filinnhold)
  
  for rad in filinnhold:
    dato_for_start_ufiltrert.append(rad[0])
    
#får ut dagene
for rad in dato_for_start_ufiltrert:
  filtrert_data = rad.split(" ")
  enda_renere_data = filtrert_data[0].split("-")
  dato_for_start_filtrert.append(int(enda_renere_data[2]))


#dato_for_start_filtrert = startlokasjon_mengde

#legger til alle de forskjellige datoene
y = 0
while y < len(dato_for_start_filtrert):
    if dato_for_start_filtrert[y] not in dager_brukt:
       dager_brukt.append(int(dato_for_start_filtrert[y]))
       y = y+ 1
    else:
        y = y+ 1

#Sjekker hvor mange som sykler på datoer som = søndag
for spesifik_dag in dager_brukt:
     ganger_brukt = dato_for_start_filtrert.count(spesifik_dag)
     if spesifik_dag == 1 or spesifik_dag == 8 or spesifik_dag == 15 or spesifik_dag == 22 or spesifik_dag == 29:
        søndag_brukt.append(ganger_brukt)
     elif spesifik_dag == 2 or spesifik_dag == 9 or spesifik_dag == 16 or spesifik_dag == 23 or spesifik_dag == 30:
        mandag_brukt.append(ganger_brukt)
     elif spesifik_dag == 3 or spesifik_dag == 10 or spesifik_dag == 17 or spesifik_dag == 24  or spesifik_dag == 31:
        tirsdag_brukt.append(ganger_brukt)
     elif spesifik_dag == 4 or spesifik_dag == 11 or spesifik_dag == 18 or spesifik_dag == 25:
        onsdag_brukt.append(ganger_brukt)
     elif spesifik_dag == 5 or spesifik_dag == 12 or spesifik_dag == 19 or spesifik_dag == 26 :
        torsdag_brukt.append(ganger_brukt)
     elif spesifik_dag == 6 or spesifik_dag == 13 or spesifik_dag == 20 or spesifik_dag == 27 :
        fredag_brukt.append(ganger_brukt)
     elif spesifik_dag == 7 or spesifik_dag == 14 or spesifik_dag == 21 or spesifik_dag == 28 :
        lørdag_brukt.append(ganger_brukt)

#regner ut summen hvor mange ganger sykkler

for ele in range(0, len(søndag_brukt)):
    søndag_bruk_sum = søndag_bruk_sum + søndag_brukt[ele]
total_sum.append(søndag_bruk_sum)

for ele in range(0, len(lørdag_brukt)):
    lørdag_bruk_sum = lørdag_bruk_sum + lørdag_brukt[ele]
total_sum.append(lørdag_bruk_sum)

for ele in range(0, len(fredag_brukt)):
    fredag_bruk_sum = fredag_bruk_sum + fredag_brukt[ele]
total_sum.append(fredag_bruk_sum)

for ele in range(0, len(torsdag_brukt)):
    torsdag_bruk_sum = torsdag_bruk_sum + torsdag_brukt[ele]
total_sum.append(torsdag_bruk_sum)

for ele in range(0, len(onsdag_brukt)):
    onsdag_bruk_sum = onsdag_bruk_sum + onsdag_brukt[ele]
total_sum.append(onsdag_bruk_sum)

for ele in range(0, len(tirsdag_brukt)):
    tirsdag_bruk_sum = tirsdag_bruk_sum + tirsdag_brukt[ele]
total_sum.append(tirsdag_bruk_sum)

for ele in range(0, len(mandag_brukt)):
    mandag_bruk_sum = mandag_bruk_sum + mandag_brukt[ele]
total_sum.append(mandag_bruk_sum)

total_sum.reverse()
print(total_sum)



plt.figure(figsize=(10, 5))          # Angir dimensjoner for figure-objektet

plt.barh(ukedager, total_sum)  # Lager stolpediagrammet

plt.subplots_adjust(left=0.4)        # Øker plassen på venstre side av diagrammet

plt.grid(axis="x")                   # Legger til rutenett (bare vertikale linjer)
plt.show()