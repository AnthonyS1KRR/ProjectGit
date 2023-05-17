def mostrar(contact):
    print("\tLista de contactos:")
    for i, j in contact.items():
        print( f"Nombre -->  {j} /// telefono --> {i}  ")

menu = ["Agreagr contacto", "Buscar contacto", "Eliminar contacto", "Mostrar lista de contactos", "Cerrar aplicación"]

def mostrar_menu():
    for i in range(len(menu)):
        print(str(i+1) + ". ", menu[i] )
    return