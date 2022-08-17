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
            user = input("User: ")
            #psd = getpass("Password : ")
            psd = input("Password : ")

            client = Client(user, psd)
            client.register_plugin('xep_0030') 
            client.register_plugin('xep_0199') 

            # Connect to the XMPP server and start processing XMPP stanzas.
            client.connect()
            client.process(forever=False)
        elif opc == '2':
            user = input("User: ")
            #psd = getpass("Password : ")
            psd = input("Password : ")

            client = Client(user, psd)
            client.register_plugin('xep_0030') 
            client.register_plugin('xep_0004')
            client.register_plugin('xep_0077')
            client.register_plugin('xep_0199')
            client.register_plugin('xep_0066')
            client["xep_0077"].force_registration = True

            # Connect to the XMPP server and start processing XMPP stanzas.
            client.connect()
            client.process(forever=False)
            
            
        
if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()