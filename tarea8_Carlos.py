#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: Tarea 8

def sumarDatos(listaA):
    listaRA=[]
    suma=0
    for i in listaA:
        suma+=i
        listaRA.append(suma)
    return listaRA

def eliminarDatos(listaB):
    listaRB=[]
    p=1
    for i in listaB:
        if 1<p<len(listaB):
            listaRB.append(i)
        p+=1
    return listaRB

def determinarOrden(listaC):
    listaCR=sorted(listaC)
    #print(listaCR)
    if listaCR==listaC:
        return True
    else:
        return False
    
def encontrarAnagrama(listaD1, listaD2):
    listaRD1=sorted(listaD1)
    listaRD2=sorted(listaD2)
    #print(listaRD1)
    if listaRD1==listaRD2:
        return True
    return False

def encontrarRepetidos(listaE):
    for i in listaE:
        while listaE.count(i)>1:
            return True
    return False

def eliminarRepetidos(listaF):
    for i in listaF:
        while listaF.count(i)>1:
            listaF.remove(i)
    return sorted(listaF)
    
def main():
    #Primer Función
    listaA=[1,2,3]
    print("Tu lista original es", listaA,"tu lista acumulada es:", sumarDatos(listaA))
    listaA=[]
    print("Tu lista original es:", listaA,"tu lista acumulada es:", sumarDatos(listaA))  
    listaA=[5]
    print("Tu lista original es:", listaA,"tu lista acumulada es:", sumarDatos(listaA))
    
    #Segunda Función
    listaB=[1,2,3,4,5]
    print("Tu lista original es:", listaB,"tu lista sin el primer y ultimo dato:",eliminarDatos(listaB))
    listaB=[1,2]
    print("Tu lista original es:", listaB,"tu lista sin el primer y ultimo dato:",eliminarDatos(listaB))
    listaB=[10,3,54,33,25]
    print("Tu lista original es:", listaB,"tu lista sin el primer y ultimo dato:",eliminarDatos(listaB))
    
    #Tercer Función
    listaC=[1,2,3,4,5]
    print("Tu lista:", listaC,"se encuentra ordenada:",determinarOrden(listaC))
    listaC=["A","B","C"]
    print("Tu lista:", listaC,"se encuentra ordenada:",determinarOrden(listaC))
    listaC=["a","x","b"]
    print("Tu lista:", listaC,"se encuentra ordenada:",determinarOrden(listaC))
    
    #Cuarta Función
    listaD1=list("Roma".upper())
    listaD2=list("Mora".upper())
    print("Las palabras", listaD1, listaD2, "son anagramas:",encontrarAnagrama(listaD1,listaD2))
    listaD1=list("Hola".upper())
    listaD2=list("Hello".upper())
    print("Las palabras", listaD1, listaD2, "son anagramas:",encontrarAnagrama(listaD1,listaD2))
    listaD1=list("tarta".upper())
    listaD2=list("trata".upper())
    print("Las palabras", listaD1, listaD2, "son anagramas:",encontrarAnagrama(listaD1,listaD2))
    
    #Quinta Función
    listaE=[1,3,5,6,8]
    print("La lista:", listaE, "contiene elementos repetidos:",encontrarRepetidos(listaE))
    listaE=[1,2,3,1,4,5]
    print("La lista:", listaE, "contiene elementos repetidos:",encontrarRepetidos(listaE))
    listaE=[5,4,3,2,1]
    print("La lista:", listaE, "contiene elementos repetidos:",encontrarRepetidos(listaE))
    
    #Sexta Función
    listaF=[1,8,3,4,3,2,1,7]
    print("Tu lista sin elementos repetidos:",eliminarRepetidos(listaF))
    listaF=[3,2,5,3,6,3,5,8,9,7]
    print("Tu lista sin elementos repetidos:",eliminarRepetidos(listaF))
    listaF=[1,1,2,2,3,3,4,5,6]
    print("Tu lista sin elementos repetidos:",eliminarRepetidos(listaF))
main()