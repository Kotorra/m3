palabra="paralelepípedo"
palabramutilada=""
posicion=[]
aux=0
aux1=0

for i in (palabra):
	if (i=="a") or (i=="e") or (i=="í") or (i=="o"):
		aux+=1
	else:
		palabramutilada+=i
		posicion.append(aux)
		aux+=1
		
for k in palabramutilada:
	print("La consonante "+k+" tiene la posicion "+str(posicion[aux1])+".")
	aux1+=1


