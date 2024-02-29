numone = int(input("Nota do primeiro bimestre "))
if numone < 0 or numone >= 11:
    print("Por favor, números de 0 a 10")
    exit()
        
numtwo = int(input("Nota do segundo bimestre "))
if numtwo < 0 or numtwo >= 11:
    print("Por favor, números de 0 a 10")
    exit()

numtrhee = int(input("Nota do terceiro bimestre "))
if numtrhee < 0 or numtrhee >= 11:
    print("Por favor, números de 0 a 10")
    exit()

numfour = int(input("Nota do quarto bimestre "))
if numfour < 0 or numfour >= 11:
    print("Por favor, números de 0 a 10")
    exit()

finalnote = numone + numtwo + numtrhee + numfour

if finalnote >= 20:
 print("Parabens! Voce foi aprovado com "+str(finalnote))
elif finalnote >=15:
 print("Voce está na recuperação com "+str(finalnote))
else:
 print("Voce foi reprovado com "+finalnote)
