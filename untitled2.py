pal=str("yo hago yoga hoy")
a=len(pal)
pal2=str()
b=str(" ")
for i in range(a):
    if (pal[i])!=(" "):
        pal2=pal2+pal[i]
aux=len(pal2)
pal1=str()

for i in (range(aux-1,-1,-1)):
    pal1=pal1+pal2[i]
    
if pal1==pal2:
    print("palindromo")
else:
    print("none palindromo")
