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
        
        #add evetns handlers
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("register", self.register)
        self.add_event_handler("delete", self.delete)
        self.add_event_handler("message", self.message)
        self.add_event_handler("add_contact", self.add_contact)
        self.add_event_handler("groupchat_message", self.groupchat)
        self.add_event_handler("change_status", self.change_status)
        
    #loggin   
    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.disconnect()
    #register user
    def register(self, iq):
        self.send_presence()
        self.get_roster()
        iq = self.Iq()
        iq['type'] = 'set'
        iq['register']['username'] = self.boundjid.user
        iq['register']['password'] = self.password

        try:
            iq.send()
            print("Nueva Cuenta Creada", self.boundjid,"\n")
        except IqError as e:
            print("Error en Registro ", e,"\n")
            self.disconnect()
        except IqTimeout:
            print("Timeout en el servidor")
            self.disconnect()
        except Exception as e:
            print(e)
            self.disconnect()
            self.send_presence()
        self.get_roster()
    #delete user from server 
    def delete(self, event):
  
        self.send_presence()
        self.get_roster()

        delete = self.Iq()
        delete['type'] = 'set'
        delete['from'] = self.user
        fragment = ET.fromstring("<query xmlns='jabber:iq:register'><remove/></query>")
        delete.append(fragment)

        try:
            delete.send()
            print("Cuenta Borrada")
        except IqError as e:
           
            print("Error", e)
        except IqTimeout:

            print("timeout del server")
        except Exception as e:
     
            print(e)  

        self.disconnect()
    #send msg to a person in server
    def message(self, to,msg):
        print(msg)
        self.send_presence()
        
        self.get_roster()
        self.send_message(mto=to,mbody=msg,mtype='chat')
    #add new contact
    def add_contact(self,user):
        self.send_presence()
        self.get_roster()
        try:
           self.send_presence_subscription(pto=user) 
        except IqTimeout:
            print("Timeout del server")
        self.send_presence()
        self.get_roster()
    async def groupchat(self,room,message):
        self.send_presence()
        self.get_roster()
        self.send_message(mto=room, mbody=message, mtype='groupchat')
        
    def change_status(self,msg):
        self.send_presence()
        self.get_roster()
        self.notification(self.message, 'active')
    
    