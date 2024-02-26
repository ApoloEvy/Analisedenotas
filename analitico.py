
numone = int(input("Nota do primeiro bimestre "))
if numone >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()

numtwo = int(input("Nota do segundo bimestre "))
if numtwo >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()


numtrhee = int(input("Nota do terceiro bimestre "))
if numtrhee >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()

numfour = int(input("Nota do quarto bimestre "))
if numfour >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()


finalnote = numOne + numtwo + numtrhee + numfour

if finalnote >= 20:
 print("voce foi aprovado")
elif finalnote >=15:
 print("Voce está na recuperação")
else:
 print("Voce foi reprovado ")