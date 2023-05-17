def elimianr(contact):
    print("\tLista de contactos:")
    for i, j in contact.items():
        print( f"Nombre -->  {j} /// telefono --> {i}  ")
    try:
        telefono = int(input("Ingrese el número de contacto a eliminar: "))
    except ValueError:
        print("Debe ser el número!!!")
    confirmar = input(f"Seguro de eliminar el contacto {contact[telefono]} del listado? si/no: ").lower()
    if confirmar == "si":
        if telefono in contact:
            contact.pop(telefono)
    return contact

if __name__ == "__main__":
    elimianr