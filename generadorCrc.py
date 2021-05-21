#funciones
def agregarCeros(codigoLista, cantidadCeros):
    for i in range(0,cantidadCeros-1):
        codigoLista.append('0')

def toList(palabra):
	lista = []
	for i in range (0,len(palabra)):
		lista.append(int(palabra[i]))
	return (lista)

def toString(lista):
	palabra =""
	for i in range (0,len(lista)):
		palabra+=str(lista[i])
	return (palabra)

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

#agregar (polinomiosGenerador.length() - 1) '0' al codigo
agregarCeros( codigoLista ,len(polinomioGeneradorLista) )

#dividir el codigo por el polinomio generador hasta que se tenga un valor del codigo
while(len(codigoLista) > (len(polinomioGeneradorLista)-1) ):
   divisionPolinomios(codigoLista,polinomioGeneradorLista)
   borrarPrimerosCeros(codigoLista,polinomioGeneradorLista)

print("CRC: " + toString(codigoLista))
