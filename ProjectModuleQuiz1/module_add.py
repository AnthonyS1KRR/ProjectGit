def agregar(contact):
    while True:
        try:
            tele = int(input("Número de teléfono: "))
            if not tele in contact:
                name = input("Nombre del contacto: ")
                if not name in contact.values():
                    contact[tele] = name
                else:
                    print("No se pueden repetir nombres")
                    continue
            else:
                print("El número de contacto no se puede repetir")
                continue
        except Exception:
            print("Deben ser valores validos")
        return

if __name__ == "__main__":
    agregar