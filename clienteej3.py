import socket

IP = "127.0.0.1"
PORT = 8080


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((IP, PORT))
    print("Conexión establecida con el servidor ")

    while True:
        print("¿Que operacion desea realizar? \n 0= salir (0,0,0)\n 1 = sumar \n 2= multiplicar")
        opcion = input("Introduce un opcion del menú y dos numeros separados por comas: ")

        enviar_mensaje = str.encode(opcion)
        s.send(enviar_mensaje)

        resultado = s.recv(2048).decode("utf-8")
        print("El resultado de la operación es:", resultado)

        if resultado == "Se ha cerrado la calculadora.":
            s.close()
            break

except OSError:
    print("El Socket ya está usado")
    s.close()
except KeyboardInterrupt:
print("\n Se ha cerrado la conexión.")
