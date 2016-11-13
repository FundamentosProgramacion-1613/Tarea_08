#encoding: UTF-8
#Edgar Eduardo Alvarado Duran
#Problema 3

lista1 = []
lista2 = []

def calcularLista():
    n = raw_input("Ingresa un numero")
    while n != "-1":
        lista1.append(n)
        lista2.append(n)
        n = raw_input("Ingresa un numero")
    lista1.sort()
    if lista1 == lista2:
        return True
    else:
        return False

def main():
    lista1
    print ("La lista", lista1, "es", calcularLista())
        
main()