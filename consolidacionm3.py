personas=["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pelé","Juanes"]
magos=("Harry Houdini","David Blaine","Teller")
magoslista=[]
magosgrandiosos=[]
cientificos=("Newton","Hawking","Einstein")
famosos=("Messi","Pelé","Juanes")
cientificoslista=[]
famososlista=[]

def separador(origen,discriminador,destino):
	for identidad in discriminador:
		for persona in origen:
			if identidad==persona:
				destino.append(persona)

separador(personas,magos,magoslista)
separador(personas,cientificos,cientificoslista)
separador(personas,famosos,famososlista)

def hacergrandioso():
	for i in range(len(magoslista)):
		magosgrandiosos.append(("El gran ")+magoslista[i])

hacergrandioso()

def imprimir_nombres():
	print("Imprimiendo nombres:\n")
	for nombre in personas:
		print(nombre)
	print("\nFin tarea.\n")

imprimir_nombres()

print("La lista completa:")
print(personas)

print("\nLos magos grandiosos:\n")
for i in magosgrandiosos:
	print(i)

print("\nLos científicos:\n")
for i in cientificoslista:
	print(i)

print("\nLos famosos:\n")
for i in famososlista:
	print(i)