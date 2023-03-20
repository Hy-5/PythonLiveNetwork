import subprocess, sys, socket, subprocess, RSA
import server, client

necessaryImports=["socket"]


for i in necessaryImports:
    try:
        __import__(i)
    except ModuleNotFoundError:
        print(f"{i} missing. Installing {i} now")
        subprocess.check_call(["pip", "install", i])
        __import__(i)


def main(argv):
    server.serverSocket() #Running the server on an infinite loop, listening to the client

if __name__=="__main__":
    main(sys.argv[1:])