import random
import string

def decrypt(encrypted_message, key):
    """Descifra el mensaje utilizando la clave."""
    decrypted_message = []
    for e, k in zip(encrypted_message, key):
        e_num = ord(e) - ord('A')
        k_num = ord(k) - ord('A')
        # Descifrar usando resta modular
        decrypted_num = (e_num - k_num) % 26
        decrypted_message.append(chr(decrypted_num + ord('A')))
    return ''.join(decrypted_message)

# Ejemplo de uso
if __name__ == "__main__":
    # Mensaje a cifrar
    encrypted_message = input("Ingrese el mensaje cifrado: ")
    # Generar clave
    key = input("Ingrese la llave: ")[:len(encrypted_message)]
    
    # Descifrar el mensaje
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Mensaje descifrado: {decrypted_message}")