# -*- coding: utf-8 -*-
"""
@author: spm
"""

importar  json , solicitudes , urllib3
de  netmiko  import  ConnectHandler
desde  tabular  import  *
de  pprint  import  pprint
desde  ncclient  import  manager
importar  xml . dom . minidom
importar xmltodict


 menú def ():
    imprimir ( "MENÚ - Router CSR1000v)" )
    print ()
    print ( "1. LISTADO INTERFAZ" )
    print ( "2. CREAR INTERFAZ" )
    print ( "3. BORRAR INTERFAZ" )
    print ( "4. LISTAR TABLA DE ENRUTAMIENTO" )
    print ( "5. PETICION MÓDULO YANG" )

    opcion  =  input ( "Por favor, eliga una opción: " )
     opcion de retorno
    
mientras  cierto :
    prueba :
        
        funcion =  menu ()

        si  funcion  ==  "1" :
            sshovercli  =  ConnectHandler ( tipo_dispositivo = 'cisco_ios' , host = '192.168.56.101' , puerto = 22 ,
            nombre de usuario = 'cisco' , contraseña = 'cisco123!' )

            salida =  sshovercli . send_command ( "show ip interface brief" )
            print ( "show ip interface brief: \ n {}" . format ( output ))

        elif  funcion == "2" :
            sshovercli  =  ConnectHandler ( tipo_dispositivo = 'cisco_ios' , host = '192.168.56.101' , puerto = 22 ,
            nombre de usuario = 'cisco' , contraseña = 'cisco123!' )

            interfaz1 = [ 'interfaz loopback1' , 'dirección IP 192.168.1.67 255.255.255.0' , 'descripción loopback sobre ssh' ]
            outputInterfaz1 =  sshovercli . send_config_set ( interfaz1 )
            interfaz2 = [ 'interface loopback2' , 'ip address 10.10.10.10 255.255.255.0' , 'description loopback over ssh' ]
            outputInterfaz2 =  sshovercli . send_config_set ( interfaz2 )

            salida =  sshovercli . send_command ( "show ip interface brief" )
            print ( "show ip interface brief: \ n {}" . format ( output ))
            print ()
            
        elif  funcion  == "3" :
            sshovercli  =  ConnectHandler ( tipo_dispositivo = 'cisco_ios' , host = '192.168.56.101' , puerto = 22 ,
            nombre de usuario = 'cisco' , contraseña = 'cisco123!' )

            interfaz1 = [ 'no int loopback1' ]
            outputInterfaz =  sshovercli . send_config_set ( interfaz1 )
            interfaz2 = [ 'no int loopback2' ]
            outputInterfaz2 =  sshovercli . send_config_set ( interfaz2 )

            salida =  sshovercli . send_command ( "show ip interface brief" )
            print ( "show ip interface brief: \ n {}" . format ( output ))
            print ()

        elif  funcion  ==  "4" :

            solicitudes . paquetes . urllib3 . disable_warnings ()

            api_url  =  "https://192.168.56.101/restconf/data/ief-interfaces:interfaces"

            encabezados = { "Aceptar" : "application / yang-data + json" ,
            "Content-Type" : "application / yang-data + json"
            }

            basic_auth = ( "cisco" , "cisco123!" )

            respuesta  =  solicitudes . get ( api_url , auth = basic_auth , encabezados = encabezados , verificar = Falso )

            respuesta_json  =  respuesta . json ()

            routeList = []
            contador = 0
            para  el  en  response_json [ 'respuesta' ]:
                contador + = 1
                ruta  = [
                    contador ,
                    el [ 'nombre' ],
                    el [ 'habilitado' ],
                    el [ 'ip' ],
                    el [ 'máscara de red' ]
                ]
                routeList . agregar ( ruta )
            tableHeader  = [ "Número" , "Nombre Interfaz" , "Encendido" , "IP" , "Máscara" ]

            imprimir ( tabular ( routeList , tableHeader ))

            "" "sshovercli = ConnectHandler (device_type = 'cisco_ios', host = '192.168.56.101', puerto = 22,
            nombre de usuario = 'cisco', contraseña = 'cisco123!')
            
            salida = sshovercli.send_command ("show brief de interfaz ip")
            print ("show ip interface brief: \ n {}". format (output)) "" "

        elif  funcion  ==  "5" :

            conexión =  gerente.connect ( host = "192.168.56.101" , puerto = 830 , nombre de usuario = "cisco" , contraseña = "cisco123!" , hostkey_verify = False )

            netconf_filter = "" "
            <filtro>
                <interfaces-state xmlns = "urn: ietf: params: xml: ns: yang: ietf-interfaces" />
            </filter>
            "" "
            netconf_reply =  conexi ó n . get ( filtro = netconf_filter )
            
            print ( xml . dom . minidom . parseString ( netconf_reply . xml ). toprettyxml ())
       
        más :
            print ( "Opción no válida, reinicie el programa" )
            break

        continuar  =  input ( "evitar (n) si no quiere continuar, y cualquier tecla para sí:" )

        si  continuar  ==  "n" :
            print ( "El programa se encuentra parado" )
            break
        
        print ()
 
    excepto  KeyboardInterrupt :
        print ( "El programa ha finalizado" )
        break