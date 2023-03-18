import socket

def clientSocket():
    c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("localhost", 8080))
    c.send(b"TESTING")

    """with open("123.png", "rb") as f:
        image_data=f.read()
    c.sendall(image_data)"""

    return c

clientSocket()