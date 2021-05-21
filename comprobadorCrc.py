#funciones

def toList(x):
	l = []
	for i in range (0,len(x)):
		l.append(int(x[i]))
	return (l)

def toString(x):
	str1 =""
	for i in range (0,len(x)):
		str1+=str(x[i])
	return (str1)

def mostrarDivision(codigoLista,polinomioLista):
    print(toString(codigoLista))
    print(toString(polinomioLista))
    print("-------------")

def borrarPrimerosCeros(codigoLista,polinomioGeneradorLista):
    i = codigoLista[0]
    while( (len(codigoLista) > len(polinomioGeneradorLista)-1) and i == 0):
        codigoLista.pop(0)
        i = codigoLista[0]

def divisionUnBit(bit1, bit2):
    if(bit1 == bit2):
        return 0
    else:
        return 1

def divisionPolinomios(codigoLista, polinomioLista):
    mostrarDivision(codigoLista,polinomioLista)
    for i in range(0,len(polinomioLista)):
        codigoLista[i] = divisionUnBit(codigoLista[i],polinomioLista[i])
    input()
#    if(len(codigoLista) > len(polinomioLista)):
   


#tomar el valor del codigo y del polinomio generador
codigo = input("Ingrese el codigo binario: ")
codigoLista = toList(codigo)
polinomioGenerador = input("Ingrese el polinomio generador: ")
polinomioGeneradorLista = toList(polinomioGenerador)


#dividir el codigo por el polinomio generador hasta que se tenga un valor del codigo
while(len(codigoLista) > (len(polinomioGeneradorLista)-1) ):
   divisionPolinomios(codigoLista,polinomioGeneradorLista)
   borrarPrimerosCeros(codigoLista,polinomioGeneradorLista)

print("CRC: " + toString(codigoLista))