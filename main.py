from client import *


'''
client = Client('prueba2510@alumchat.fun','prueba2510')


client.message('mar19845@alumchat.fun','perra')
client.register_plugin('xep_0030') # Service Discovery
client.register_plugin('xep_0199') # client Ping
client.register_plugin('xep_0045') # Mulit-User Chat (MUC)
client.register_plugin('xep_0096') # Jabber Search

client.connect()
client.process(forever=False)


'''


        
####################################################################

#logged user logic
def logged_user(user):
    conditional = True
    while conditional:
        print("-----------------------------------------------")
        print("Presione 1 para mostrar contactos")
        print("Presione 2 para agregar contactos")
        print("Presione 3 para mostrar detalles de un contacto")
        print("Presione 4 para entrar a un chat 1 a 1")
        print("Presione 5 para entrar a un chat grupal")
        print("Presione 6 para cambiar mensaje de presencia")
        print("Presione 7 para enviar y recibir archivos")
        print("Presione 8 para notificaciones")
        print("Presione 9 para eliminar cuenta")
        print("Presione 10 para cerrar sesion")
        print("-----------------------------------------------")
        opc2  = input("")
        if opc2 == '10':
            #user.disconnect()
            #user.process(forever=False)
            conditional = False
            break
        elif opc2 == '9':
            user.delete()
            user.register_plugin('xep_0030') # Service Discovery
            user.register_plugin('xep_0004') # Data forms
            user.register_plugin('xep_0066') # Out-of-band Data
            user.register_plugin('xep_0077') # In-band Registration
            #user.connect()
            #user.process()
        elif opc2 == '2':
            
            to = input('Ingrese el contacto: ')
            user.add_contact(to)
            user.register_plugin('xep_0030') # Service Discovery
            user.register_plugin('xep_0199') # XMPP Ping
            user.register_plugin('xep_0045') # Mulit-User Chat (MUC)
            user.register_plugin('xep_0096') # Jabber Search
        elif opc2 == '3':
            to = input('Ingrese el contacto: ')
            #user.get_contact_detail(user=to)
            #user.register_plugin('xep_0030') # Service Discovery
            #user.register_plugin('xep_0199') # XMPP Ping
            #user.register_plugin('xep_0045') # Mulit-User Chat (MUC)
            #user.register_plugin('xep_0096') # Jabber Search
            #user.process(forever=False)
        elif opc2 == '4':
            to = input('Ingrese el contacto: ')
            cond_msg = True
            while cond_msg:
                try:
                    msg = input()
                    user.message(to,msg)
                    user.register_plugin('xep_0030') # Service Discovery
                    user.register_plugin('xep_0199') # client Ping
                    user.register_plugin('xep_0045') # Mulit-User Chat (MUC)
                    user.register_plugin('xep_0096') # Jabber Search

                    user.connect()
                    user.process(forever=False)
                except KeyboardInterrupt as e:
                    print('Conversacion finalizada')
                    cond_msg = False
                    #user.disconnect()
        elif opc2 == '6':
            msg = input('Ingrese el nuevo status: ')
            user.change_status(msg)
            user.register_plugin('xep_0030') # Service Discovery
            user.register_plugin('xep_0199') # XMPP Ping
            user.register_plugin('xep_0045') # Mulit-User Chat (MUC)
            user.register_plugin('xep_0096') # Jabber Search
                    
                    
                    
#####################################################################################################
conditional = True
while conditional:
    opc = ''
    print("PRESIONE 1 PARA INGRESAR EN EL SERVIDOR DE ALUMCHAT")
    print("PRESIONE 2 PARA REGISTRARSE EN EL SERVIDOR DE ALUMCHAT")
    print("PRESIONE 3 PARA SALIR")
    opc = input("-> ")
    if opc == '3':
        print('Gracias por usar el chat vuelva pronto\n')
        conditional = False
    if opc == '1':
        user=input('Ingrese su username: ')
        psw=input('Ingrese su password: ')
        #psw = getpass("Ingrese contraseña: ")
        client = Client(user,psw)
        logged_user(client)
    if opc == '2':
        user=input('Ingrese su username: ')
        psw=input('Ingrese su password: ')
        client = Client(user,psw)
        client.register()
        client.register_plugin('xep_0030') # Service Discovery
        client.register_plugin('xep_0004') # Data Forms
        client.register_plugin('xep_0066') # Band Data
        client.register_plugin('xep_0077') # Band Registration
        client.connect()
        client.process(forever=False)
        print("Registro Completado\n")