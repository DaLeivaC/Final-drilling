def hacer_grandioso(lista):
    for i in range(len(lista)):
        lista[i] = "El gran " + lista[i]
    return lista

def imprimir_nombres(lista):
    for i in range (len(lista)):
        print (lista[i])
    
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

magos_originales = magos[:]

magos_grandiosos = hacer_grandioso (magos)

print ("Nombres antes de ser modificados:")

imprimir_nombres (nombres)

print ("Lista de magos grandiosos:")

imprimir_nombres (magos_grandiosos)

print ("Científicos:")

imprimir_nombres (cientificos)

print ("Otros:")

set_cientificos = set (cientificos)
set_magos = set (magos_originales)

otros = list (set(nombres) - set_cientificos - set_magos)

imprimir_nombres (otros)










