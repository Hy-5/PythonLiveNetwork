--WIP--

Live network architecture to host python apps and test RSA encryption in a live environment

1.  Make sure you have an IDE that runs python installed on your machine (or a python interpreter if you would rather use the terminal)
2.  To install the dependencies, open your IDE or a terminal in the source folder, and run <pip install -r requirements.txt> #without the quotes <>
3.  Run the main function: <python main.py> #without the quotes <>
4.  Wait until you see a message in the terminal saying "Server is up" followed by the socket address
5.  If the message "Server is up" takes a while to appear, go to the RSA.py file, and comment out the last line ("plt.show"). The code will still run, but you'll skip the automatic
    display of the encrypted image that tends to hang up sometimes
6.  Run the client in a separate terminal: <python client.py> #without the quotes <>