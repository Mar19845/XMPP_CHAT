from client import *
from getpass import getpass
import logging

def main():
    while True:
        print("********************* Welcome *********************")
        print()
        print("1. Loggin") # done
        print("2. Sign in") # done
        print("3. get out\n") # done
        opc = input("-> ")
        if opc == '3':
            exit()
        elif opc == '1':
            Client.loggin()
        elif opc == '2':
            Client.signin()
            
            
        
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()