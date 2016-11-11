#encoding: UTF-8
#Marlon Brandon Velasco Pinello, A01379404
#Tarea 8

#Ejercicio Uno
def sumaLista(listaN):#listaN = listaNumeros
    listaAcu=[]#listaAcu=ListaAcumuladora
    acumulador=0
    for i in range (0,len(listaN)):
        acumulador=acumulador+listaN[i]
        listaAcu.append(acumulador)
    return listaAcu

#Ejercicio Dos    
def quitaUnoF(listaQ): #quitaUnoF = quitaPrimeroFinal y listaQ = listaQuitar
    listaR=listaQ[1:-1]
    #listaR=listaResultante
    return listaR
    
#Ejercicio Tres
def esDigitoOr(lista): #esDigitoOr = esDigitoOrdenado
    for casilla in lista:
        if str(casilla).isdigit()==False:
            return False
    listaO=sorted(lista)
    if listaO==lista:
        return True
    return False
        
#Ejercicio Cuatro        
def esAnagrama(cadenaUno,cadenaDos):
    listaUno=[]
    listaDos=[]
    cadenaUno=cadenaUno.upper()
    cadenaDos=cadenaDos.upper()
    if len(cadenaUno)==len(cadenaDos):
        for i in range (len(cadenaUno)):
            listaUno.append(ord(cadenaUno[i]))
            listaDos.append(ord(cadenaDos[i]))
        listaUno=sorted(listaUno)
        listaDos=sorted(listaDos)
        if listaUno==listaDos:
            resultado= True
        else:
            resultado= False
    else:
        resultado= False
    return resultado

#Ejercicio Cinco
def esDuplicado(lista):
    for k in lista:
        cantidad=lista.count(k)
        if cantidad>1:
            return True
    return False

#Ejercicio Seis                        
def removerDuplica(lista):
    lista=sorted(lista)
    for k in lista:
        cantidad=lista.count(k)
        if cantidad>1:
            lista.remove(k)
    return lista

def main():
    print("Ejercicio 1")
    listaN=[1,2,3,4,5]
    resultado=sumaLista(listaN)
    print("la lista: "+str(listaN)+" regresa: "+str(resultado))
    listaN=[]
    resultado=sumaLista(listaN)
    print("la lista: "+str(listaN)+" regresa: "+str(resultado))
    listaN=[5]
    resultado=sumaLista(listaN)
    print("la lista: "+str(listaN)+" regresa: "+str(resultado))
    
    print("\nEjercicio 2")
    listaQ=[1,2,3,4,5]
    resultado=quitaUnoF(listaQ)
    print("la lista: "+str(listaQ)+" regresa: "+str(resultado))
    listaQ=[1,2]
    resultado=quitaUnoF(listaQ)
    print("la lista: "+str(listaQ)+" regresa: "+str(resultado))
    listaQ=[]
    resultado=quitaUnoF(listaQ)
    print("la lista: "+str(listaQ)+" regresa: "+str(resultado))
    
    print("\nEjercicio 3")
    lista=[1,2,3,4,5,6]
    resultado=esDigitoOr(lista)
    print("la lista: "+str(lista)+" regresa: "+str(resultado))
    lista=["A","B","Z","C",9]
    resultado=esDigitoOr(lista)
    print("la lista: "+str(lista)+" regresa: "+str(resultado))
    lista=[8,9,1,3,4,6]
    resultado=esDigitoOr(lista)
    print("la lista: "+str(lista)+" regresa: "+str(resultado))
    
    print("\nEjercicio 4")
    cadenaUno="Hola"
    cadenaDos="Hello"
    resultado=esAnagrama(cadenaUno,cadenaDos)
    print("las cadenas: "+cadenaUno+" , "+cadenaDos+" regresan: "+str(resultado))
    cadenaUno="Mora"
    cadenaDos="Roma"
    resultado=esAnagrama(cadenaUno,cadenaDos)
    print("las cadenas: "+cadenaUno+" , "+cadenaDos+" regresan: "+str(resultado))
    
    print("\nEjercicio 5")
    lista=[1,2,3,1,4,5]
    resultado=esDuplicado(lista)
    print("la lista: "+str(lista)+" regresa: "+str(resultado))
    lista=[1,2,3,4,5]
    resultado=esDuplicado(lista)
    print("la lista: "+str(lista)+" regresa: "+str(resultado))
    
    print("\nEjercicio 6")
    lista=[1,8,3,4,3,1,2,7]
    print("la lista: "+str(lista), end="")
    resultado=removerDuplica(lista)
    print(" regresa: "+str(resultado))
    lista=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    print("la lista: "+str(lista), end="")
    resultado=removerDuplica(lista)
    print(" regresa: "+str(resultado))
    
main()