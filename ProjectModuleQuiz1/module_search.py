def buscar(contact, value):
    if len(contact) == 0:
        print("No hay contactos agregados")
    else:
        if value in contact.values():
            print("El contacto se encuentra en la lista")
        else:
            print("El contacto no se encuentra")
    return 

if __name__ == "__main__":
    buscar