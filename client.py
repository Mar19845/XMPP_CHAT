import sys
import aiodns
import asyncio
import logging
from getpass import getpass
from argparse import ArgumentParser
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream.stanzabase import ET, ElementBase 
import slixmpp
import base64, time
import threading

if sys.platform == 'win32' and sys.version_info >= (3, 8):
     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logging.basicConfig(level=logging.DEBUG, format=None)   
     
class Client(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)
        
        self.user = jid
        self.presences = threading.Event()
        
        self.add_event_handler("session_start", self.start)
        
    async def start(self, event):
        
        self.send_presence()
        #send gruop msg
        def send_groupchat_msg():
            self.register_plugin('xep_0030')
            self.register_plugin('xep_0045')
            self.register_plugin('xep_0199')
            room = input('room -> ')
            nickname = input('nickname -> ')
            self.plugin['xep_0045'].join_muc(room, nickname)
            cond = True
            while cond:
                try:
                    msg = input('msg -> ')
                    self.send_message(mto=self.room, mbody=msg, mtype='groupchat')
                    self.send_presence()
                except KeyboardInterrupt as e:
                    print('Conversacion finalizada')
                    cond = False
        #send private msg to a user
        def send_private_msg():
            self.send_presence()
            user = input('To -> ')
            msg = input('msg -> ')
            self.send_message(mto= user, mbody= msg, mtype='chat')
            print('msg send \n')
            self.send_presence()
        #logot out func  
        def logout():
            self.disconnect()
            print("session ended \n")
            
        #add new user func
        def add_user():
            user = input('user -> ')
            self.send_presence_subscription(pto=user)
            
        #delete account from server func
        def delete_account():
            self.register_plugin('xep_0030') 
            self.register_plugin('xep_0004')
            self.register_plugin('xep_0077')
            self.register_plugin('xep_0199')
            self.register_plugin('xep_0066')

            # delete logged account
            delete = self.Iq()
            delete['type'] = 'set'
            delete['from'] = self.boundjid.user
            delete['register']['remove'] = True
            delete.send()
            
            self.disconnect()
            print('Account successfully deleted\n')
        
        #show friends info func
        def show_users():
            self.send_presence()
            self.get_roster()
            print('================================================\n')
            contacts = self.client_roster.groups()
            for contact in contacts:
                for jid in contacts[contact]:
                    user = self.client_roster[jid]['name']
                    
                    print('-----------------------------')

                    user_connected = self.client_roster.presence(jid)
                    for res, pres in user_connected.items():
                        print('Usuario: ', jid)
                        show = 'conectado'
                        if pres['show']:
                            show = pres['show']
                        print(show)
                        if pres['status']:
                            print(' Status -> ', pres['status'])
                        print('-----------------------------')

        #change status on server            
        def change_status():
            self.send_presence()
            self.get_roster()
            status = input("status -> ")
            info = input("your info -> ")
            self.send_presence(pshow=info, pstatus=status)
            print('Status changed successfully\n')
        
        def user_detail():
            self.send_presence()
            self.get_roster()
            user = input("user -> ")
            contacts = self.client_roster.presence(user)
            for res, pres in contacts.items():
                show = 'chat'
                if pres['show']:
                    show = pres['show']
                print(" INFO:")
                print(show)
                print('Status -> ', pres['status'])
            
        
        cond = True
        while cond:
            print("1. Send a msg to a user") # done
            print("2. show status and details of all friends") # done
            print("3. add new user") # done
            print("4. show detail and status of a user") # done
            print("5. groupchat")
            print("6. define status") # done
            print("7. delete account") # done
            print("8. loggout") # done
            opc = input('-> ')
            
            if opc == '8':
                logout()
                cond = False
            elif opc == '1':
                send_private_msg()
            elif opc == '2':
                show_users()
            elif opc == '3':
                add_user()
            elif opc == '4':
                user_detail()
            elif opc == '5':
                send_groupchat_msg()
            elif opc == '6':
                change_status()
            elif opc == '7':
                delete_account()
                cond = False
            self.send_presence()
            await self.get_roster()
                
    
    def loggin():
        

        user = input("User: ")
        #psd = getpass("Password : ")
        psd = input("Password : ")

        client = Client(user, psd)
        client.register_plugin('xep_0030') 
        client.register_plugin('xep_0199') 

        # Connect to the XMPP server and start processing XMPP stanzas.
        client.connect()
        client.process(forever=False)
        
    def signin():
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