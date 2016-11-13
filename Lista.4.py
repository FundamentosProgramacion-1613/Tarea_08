#encoding: UTF-8
#Edgar Eduardo Alvarado Duran
#Problema 5

def main():
    lista = []
    lista1 = []
    n = int(input("Ingresa un numero"))
    while n != -1:
        lista.append(n)
        lista1.append(n)
        n = int(input("Ingresa otro numero"))
    print (lista)
    lista.count(n)
    if lista == lista1:
        print (True)
    else:
        print (False)

main()