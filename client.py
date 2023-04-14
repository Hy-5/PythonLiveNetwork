import socket, subprocess, time
#import RSA

def clientSocket():
    c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("localhost", 8080))
    #c.send(b"TESTING")

    #from . import RSA
    try:
        import RSA
    except:
        pass
    #rsa=subprocess.run(["python39", ".\RSA.py"])
    #rsa=subprocess.Popen(["python3.9", ".\RSA.py"])
    binaryList=0
    try:
        with open("encryptedListBinary.bin", "rb") as f: #reads the image as a binary file
            binaryList=f.read()
    except FileNotFoundError as e:
        pass
    
    
    try:
        print(f"Sending {len(binaryList)} bytes of image data.") #Total Byte count for verification
        c.sendall(binaryList) #Sends the entire binary image over the network (to be preceded by the encryption)
    except:
        print("Encrypted file in the process of being created")
    c.close()

clientSocket()