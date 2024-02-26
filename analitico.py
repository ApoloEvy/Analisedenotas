numOne = int(input("Nota do primeiro bimestre "))
numtwo = int(input("Nota do segundo bimestre "))
numtrhee = int(input("Nota do terceiro bimestre "))
numfour = int(input("Nota do quarto bimestre "))

finalnote = numOne + numtwo + numtrhee + numfour

if finalnote >= 20:
 print("voce foi aprovado")
elif finalnote >=15:
 print("Voce está na recuperação")
else:
 print("Voce foi reprovado ")
