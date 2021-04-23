from hashlib import sha256
import binascii
import os
def encode():
	message = input("	Entrez le message a chiffrer : ")
	key = input("	Entrez la clé : ")

	keys = str(sha256(key.encode ('ascii')).hexdigest())

	message_en_binaire = '0' + bin(int.from_bytes(message.encode(), 'big'))[2:]
	keys_en_binaire = '0' + bin(int.from_bytes(keys.encode(), 'big'))[2:]

	liste_message = list(message_en_binaire)
	liste_key = list(keys_en_binaire)

	longueur_message = len(message_en_binaire)

	try:
		a = 0
		resultat_binaire = ""
		for loop in range(longueur_message):
			if liste_key[a] == liste_message[a]:
				resultat_binaire = resultat_binaire + "0"
			else:
				resultat_binaire = resultat_binaire + "1"
			a = a + 1

		result = resultat_binaire
		print(f'	Voici votre message encodé {result}')
	except IndexError:
		print("	Votre clé est trop petite pour votre message veuillez l'agrandir")

def decode():
	message = input("	Entrez le message a decrypter : ")
	key = input("	Entrez la clé : ")
	keys = str(sha256(key.encode ('ascii')).hexdigest())

	message_en_binaire = message
	keys_en_binaire = '0' + bin(int.from_bytes(keys.encode(), 'big'))[2:]

	liste_message = list(message_en_binaire)
	liste_key = list(keys_en_binaire)

	longueur_message = len(message_en_binaire)


	a = 0
	resultat_binaire = ""
	for loop in range(longueur_message):
		if liste_key[a] == liste_message[a]:
			resultat_binaire = resultat_binaire + "0"
		else:
			resultat_binaire = resultat_binaire + "1"
		a = a + 1
	try:
		binary_int = int(resultat_binaire, 2)
		byte_number = binary_int.bit_length() + 7 // 8
		binary_array = binary_int.to_bytes(byte_number, "big")
		result = binary_array.decode()
		print(f'	Voici votre message decodé : {result}')
	except ValueError:
		print('Vous devez entrer une clé et/ou un message valide')
		pass

	

if __name__ == '__main__':
	os.system('cls')
	mode = input("""
		__   __            ______                     _           
		\ \ / /           |  ____|                   | |          
		 \ V / ___  _ __  | |__   _ __   ___ ___   __| | ___ _ __ 
		  > < / _ \| '__| |  __| | '_ \ / __/ _ \ / _` |/ _ \ '__|
		 / . \ (_) | |    | |____| | | | (__ (_) | (_| |  __/ |   
		/_/ \_\___/|_|    |______|_| |_|\___\___/ \__,_|\___|_|   
		by LeRatGondin

	Dechiffrer message : 1
	Chiffrer message : 2
	
	>>> """)
	if mode == "2":
		encode()
	if mode == "1":
		decode()