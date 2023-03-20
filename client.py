import socket

def clientSocket():
    c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("localhost", 8080))
    #c.send(b"TESTING")

    with open("output.jpg", "rb") as f: #reads the image as a binary file
        image_data=f.read()
    
    
    print(f"Sending {len(image_data)} bytes of image data.") #Total Byte count for verification
    c.sendall(image_data) #Sends the entire binary image over the network (to be preceded by the encryption)
    c.close()

clientSocket()