liste1 = [1,2,3,4,8,9,10,12,15,20]
liste2 = [1,5,9,20,100]

def flett_listene_sammen(list1, list2):
    list3 = list1 + list2
    list3.sort
    return list3

liste3 = flett_listene_sammen(liste1, liste2)

y = -1
z = 0
for i in liste3:
    y = -1
    z = 0
    while z < len(liste3) - 1:
        if liste3[y+1] > liste3[z+1]:
            liste3[y+1], liste3[z+1] = liste3[z+1], liste3[y+1]
        y = y+1
        z = z+1
print(liste3)