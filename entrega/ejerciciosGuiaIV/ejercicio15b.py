flores = ["Rosas", "Oruidea","Lirio","Tulipan","Margarita","Dalia","Hortensia"]
sublist = flores[1:2]
for i in range(2,len(flores)):
    if i%2 == 0:
        sublist.append(flores[i])
print(sublist)