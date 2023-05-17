import csv
import os

lista_encabezado = ["Cedula", "Nombre", "Ciudad", "Edad"]

DATA = {}

def menu():
    while True:
        menu = ["Escribir encabezado", "Pedir datos", "Escribir datos en el archivo", "Leer datos del archivo", "Salir"]
        print("Bienvenido a...")
        for i in range(len(menu)):
            print(str(i+1) + ". ", menu[i])
        option = int(input("Escoja una opción: "))
        vacio = empty()
        if vacio == True and option == 1:
            write_encabezado()
        else:
            if option == 2:
                get_datos()
            elif option == 3:
                write_file(DATA)
            elif option == 4:
                read_file()
            elif option == 5:
                print("Bye...")
                exit() 

def get_datos():
    for j in lista_encabezado:
        datos = input(f"Digite sú {j} : ")
        DATA[j] = datos
    return
        
def read_file():
    with open("data.txt") as f:
        csv_reader = csv.DictReader(f, delimiter = ",")
        for row in csv_reader:
            for i in lista_encabezado:
                print( f"{i} ---> {row[i]}")
            print("-"*26)

def write_file(DATA):
    with open("data.txt", "a", encoding = "UTF-8", newline = "" ) as f:
        write = csv.DictWriter(f, fieldnames = lista_encabezado)
        write.writerow(DATA)
        
def write_encabezado():
    with open("data.txt", "a", encoding = "UTF-8", newline = "" ) as f:
        write = csv.DictWriter(f, fieldnames = lista_encabezado, quotechar ='"' )
        write.writeheader()

def empty(): 
    with open('data.txt', 'r') as f:
        f.seek(0, os.SEEK_END)
        isempty = f.tell() == 0
        f.seek(0)
    return isempty