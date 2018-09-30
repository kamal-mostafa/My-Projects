# ============================================================
#
# Student Name (as it appears on cuLearn): Mostafa Kamal
# Student ID (9 digits in angle brackets): <101052833>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

'''
This function will load a test file.

@params			file_name, the name of the file to be loaded
@return			an uppercase string containing the data read from the file
'''
def load_text(file_name):
	file_hndl = open(file_name, "r")
	file_data = file_hndl.read()
	file_hndl.close()
	return file_data.upper()

'''
This function will save data to a text file.

@params			file_name, the name of the file to be saved
			file_data, the data to be written to the file
@return			none
'''

def save_text(file_name, file_data):
	file_hndl = open(file_name, "w")
	file_hndl.write(file_data)
	file_hndl.close()

'''
This function will encode a user provided message with a user provided cipher.

@params			message, the user provided message (either by the load or save function)
			key, the user provided cipher (either by the load or save function)
@return			An uppercase string containing the encrypted message
'''
def encode(message, key):

	encrypted_msg = ''
	key_list = list(key)

	for letter in message:
		letter_index = ord(letter) - 65
		if ord(letter) < 65 or ord(letter) > 90: 
			encrypted_msg += letter
		else:
			encrypted_msg += key_list[letter_index]
	return (encrypted_msg)


'''
This function will decode a user provided message with a user provided cipher.

@params			message, the user provided message (either by the load or save function)
			key, the user provided cipher (either by the load or save function)
@return			An uppercase string containing the decrypted message
'''
def decode(message, key):

	decrypted_msg = ''
	pos = 0
	for letter in message:
		if ord(letter) <65 or ord(letter) > 90:
			decrypted_msg = decrypted_msg + letter
		else:
			for ltr in key:
				if letter == ltr:
					decrypted_msg += chr(65+pos)
				else:
					pos = pos + 1		
			pos = 0	
	return (decrypted_msg)
		

'''
This function will produce a cipher alphabet which is shifted by the user provided number of integers.

@params			integer_shift, a user provided integer, used to shift the alphabet
@return			An uppercase alphabet cipher which has been shifted according to the user provided integer
'''
def caesar_cipher_alphabet(integer_shift):

	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	caesar_alphabet = ''

	for letter in alphabet:
		if ord(letter) + integer_shift > ord("Z"):
			caesar_alphabet += chr(ord(letter) + integer_shift - 26)
		else:
			caesar_alphabet += chr(ord(letter) + integer_shift)
	return (caesar_alphabet)


'''
This function will ask the user to type an alphabet, and then will produce a cipher alphabet based on the unique entry of the 26 letters in the English alphabet (of the user's choice).

@params			none
@return			An uppercase alphabet cipher which the user entered, that is 26 letters long with no duplicates.
			If the user enters an alphabet with less than or more than 26 letters, or has duplicates, this function returns an unmodified default English alphabet
'''
def cryptogram_alphabet():
	user_alphabet = input("Type the 26 letters of the English alphabet in any order as your cipher (without duplicate letters).\n*WARNING* Failure to do so will result in the standard 26 letter English alphabet being returned.\n\nEnter here: ")
	
	count = 0
	duplicate = False
	list_user_alphabet = list(user_alphabet)
	if (len(list_user_alphabet)) != 26:
		print ()
		print ("ERROR: The alphabet you entered is not equal to 26 letters.\nThe standard 26 letter English alphabet will be returned.")
		return ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	else:
		for letter in user_alphabet:
			for ltr in user_alphabet:
				if letter == ltr:
					count = count + 1
					if count > 1:
						duplicate = True
			count = 0
	if duplicate:
		print ()
		print ("ERROR: The alphabet you entered has duplicate letters.\nThe standard 26 letter English alphabet will be returned.")
		return ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	else:
		return (user_alphabet)


'''
This function will ask the user to type a keyword, and then will produce a cipher alphabet based on the keyword, with all the letters of the keyword going to the beginning of the alphabet.

@params			keyword, a user provided keyword used in creating a cipher/key
@return			An uppercase alphabet cipher with the user entered keyword at the beginning of the alphabet, that is 26 letters long with no duplicates.
'''
def keyword_cipher_alphabet(keyword):

	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	listKeyword = list(keyword)
	newKeyword = [listKeyword[0]]
	found = False
	cipher = ''

	for letter in keyword:
		for x in newKeyword:
			if x == letter:
				found = True
		if not found:
			newKeyword.append(letter)
		found = False		


	for letter in alphabet:
		for x in newKeyword:
			if x == letter:
				found = True
		if not found:
			newKeyword.append(letter)
		found = False		

	for letter in newKeyword:
		cipher += letter

	return (cipher)



'''
This is the main function, responsible for the user interface.

@params			none
@return			none
'''
def main():

	print ("====================================================================================================")
	print ("                                 E N C O D E    O R    D E C O D E")
	print ("====================================================================================================")
	print ()
	print ()
	print ("M A I N   M E N U")
	print ("====================================================================================================")
	print ()
	again = '1'
	while again == '1':


		loaded_msg = ''
		loaded_key = ''
		encrypted_msg = ''

		enc_or_dec = input("Would you like to encode or decode a message?\n\n1) Encode (Enter 1)\n2) Decode (Enter 2)\n\nEnter here: ")

		while (enc_or_dec != '1' and enc_or_dec != '2'):
			print ()
			print ("ERROR: That is an incorrect option.")
			print ()
			enc_or_dec = input("Please enter one of the following options again:\n\n1) Encode (Enter 1)\n2) Decode (Enter 2)\n\nEnter here: ")
	
		# If the user wants to encode
		if enc_or_dec == '1':

			print ()
			# Ask the user if they want to load or enter a message
			load_or_save_msg = input("Would you like to:\n\n1) Load a message to Encode (Enter 1)\n2) Input and save a message to Encode (Enter 2)\n\nEnter here: ")

			while (load_or_save_msg != '1' and load_or_save_msg != '2'):
				print ()
				print ("ERROR: That is an incorrect option.")
				print ()
				load_or_save_msg = input("Please enter one of the following options again:\n\n1) Load a message to Encode (Enter 1)\n2) Input and save a message to Encode (Enter 2)\n\nEnter here: ") 

			# If the user wants to load a file that has a message
			if load_or_save_msg == '1':
				print ()
				file_to_load = input("Enter the name of the text file you want to Encode (.txt): ")
				loaded_msg = load_text(file_to_load)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()

			#If the user wants to enter a message into terminal
			elif load_or_save_msg == '2':
				print ()
				msg_to_save = input("Enter the message you want to Encode: ")
				print ()
				file_to_save = input("Enter a name that you want your .txt file to be saved as: ")
				save_text(file_to_save, msg_to_save)
				loaded_msg = load_text(file_to_save)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()

			# Ask the user if they want to load a cipher, or enter one of 3 different cipher keys
			load_or_save_key = input("Would you like to:\n\n1) Load a key/cipher to Encode your message (Enter 1)\n2) Use a Caesar Cipher Alphabet to Encode your message  (Enter 2)\n3) Create your own 26 letter Cryptogram Alphabet Cipher to Encode your message (Enter 3)\n4) Use a Keyword Cipher Alphabet to Encode your message (Enter 4)\n\nEnter here: ")

			while (load_or_save_key != '1' and load_or_save_key != '2' and load_or_save_key != '3' and load_or_save_key != '4'):
				print ()
				print ("ERROR: That is an incorrect option.")
				print ()
				load_or_save_key = input("Please enter one of the following options again:\n\n1) Load a key/cipher to Encode your message with (Enter 1)\n2) Use a Caesar Cipher Alphabet to Encode your message with (Enter 2)\n3) Create your own 26 letter Cryptogram Alphabet Cipher to Encode your message with (Enter 3)\n4) Use a Keyword Cipher Alphabet to Encode your message with (Enter 4)\n\nEnter here: ")

			# If the user wants to load a file that has the key
			if load_or_save_key == '1':
				print ()
				key_to_load = input("Enter the name of the text file that has your key/cipher (.txt): ")
				loaded_key = load_text(key_to_load)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Encode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the encode function on loaded message and loaded key
				encrypted_msg = encode(loaded_msg, loaded_key)
				print ("Your encrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

			# If the user wants to create a caesar cipher
			elif load_or_save_key == '2':
				print ()
				caesar_integer = int(input("Enter an integer amount by which you want your alphabet to be shifted in your Caesar Cipher.\nFor example, an input of '3' will return you a cipher that looks like:\nDEFGHIJKLMNOPQRSTUVWXYZABC\n\nEnter here: "))
				users_caesar_cipher = caesar_cipher_alphabet(caesar_integer)
				print ()
				key_to_save = input("Enter a name that you want your key/cipher file to be saved as: ")
				save_text(key_to_save, users_caesar_cipher)
				loaded_key = load_text(key_to_save)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Encode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the encode function on loaded message and loaded key
				encrypted_msg = encode(loaded_msg, loaded_key)
				print ("Your encrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

			# If the user wants to create their own alphabet
			elif load_or_save_key == '3':
				print ()
				users_cryptogram = cryptogram_alphabet()
				print ()
				key_to_save = input("Enter a name that you want your key/cipher file to be saved as: ")
				save_text (key_to_save, users_cryptogram)
				loaded_key = load_text(key_to_save)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Encode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the encode function on loaded message and loaded key
				encrypted_msg = encode(loaded_msg, loaded_key)
				print ("Your encrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

			# If the user wants to create a keyword cipher
			elif load_or_save_key == '4':
				print ()
				users_keyword = input("Enter a keyword out of which you want to contruct your cipher alphabet.\nFor example the keyword 'HELLO' would return the cipher: 'HELOABCDFGIJKMNPQRSTUVWXYZ' with 26 total letters (duplicates are not counted)\n\nEnter here: ").upper()
				while users_keyword.isalpha() != True:
					print ()
					print ("ERROR: Your keyword cannot have spaces or numbers.")
					print ()
					users_keyword = input("Please enter again a keyword out of which you want to contruct your cipher alphabet.\nFor example the keyword 'HELLO' would return the cipher: 'HELOABCDFGIJKMNPQRSTUVWXYZ' with 26 total letters (duplicates are not counted)\n\nEnter here: ").upper()
				users_keyword_cipher = keyword_cipher_alphabet(users_keyword)
				print ()
				key_to_save = input("Enter a name that you want your key/cipher file to be saved as: ")
				save_text (key_to_save, users_keyword_cipher)
				loaded_key = load_text(key_to_save)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Encode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the encode function on loaded message and loaded key
				encrypted_msg = encode(loaded_msg, loaded_key)
				print ("Your encrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")


		# If the user wants to decode
		if enc_or_dec == '2':

			print ()
			# Ask the user if they want to load or enter a message
			load_or_save_msg = input("Would you like to:\n\n1) Load a message to Decode (Enter 1)\n2) Input and save a message to Decode (Enter 2)\n\nEnter here: ")

			while (load_or_save_msg != '1' and load_or_save_msg != '2'):
				print ()
				print ("ERROR: That is an incorrect option.")
				print ()
				load_or_save_msg = input("Please enter one of the following options again:\n\n1) Load a message to Decode (Enter 1)\n2) Input and save a message to Decode (Enter 2)\n\nEnter here: ") 

			# If the user wants to load a file that has a message
			if load_or_save_msg == '1':
				print ()
				file_to_load = input("Enter the name of the text file you want to Decode (.txt): ")
				loaded_msg = load_text(file_to_load)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()

			#If the user wants to enter a message into terminal
			elif load_or_save_msg == '2':
				print ()
				msg_to_save = input("Enter the message you want to Decode: ")
				print ()
				file_to_save = input("Enter a name that you want your .txt file to be saved as: ")
				save_text(file_to_save, msg_to_save)
				loaded_msg = load_text(file_to_save)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()

			# Ask the user if they want to load a cipher, or enter one of 3 different cipher keys
			load_or_save_key = input("Would you like to:\n\n1) Load a key/cipher to Decode your message (Enter 1)\n2) Use a Caesar Cipher Alphabet to Decode your message  (Enter 2)\n3) Create your own 26 letter Cryptogram Alphabet Cipher to Decode your message (Enter 3)\n4) Use a Keyword Cipher Alphabet to Decode your message (Enter 4)\n\nEnter here: ")

			while (load_or_save_key != '1' and load_or_save_key != '2' and load_or_save_key != '3' and load_or_save_key != '4'):
				print ()
				print ("ERROR: That is an incorrect option.")
				print ()
				load_or_save_key = input("Please enter one of the following options again:\n\n1) Load a key/cipher to Decode your message with (Enter 1)\n2) Use a Caesar Cipher Alphabet to Decode your message with (Enter 2)\n3) Create your own 26 letter Cryptogram Alphabet Cipher to Decode your message with (Enter 3)\n4) Use a Keyword Cipher Alphabet to Decode your message with (Enter 4)\n\nEnter here: ")

			# If the user wants to load a file that has the key
			if load_or_save_key == '1':
				print ()
				key_to_load = input("Enter the name of the text file that has your key/cipher (.txt): ")
				loaded_key = load_text(key_to_load)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Decode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the decode function on loaded message and loaded key
				encrypted_msg = decode(loaded_msg, loaded_key)
				print ("Your decrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

			# If the user wants to create a caesar cipher
			elif load_or_save_key == '2':
				print ()
				caesar_integer = int(input("Enter an integer amount by which you want your alphabet to be shifted in your Caesar Cipher.\nFor example, an input of '3' will return you a cipher that looks like:\nDEFGHIJKLMNOPQRSTUVWXYZABC\n\nEnter here: "))
				users_caesar_cipher = caesar_cipher_alphabet(caesar_integer)
				print ()
				key_to_save = input("Enter a name that you want your key/cipher file to be saved as: ")
				save_text(key_to_save, users_caesar_cipher)
				loaded_key = load_text(key_to_save)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Decode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the decode function on loaded message and loaded key
				encrypted_msg = decode(loaded_msg, loaded_key)
				print ("Your decrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

			# If the user wants to create their own alphabet
			elif load_or_save_key == '3':
				print ()
				users_cryptogram = cryptogram_alphabet()
				print ()
				key_to_save = input("Enter a name that you want your key/cipher file to be saved as: ")
				save_text (key_to_save, users_cryptogram)
				loaded_key = load_text(key_to_save)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Encode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the decode function on loaded message and loaded key
				encrypted_msg = decode(loaded_msg, loaded_key)
				print ("Your decrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

			# If the user wants to create a keyword cipher
			elif load_or_save_key == '4':
				print ()
				users_keyword = input("Enter a keyword out of which you want to contruct your cipher alphabet.\nFor example the keyword 'HELLO' would return the cipher: 'HELOABCDFGIJKMNPQRSTUVWXYZ' with 26 total letters (duplicates are not counted)\n\nEnter here: ").upper()
				while users_keyword.isalpha() != True:
					print ()
					print ("ERROR: Your keyword cannot have spaces or numbers.")
					print ()
					users_keyword = input("Please enter again a keyword out of which you want to contruct your cipher alphabet.\nFor example the keyword 'HELLO' would return the cipher: 'HELOABCDFGIJKMNPQRSTUVWXYZ' with 26 total letters (duplicates are not counted)\n\nEnter here: ").upper()
				users_keyword_cipher = keyword_cipher_alphabet(users_keyword)
				print ()
				key_to_save = input("Enter a name that you want your key/cipher file to be saved as: ")
				save_text (key_to_save, users_keyword_cipher)
				loaded_key = load_text(key_to_save)
				print ()
				print ("====================================================================================================")
				print ("Your current cipher alphabet being to used to Encode: ", loaded_key)
				print ()
				print ("Your unmodified message: ", loaded_msg)
				print ()
				# Call the decode function on loaded message and loaded key
				encrypted_msg = decode(loaded_msg, loaded_key)
				print ("Your decrypted message is:")
				print (encrypted_msg)
				print ("====================================================================================================")

		# Ask if the user would like to repeat the program
		again = input("Would you like to Encode or Decode another message?\n\n1) YES (Enter 1)\n2) NO (Enter 2)\n\nEnter here: ")

		while (again != '1' and again != '2'):
			print()
			again = input("ERROR: That is an invalid entry.\n\nWould you like to Encode or Decode another message?\n\n1) YES (Enter 1)\n2) NO (Enter 2)\n\nEnter here: ")

		if again == '1':
			print ()
			print ()
			print ("M A I N   M E N U")
			print ("====================================================================================================")
			if len(loaded_msg) > 0:
				print ("Your initial unmodified message: ", loaded_msg)
			if len(loaded_key) > 0:
				print ("Your current key/cipher being used: ", loaded_key)
			if len(encrypted_msg) > 0:
				print ("Your current encoded/decoded message: ", encrypted_msg)
			print ("====================================================================================================")
			print ()

		if again == '2':
			print ()
			print ("Thank you for using the ENCODE OR DECODE program.")



#call the main function (the only line in my code that isn't inside a function definition)
main()

