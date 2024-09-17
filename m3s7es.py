estudiantes = [
{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
{'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
{'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
{'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
{'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]


print("Requisito #1\n")
for i in range(len(estudiantes)):
	promedio=float(0)
	if (estudiantes[i])["edad"]>=18:
		for j in range(3):
			promedio=((estudiantes[i])["calificaciones"])[j]+promedio
		promedio=promedio/3
		if promedio>85:
			print(f"El estudiante {((estudiantes[i])["nombre"])}, de edad {estudiantes[i]["edad"]} tiene un promedio de: {promedio:.3f}.")

print("######################")
print("Requisito #2\n")

for i in estudiantes:
	aux=0
	promedio=0
	if i["edad"]>=18:
		for j in range(1,i["edad"]):
			if i["edad"]%j==0:
				aux+=1
		if aux==1:
			for j in range(3):
				promedio=i["calificaciones"][j]+promedio
			promedio=promedio/3
			print(f"El estudiante {i["nombre"]}, de edad {i["edad"]} tiene un promedio de: {promedio:.3f}.")


