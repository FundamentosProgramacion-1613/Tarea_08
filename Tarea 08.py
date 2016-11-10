#encoding: UTF-8
#Autor: Marina Itzel Haro Hernández, A01373471
#Tarea sobre listas

def funcion1(lista):
    num = 0
    lista1 = []
    for i in lista:
        num += i
        lista1.append(num)
    return lista1
    

def funcion2(lista):
    listaNueva=[]
    for i in range(1,len(lista)-1):
        listaNueva.append(lista[i])
    return listaNueva
    
def funcion3(lista):
    for i in range (len(lista)-1):
        if (lista[i] > lista[i+1]):
            return False
    return True
    
def funcion4(palabra1, palabra2):
    palabra11 = list(palabra1)
    palabra12 = list(palabra2)
    if len(palabra11)!=len(palabra12):
        return False
    palabra11 = sorted(palabra1)
    palabra12 = sorted(palabra2)
    if palabra11 == palabra12:
        return True
    else:
        return False
        
def funcion5(lista):
    a = 0
    for i in lista:
        b = lista.count(i)
        if b>1:
            return True
        else:
            return False
            
def funcion6(lista):
    for i in lista:
        while lista.count(i)>1:
            lista.remove(i)
    return lista
    
def main():
    #Listas para probar 
    lista1=[]
    lista2=[1,2]
    lista3=[1,2,3]
    lista4=[1,2,3,7,5]
    lista5=['A','B','C','X','E']
    lista6=[31,32,33,37,35]
    lista7=[1,1,2,2,3]
    lista8=[11,11,11,12,12,24,23,24]
    opcion = 0
    while opcion != 7 :
        opcion = int(input("1. Funcion 1\n2. Funcion 2\n3. Funcion 3\n4. Funcion 4\n5. Funcion 5\n6. Funcion 6\n7. Salir\nTeclea tu opción"))
        if opcion ==1:
            print ("\n")
            #Funcion 1
            print(funcion1(lista1))
            print(funcion1(lista2))
            print(funcion1(lista3))
            print(funcion1(lista4))
            print(funcion1(lista6))
        elif opcion==2:
            print ("\n")
            #Funcion 2
            print(funcion2(lista1))
            print(funcion2(lista2))
            print(funcion2(lista3))
            print(funcion2(lista4))
            print(funcion2(lista5))
            print(funcion2(lista6))
        elif opcion==3:
            print ("\n")
            #Funcion 3
            print(funcion3(lista1)) #True
            print(funcion3(lista2)) #True
            print(funcion3(lista3)) #True
            print(funcion3(lista4)) #False
            print(funcion3(lista5)) #False
            print(funcion3(lista6)) #False
        elif opcion==4:
            print ("\n")
            #Funcion 4
            palabra1 = input("Ingresa una palabra")
            palabra2 = input("Ingresa otra palabra")
            print(funcion4(palabra1, palabra2))
        elif opcion==5:
            print ("\n")
            #Funcion 5
            print(funcion5(lista2))
            print(funcion5(lista3))
            print(funcion5(lista4))
            print(funcion5(lista7))
            print(funcion5(lista8))
        elif opcion==6:
            print ("\n")
            #Funcion 6
            print(funcion6(lista2))
            print(funcion6(lista3))
            print(funcion6(lista7))
            print(funcion6(lista8))
        elif opcion==7:
            print ("\n")
            print("Adios")
        else:
            print ("\n")
            print("Opcion incorrecta")

main()
  