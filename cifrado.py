import base64

CLAVE = b"miClaveSecreta"  # clave fija interna

def cifrar(mensaje: str) -> str:
    datos = mensaje.encode("utf-8")
    xor = bytes(b ^ CLAVE[i % len(CLAVE)] for i, b in enumerate(datos))
    return base64.urlsafe_b64encode(xor).decode("ascii")

def descifrar(cifrado: str) -> str:
    datos = base64.urlsafe_b64decode(cifrado.encode("ascii"))
    original = bytes(b ^ CLAVE[i % len(CLAVE)] for i, b in enumerate(datos))
    return original.decode("utf-8")

if __name__ == "__main__":
    while True:
        print("\n1) Cifrar\n2) Descifrar\n3) Salir")
        opcion = input("Elegí una opción: ").strip()

        if opcion == "3":
            print("Chau!")
            break
        if opcion not in ("1", "2"):
            print("Opción inválida.")
            continue

        mensaje = input("Mensaje: ")
        try:
            if opcion == "1":
                print("Cifrado:", cifrar(mensaje))
            else:
                print("Descifrado:", descifrar(mensaje))
        except Exception:
            print("No se pudo descifrar: el texto no es válido.")