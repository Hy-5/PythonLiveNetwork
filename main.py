import sys, socket, RSA
import server

def main(argv):
    server.serverSocket() #Running the server on an infinite loop, listening to the client

if __name__=="__main__":
    main(sys.argv[1:])