#imports for encrypt/decrpyt and delete 

import pyAesCrypt
import os
import colorsys

print("="*60)
print(" Welcome to the windows encpyt/decrypt tool for passwordgen \n")
print('\033[31m' + "WARNING: PLEASE REMEMBER THE PASSWORD FOR DECRYPTING YOUR FILE")
print("WITHOUT IT YOU WILL NOT BE ABLE TO DECRYPT YOUR GENERATED PASSWORDS0")
print(":D\n")
print('\033[0m' + "="*60)

buffersize = 64 * 1024
filename = input("Enter a filename to encrypt/decrypt (Do not use extenstion (.txt) ): ")
password = input("Enter a password to encrypt/decrypt your file: ")
eOrD = input("Would you like to encrypt or decrypt your file (e or d): ").upper()

if eOrD == "E":
    try:
        pyAesCrypt.encryptFile(f'{filename}.txt', f"{filename}.txt.aes", password, buffersize)
    except EOFError as err:
            print('\033[31m' + err)

    deletefile = input("Would you like to delete the plaintext file and keep the AES Encrypted file? (y/n):").upper()

    if deletefile == "Y":
        os.system(f'del {filename}.txt')
    elif deletefile == "N":
        print("Keeping the file!")
    else:
        print('\033[31m' + "Choose either y or n!!")

elif eOrD == "D":
    try:
        pyAesCrypt.decryptFile(f'{filename}.txt.aes', f'{filename}.txt', password, buffersize)
        print("File has been decrypted!")
    except EOFError as err:
        print('\033[31m' + err)

else:
    print('Please choose e or d!!')