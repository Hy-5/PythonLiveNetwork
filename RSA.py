from PIL import Image
from skimage import color, io
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import sys
import pickle

import codecs
########### RSA Algorithm

### GCD Function
def gcd(a, h):
    while(1):
        temp = a%h
        if(temp == 0):
            return h
        a = h
        h = temp

################# Prime Numbers Big enough
p = 37          ### as high as possible
q = 23
n = p*q
global totient
totient = (p-1)*(q-1)
e = random.randrange(1, totient)
   
#MODIFIED ENCRYPTION FUNCTION
def encrypt(img, img_1D):  

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    global e
    g = gcd(e, totient)
    while g != 1:
        e = random.randrange(1, totient)
        g = gcd(e, totient)


    ### Finding D Value  
    def multiplicative_inverse(e, phi):
        global d
        d = None
        i = 1
        exit = False
        while not exit:
            temp1 = phi*i +1
            d = float(temp1/e)
            d_int = int(d)
            i += 1
            if(d_int == d):
                exit=True
        return int(d)
        
    d = multiplicative_inverse(e, totient)

    #### Now we have p,q,n,totient,e,g,d


    #### Encryption
    # for i in range(0, len(msg_ascii)): then use as msg_ascii[i]
    encrypted_list = []
    for i in range(0, len(img_1D)):
        current_enc = (int(img_1D[i]) ** d) % n
        encrypted_list.append(int(current_enc))
    with open("enc_list", "w") as f:
        f.write(str(encrypted_list))

    ### Displaying encrypted image
    enc_img = np.array(encrypted_list).reshape(img.shape[0], img.shape[1])
    imgplot = plt.imshow(enc_img)
    plt.savefig("encryptedOutput.jpg") #save as jpg
    #print("Starting list is", encryptedList)
    with open("encryptedListBinary.bin", "wb") as file:
        pickle.dump(encrypted_list, file)
    test=str(encrypted_list)
    encodedTest=test.encode("utf-8")
    encodedTesttoInt= int.from_bytes(encodedTest, byteorder="big")
    littletest="Bonjour monsieur"
    littletest=littletest.encode("utf-8")
    littletest=int.from_bytes(littletest, byteorder="big")
    ciphertobetested=pow(littletest, e, n)
    ciphertext=pow(encodedTesttoInt, e, n)
    #print("TEST:\n", encrypted_list)
    print("\n\n\ne is:",e,"\nn is",n,"d is",d,"totient is", totient,"\n\n")
    #print("it is",ciphertobetested)
    #print("TEST:\n", ciphertext)
    """with open("encodedTest", "w") as f:
        f.write(str(ciphertext))"""
    """with open("originalTest", "w") as f:
        f.write(str(test))"""
    return enc_img
    




####### Decryption
def decrypt():
    with open("encryptedListBinary.bin", "rb") as file:
        retrievedEncryptedList=pickle.load(file)
        #print("FINAL LIST is ", retrievedEncryptedList)
    global dec_list
    dec_list = []
    for i in range(0, len(retrievedEncryptedList)):
        current_dec = (retrievedEncryptedList[i] ** e) % n
        dec_list.append(current_dec)
    with open("dec_list", "w") as f:
        f.write(str(dec_list))

    ### conerting decrypted msg to characters
    chars = []
    for num in dec_list:
        chars.append(chr(num))


    decrypted_msg = ''.join(map(lambda x: str(x), chars))
    
    decrypted_img = np.array(dec_list).reshape(img.shape[0], img.shape[1])
    imgplot = plt.imshow(decrypted_img)
    plt.show()
    
    return dec_list

#### Back to Image
def imageRecons(img=color.rgb2gray(io.imread('babygirl.jpg')), data=None, enc_img=None, dec_list=None):
    recovered_img = np.array(dec_list).reshape(img.shape[0], img.shape[1])

    imgplot = plt.imshow(recovered_img)

    fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    axs[0].imshow(data)
    axs[0].set_title('Original')
    axs[1].imshow(enc_img)
    axs[1].set_title('Encrypted')
    axs[2].imshow(recovered_img)
    axs[2].set_title('Decrypted')
    #plt.show()



def main():
    global img
    img = color.rgb2gray(io.imread('babygirl.jpg'))
    #print("TEST")
    data = (img*255).astype(np.uint8)

    imgplot = plt.imshow(data)
    ### Img size = 899, 1174
    img_1D = data.ravel()   # converting to 1D
    encryptedImage=encrypt(img, img_1D)
    #decryptedList=decrypt()
    #imageRecons(img, data, encryptedImage, decryptedList)


    """#new n and e
    stre=str(e)
    strn=str(n)
    newn=strn.encode("utf-8")
    newe=stre.encode("utf-8")
    finaln= int.from_bytes(newn, byteorder="big")
    finale= int.from_bytes(newe, byteorder="big")

    with open("nvariable.bin", "w") as f:
        #finalN=int.from_bytes(str(n).encode(), byteorder="big")
        f.write(str(finaln))"""
    with open("evariable.bin", "w") as f:
        f.write(str(e))

    #plt.show()

main()