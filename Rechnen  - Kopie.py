zahl1 = 80
zahl2 = 40
passt = True
rechenoperator = input('Rechenoperator eingeben:')
if rechenoperator == '-':
    ergebnis = zahl1 - zahl2
elif rechenoperator == '+':
    ergebnis = zahl1 + zahl2
elif rechenoperator == '*':
    ergebnis = zahl1 * zahl2
elif rechenoperator == '/':
    ergebnis = zahl1 / zahl2
else:
    print('falscher Rachenoperator eingegeben')
    passt = False
if passt:
    print(zahl1, rechenoperator, zahl2,'=',ergebnis)