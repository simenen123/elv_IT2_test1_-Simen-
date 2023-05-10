import csv
import matplotlib.pyplot as plt

filnavn = "tidsbruk.csv"


alle = []

tid_2010 = []

alder = []

kjønn = []

desimaltal_tider = []

fullstendig_tid = []

inntektsgivende = []

menn_inntektsgivende = []

menn_husholdningsarbeid = []

husholdning = []

kvinner_inntektsgivende = []

kvinner_husholdningsarbeid = []

#kode for å regne til desimaltall hvis man har minutter
def regn_ut_tid(tider):
    tider = str(tider)
    ny_tider = tider.split(".")
    minutter = ny_tider[1]
    timer = ny_tider[0]
    minutter = float(minutter)
    timer = float(timer)
    minutter = minutter/60
    result = float(ny_tider[0]) + minutter
    return result



with open(filnavn, encoding="latin-1") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  
  for rad in filinnhold:
    alle.append(rad[0])
    kjønn.append(rad[1])
    tid_2010.append(float(rad[7]))
    alder.append(rad[2])


#gjør dem til desimaltall
for element in tid_2010:
    desimaltal_tider.append(regn_ut_tid(element))



#Herfra regner man ut gjennomsnitten for menn i intektsgivende
#får bare inntektsgivende
for jobb in alle:
  filtrert_data = jobb.split(",")
  if filtrert_data[0] == "Inntektsgivende arbeid":
    inntektsgivende.append(filtrert_data[0])
  if jobb == "Husholdsarbeid i alt":
    husholdning.append(filtrert_data[0])


inntektsgivende_og_kjønn = list(zip(inntektsgivende, kjønn))

#Lager listen med menn_inntektsgivende og kvinner_inntektsgivende (ferdig)
for gender in inntektsgivende_og_kjønn:
    if gender[1] == "Menn":
        menn_inntektsgivende.append(gender)
    if gender[1] == "Kvinner":
        kvinner_inntektsgivende.append(gender)

#liste med desimaltall-tid for inntektsgivende
menn_inntektsgivende_og_tid = list(zip(menn_inntektsgivende, desimaltal_tider))

menn_inntektsgivende_og_tid_og_alder =  list(zip(menn_inntektsgivende_og_tid, alder))


#for element in menn_inntektsgivende_og_tid_og_alder:
for element in menn_inntektsgivende_og_tid_og_alder:
    if menn_inntektsgivende_og_tid_og_alder[0][1] == "16-24 Ã¥r":
        fullstendig_tid.append((menn_inntektsgivende_og_tid_og_alder[0][0][1]*16)/100)
    if menn_inntektsgivende_og_tid_og_alder[0][1] == "25-44 Ã¥r":
        fullstendig_tid.append((menn_inntektsgivende_og_tid_og_alder[0][0][1]*36)/100)
    if menn_inntektsgivende_og_tid_og_alder[0][1] == "45-66 Ã¥r":
        fullstendig_tid.append((menn_inntektsgivende_og_tid_og_alder[0][0][1]*34)/100)
    if menn_inntektsgivende_og_tid_og_alder[0][1] == "67-74 Ã¥r":
        fullstendig_tid.append((menn_inntektsgivende_og_tid_og_alder[0][0][1]*34)/100)
    
menn_inntektsgivende_sum = 0 
for element in fullstendig_tid:
    menn_inntektsgivende_sum = menn_inntektsgivende_sum + element


#herfra er det gjennomsnitstiden til husholdarbeidere


husholdsarbeid_og_kjønn = list(zip(husholdning, kjønn))

for gender in husholdsarbeid_og_kjønn:
    if gender[1] == "Menn":
        menn_husholdningsarbeid.append(gender)
    if gender[1] == "Kvinner":
        kvinner_husholdningsarbeid.append(gender)

menn_husholdningsarbeid_og_tid = list(zip(menn_husholdningsarbeid, desimaltal_tider))

menn_husholdningsarbeid_og_tid_og_alder = list(zip(menn_husholdningsarbeid_og_tid, alder))

#for element in menn_inntektsgivende_og_tid_og_alder:
for element in menn_husholdningsarbeid_og_tid_og_alder:
    if menn_husholdningsarbeid_og_tid_og_alder[0][1] == "16-24 Ã¥r":
        fullstendig_tid.append((menn_husholdningsarbeid_og_tid_og_alder[0][0][1]*16)/100)
    if menn_husholdningsarbeid_og_tid_og_alder[0][1] == "25-44 Ã¥r":
        fullstendig_tid.append((menn_husholdningsarbeid_og_tid_og_alder[0][0][1]*36)/100)
    if menn_husholdningsarbeid_og_tid_og_alder[0][1] == "45-66 Ã¥r":
        fullstendig_tid.append((menn_husholdningsarbeid_og_tid_og_alder[0][0][1]*34)/100)
    if menn_husholdningsarbeid_og_tid_og_alder[0][1] == "67-74 Ã¥r":
        fullstendig_tid.append((menn_husholdningsarbeid_og_tid_og_alder[0][0][1]*34)/100)
    
menn_husholdningsarbeid_sum = 0 
for element in fullstendig_tid:
    menn_husholdningsarbeid_sum = menn_husholdningsarbeid_sum + element

print(menn_husholdningsarbeid_sum)

print(menn_inntektsgivende_sum)

summer = [menn_husholdningsarbeid_sum, menn_inntektsgivende_sum]

navn = ["menn_husholdningsarbeid", "menn_inntektsgivende"]

plt.figure(figsize=(10, 5))          # Angir dimensjoner for figure-objektet
plt.barh(navn,summer)  # Lager stolpediagrammet
plt.subplots_adjust(left=0.4)        # Øker plassen på venstre side av diagrammet
plt.grid(axis="x")                   # Legger til rutenett (bare vertikale linjer)
plt.show()



