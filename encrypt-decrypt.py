
import pyAesCrypt, os

buffersize = 64 * 1024 # 64kb size of file

os.system('clear')
# note 
print("MEMORIZE/WRITE THIS PASSWORD DOWN SOMEWHERE")
print("YOU WILL NOT BE ABLE TO DECRYPT YOUR PASSWORD FILE")
print("IF YOU FORGET YOUR PASSWORD!")
print(" ")

filename = input("Enter your password file name (Do not use the extension of the file): ")

# get a password to encrypt or decrypt a file
password = input("Enter a password to encrypt or decrypt your file: ")

# choose to encrypt or decrypt
encryptOrDecrypt = input("Encrypt or Decrypt a file (e or d): ").upper()

if(encryptOrDecrypt == "E"):
    try:
        # encrypt the file
        pyAesCrypt.encryptFile(f"{filename}.txt", f"{filename}.txt.aes", password, buffersize)
        print("\nFile has been Encrypted!")
    except EOFError as err:
        print(err)

    deleteFile = input("\nWould you like to delete the original file and keep the AES encrypted file? (Y/y or N/n): ").upper()

    if(deleteFile == "Y"):
        
        print("\nOriginal text file deleted!\n")
        os.system(f"rm -rf {filename}.txt")
    elif(deleteFile == "N"):
        print("\nKeeping original File!\n")
    else:
        print("\nChoose either Y/y or N/n\n")

elif(encryptOrDecrypt == "D"):
    # decrypt the file
    try:
        pyAesCrypt.decryptFile(f"{filename}.txt.aes", f"{filename}.txt", password, buffersize)
        print("\nFile has been Decrypted!\n")
    except EOFError as err:
        print(err)
else:
    print("Please choose E/e or D/d!")