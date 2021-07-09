Contents
--------

In this file you will find the following tools coded by // xtc

-> Password-gen.py
-> encrypt-decrypt.py

Basic Summary of tools
----------------------

Password-gen.py

Password-gen.py is a password generator written in python.
It uses letters (uppercase and lowercase), digits and punctuation to generate random password(s) based on user input
The passwords generated are then written to a file
You can choose the amount of characters (16) is recommended

If you choose to use 16 chars an attacker will have a 1 in 26,339,361,174,458,854,765,907,679,379,456 chance (I think) to guess this password since there are 92 possible chars to choose from and 16 chars for a password

----------------------

encrypt-decrypt.py

encrypt-decrypt.py is a tool written in python to encrypt text files in AES-256-CBC encryption.
simply put brute-forcing this encryption with standard hardware would take A REALLY LONG TIME!

----------------------

Instructions for Termux

Download and install termux from google play

commands for termux

$ termux-change-repos

select the grimler mirrors

$ apt upgrade
$ apt install git
$ git clone https://github.com/T3RR0RS-END/passgenerator.git
$ sh setup.sh
$ termux-setup-storage
$ python3 password-gen.py
$ python3 encrypt-decrypt.py

commands for windows

open up cmd

> SETUP.SH WILL NOT WORK ON WINDOWS
> pip3 install pyaescrypt
> python3 password-gen.py
> python3 encrypt-decrypt.py

commands for linux

open terminal

$ ./setup.sh
$ python3 password-gen.py
$ python3 encrypt-decrypt.py
