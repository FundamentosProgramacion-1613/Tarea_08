#Oswaldo Morales Rodriguez
#A01378566
#Tarea 8


def quitarElementos(lista):   #Funcion remover elemtos de lista siendo el primero y el ultimo
    
    if len(lista)>0:
        nueva=lista[::]
        nueva.pop(0)
        nueva.pop()
        print(lista, nueva)
    else:
        nueva=[]
        print(lista,nueva)
        
def removerRepetidos(lista):   #Funcion que comprueba los repetidos y los elimina solo dejando uno
    for i in lista:
        x=lista.count(i)
        if x!=1:
            lista.remove(i)
    print(lista)

def sumaLista(lista):   #Funcion para la suma de listas
    nueva=[]
    valor=0
    for i in lista:
        valor=valor+i
        nueva.append(valor)
    print(lista, nueva)
    
def compararOrden(lista):   #Funcion para saber si estan en orden o no
    nueva=lista[:]
    nueva.sort()
    if nueva == lista:
        print("Los valores estan en orden", True)
    else:
        print("Los valores no estan en orden", False)
        
def comprobarRepetidos(lista):   #Saber si hay mas de uno
    valor=0
    for i in  lista:
        x=lista.count(i)
        if x>1:
            valor+=1
        else:
            valor+=0
    if valor>=1:
        print(True)
    else:
        print (False)
        
def comprobarAnagrama(lista1,lista2):  #Comparacion de palabras
    lista1.sort()
    lista2.sort()
    if lista1==lista2:
        print(True)
    else:
        print(False)
        
        
    
    
    
    
    
def main():
    a=[1,2,3,4,5]
    b=[1,2]
    c=[]
    d=["X","J","O","P"]
    e=["A","B","C","D","E"]
    f=[34,68,106,212,424]
    g=[1,8,3,4,3,1,2,7]
    h=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    i=["A","B","B","C","D","C","D","J","H","I","O"]

        

    palabra1=input("Palabra de anagrama")
    palabra2=input("Palabra a compaarar")
    lista1=list(palabra1)
    lista2=list(palabra2)
    comprobarAnagrama(lista1,lista2)
    
    quitarElementos(a)
    quitarElementos(b)
    quitarElementos(c)
    
    removerRepetidos(g)
    removerRepetidos(h)
    removerRepetidos(i)
    
    sumaLista(a)
    sumaLista(b)
    sumaLista(g)
    
    compararOrden(a)
    compararOrden(g)
    compararOrden(d)
    compararOrden(e)
    
    comprobarRepetidos(a)
    comprobarRepetidos(h)
    comprobarRepetidos(i)
    
main()