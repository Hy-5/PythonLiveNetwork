import sys, socket

serverHost="localhost"
serverPort=8080

def serverSocket():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((serverHost,serverPort))
    s.listen(1)
    print(f"Server listening on {serverHost}:{serverPort}")
    while True:
        #print("HEEEERRREEEEE :", s.accept())
        conn, addr=s.accept()
        data=conn.recv(1024)
        if data:
            print(f"Data received: {data.decode()}")
            #conn.send(data)
        conn.close()
    """while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            # Receive the image data
            image_data = b""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                image_data += data
            print(f"Received {len(image_data)} bytes of image data.")

            with open("recons.jpg", "wb") as f:
                f.write(image_data)"""
    
    

serverSocket()