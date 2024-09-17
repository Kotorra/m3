
matriz=[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
diccionario={}

for i in matriz:
	for j in range(len(i)):
		if i[0]==0:
			break
		else:
			if i[j]!=0:
				print(f"Elemento: {i[j]}")
			else:
				continue
				
diccionario["A"]=matriz[0]
diccionario["B"]=matriz[1]
diccionario["C"]=matriz[2]
diccionario["D"]=matriz[3]

for i in diccionario:
	print(f"{i}:{diccionario[i]}")
