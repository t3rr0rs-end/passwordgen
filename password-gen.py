
import os, random, string, time

x = 1                                                                                   # set x var = 1 for counting
wOrL = input("Are you using this tool on windows or linux?(w/l): ").upper()
if wOrL == "L":
    os.system('clear')                                                                      # clear terminal
if wOrL == "W":
    os.system('cls')
else:
    print("Please choose w or l")

print(" ")                                                                              # newline

print("             + --------------------------- +")                                   
time.sleep(0.05)
print("             |     Password Generator!     |")           
time.sleep(0.05)
print("             + --------------------------- +")
time.sleep(0.05)
print(" ")

charsLen = int(input("How many chars in generated passwords?: "))                       # asks for desired length of password(s)
howMany = int(input("How many passwords would you like to generate?: "))                # asks for amount of passwords to generate
chars = string.ascii_letters + string.digits + string.punctuation                       # sets types of chars to be generated
print("")

filename = input("Name of the file you want to create for passwords (Do not use extension): ")
file = open(f"{filename}.txt", "w")                                                       # creates file to be opened

for i in range(howMany):                                                                # for loop
    password = ''.join(random.sample(chars, charsLen))                                  # set password = random chars for len specified
    file.write(f"Password {x} Generated: {password}\n")                                 # writes password number and password to file
    x += 1                                                                              # increment counter by one

file.close()                                                                            # close file after writing passwords

print("Password file has been generated!\n")