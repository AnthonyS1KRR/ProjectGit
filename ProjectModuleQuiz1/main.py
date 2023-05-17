import module_search, module_add, module_del, module_show 
from os import system
system("cls")

contactos = {}

while True:
    print("\tSeleccione una opcion del menú")
    module_show.mostrar_menu()
    try:
        option = int(input("Opción: "))
    except ValueError:
        system("cls")
        print("\nDebe ser un número valido")
        continue
    if option >= 1 and option <= 5:
        if option == 1:
            module_add.agregar(contactos)
        elif option == 2:
            valor = input("Escriba el nombre del contacto: ")
            module_search.buscar(contactos, valor)
        elif option == 3:
            module_del.elimianr(contactos)
        elif option == 4:
            print("Adiosssssssssss")
        elif option == 5:
            print("bye...")
            exit()
    else:
        system("cls")
        print("\nDebe ser una opción entre 1 y 5")
        continue
