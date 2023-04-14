from PIL import Image
from skimage import color, io
import matplotlib.pyplot as plt
import numpy as np
import json
import socket
import select
import os
import time

def attacker():
	#No need to hardvode e anymore
	#e = 475
	with open("evariable.bin", "r") as f:
		e=int(f.read().strip())

	def rsaDecrypt(n, c, e, p, q):
		def euclidAlgo(a, b):
			if a == 0:
				return (b, 0, 1)
			else:
				g, y, x = euclidAlgo(b % a, a)
				return (g, x - (b // a) * y, y)

		totient = (p - 1) * (q - 1)
		g, x, y = euclidAlgo(e, totient)
		d = x % totient

		# Decrypt ciphertext
		plaintext = pow(c, d, n)

		return plaintext

	# opens list of ciphered pixels
	with open('dec_list', 'r') as f:
		cipherlistStr = f.read()
	cipherlist = json.loads(cipherlistStr)

	# Reading t2 (enc) to check for matching data
	with open('enc_list', 'r') as f:
		t2_str = f.read()
	t2_list = json.loads(t2_str)

	for p in range(2, 40):
		for q in range(2, 40):
			if p != q:
				# pixel per pixel decryption
				plaintextlist = []
				for c in cipherlist:
					n=p*q
					plaintext = rsaDecrypt(n, c, e, p, q)
					plaintextlist.append(plaintext)
				
				#if plaintextlist=t2, then matching p and q were found
				if plaintextlist == t2_list:
					print("Found a match")
					print("p:", p)
					print("q:", q)
					#print("e:", e)
					break

		if plaintextlist == t2_list:
		
			dec_list = []
			with open('dec_list', 'r') as f:
				dec_list = json.load(f)

			### conerting decrypted msg to characters
			chars = []
			for num in dec_list:
				chars.append(chr(num))

			img = color.rgb2gray(io.imread('babygirl.jpg'))
			decrypted_msg = ''.join(map(lambda x: str(x), chars))
			decrypted_img = np.array(dec_list).reshape(img.shape[0], img.shape[1])
			imgplot = plt.imshow(decrypted_img)
			plt.savefig("./attackresult/reconstructedImage.jpg")
			break

	else:
		print("No dice")
	print("Decryption of intercepted data over.\nFile saved as ./attackresult/reconstructedImage.jpg.")
		
		
def main():
	print("Waiting for data to arrive\n")
	while True:
		if (os.path.exists("evariable.bin")):
			size=os.path.getsize("encryptedListBinary.bin")
			print(f"Server received {size} bytes of image data.\nIntercepted.") #Total Byte count for verification
			userinp=input("Press 1 if you want to run the attack\n")
			if userinp=="1":
				attacker()
				break
			else:
				print("Terminating the program")


	"""serverHost="localhost"
	serverPort=8080
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setblocking(False)
	s.connect((serverHost, serverPort))
	while True:
		ready_to_read, _, _ = select.select([s], [], [], 0)
		if ready_to_read:
			data = s.recv(1024)
			if data:
				s.close()
				print(f"Server received {len(data)} bytes of image data.\nIntercepted.") #Total Byte count for verification
				userinp=input("Press 1 if you want to run the attack")
				if userinp=="1":
					attacker()
				else:
					print("Terminating the program")"""
		
main()