numone = int(input("Nota do primeiro bimestre "))
if numone < 0:
    print("Por favor, números de 0 a 10")
    exit()
if numone >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()
        
numtwo = int(input("Nota do segundo bimestre "))
if numtwo < 0:
    print("Por favor, números de 0 a 10")
    exit()
if numtwo >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()


numtrhee = int(input("Nota do terceiro bimestre "))
if numtrhee < 0:
    print("Por favor, números de 0 a 10")
    exit()
if numtrhee >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()

numfour = int(input("Nota do quarto bimestre "))
if numfour < 0:
    print("Por favor, números de 0 a 10")
    exit()
if numfour >= 11:
 print("Por favor, Numero de 0 a 10")
 exit()


finalnote = numone + numtwo + numtrhee + numfour

if finalnote >= 20:
 print("voce foi aprovado")
elif finalnote >=15:
 print("Voce está na recuperação")
else:
 print("Voce foi reprovado ")