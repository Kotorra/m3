personas=["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pelé","Juanes"]

magos=["Harry Houdini","David Blaine","Teller"]

magosgrandiosos=[]

cientificos=["Newton","Hawking","Einstein",]

famosos=["Messi","Pelé","Juanes"]

def hacergrandioso():
	for i in range(3):
		magosgrandiosos.append(("El gran ")+magos[i])

def imprimir_nombres():
	for i in range(len(personas)):
		print(personas[i])

print("Lista Completa")
imprimir_nombres()
hacergrandioso()

print("")
print("Magos grandiosos")
for i in range(len(magosgrandiosos)):
	print(magosgrandiosos[i])
print("")
print("Científicos")
for i in range(len(cientificos)):
	print(cientificos[i])
print("")
print("Famosos")
for i in range(len(famosos)):
	print(famosos[i])

