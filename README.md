Live network architecture to host python apps and test RSA encryption in a live environment

#Required environment - Any OS with python 3.9 (Tested on windows using Vscode for the main.py and separate terminal instances for nrsa.py and client.py)
#Dependencies are listed in the requirements.txt file

1.  Make sure you have an IDE that runs python installed on your machine (or a python interpreter if you would rather use the terminal)
2.  To install the dependencies, open your IDE or a terminal in the source folder, and run <pip install -r requirements.txt> #without the quotes <>
3.  Run the main function: <python main.py> #without the quotes <>
4.  Wait until you see a message in the terminal saying "Server is up" followed by the socket address
5.  Run the attacker on a separate terminal : <python3.9 nrsa.py>
6.  Run the client in a separate terminal: <python client.py> #without the quotes <>
7.  The attacker will show that data has been received from the client. Press 1, then enter on the nrsa terminal to start the bruteforce process.
8.  The final image, decrypted by the nrsa script can be found the in "sourcefolder/attackresult" folder.