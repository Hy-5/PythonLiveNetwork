import sys, socket

serverHost="localhost"
serverPort=8080

def serverSocket():
    print("Server is up")
    fileName="recons"
    fileExtension=".jpg"
    i=0
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((serverHost,serverPort))
    s.listen(1)
    print(f"Server listening on {serverHost}:{serverPort}")
    """while True:
        conn, addr=s.accept()
        data=conn.recv(1024)
        if data:
            print(f"Data received: {data.decode()}")
            #conn.send(data)
        conn.close()"""
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            list_data = b""
            while True: # Receiving and putting image data back together
                data = conn.recv(1024)
                if not data:
                    break
                list_data += data
            i+=1
            print(f"Received {len(list_data)} bytes of image data.") #Total Byte count for verification


            
            print("Reconstructing the image server side")
            from RSA import decrypt
            decrypt()
            
            """with open(fileName+str(i)+fileExtension, "wb") as f: #Reconstructing image (to be preceded by decryption phase )
                f.write(list_data)
                print(f"Image reconstructed as {fileName}"+str(i)+f"{fileExtension}")"""
    
    

serverSocket()