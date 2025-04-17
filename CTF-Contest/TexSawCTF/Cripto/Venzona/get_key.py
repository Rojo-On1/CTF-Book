def calculate_key(plain_text, cipher_text):
    """Calcula la clave dada el texto plano y el texto cifrado."""
    key = []
    for p, c in zip(plain_text, cipher_text):
        # Convertir letras a números (A=0, B=1, ..., Z=25)
        p_num = ord(p) - ord('A')
        c_num = ord(c) - ord('A')
        # Calcular la clave usando resta modular
        k_num = (c_num - p_num) % 26
        key.append(chr(k_num + ord('A')))
    return ''.join(key)

# Ejemplo de uso
if __name__ == "__main__":
    # Texto plano y texto cifrado
    plain_text = input("Ingrese el texto plano: ").replace(" ","")
    cipher_text = input("Ingrse el texto cifrado: ")  # "KHOOR" es "HELLO" cifrado con la clave "K"
    
    # Calcular la clave
    print("="*100)
    key = calculate_key(plain_text, cipher_text)
    print(f"Texto plano: {plain_text}")
    print(f"Texto cifrado: {cipher_text}")
    print(f"Clave calculada: {key}")