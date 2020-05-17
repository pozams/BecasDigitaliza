# -*- coding: utf-8 -*-
"""
@author: spm
@descripción: conexion a controlado APIC EM de CISCO
"""

importar  os
 solicitudes de importación
import  json , time , re , urllib3
desde  tabular  import  *
de  my_apic_em_functions  import  *

def  menuFunciones ():
    print ( "" "
          MENÚ (APIC-EM)
          
          Elije una opción:
           1.- TICKET
           2.- IMPRIMIR HOST
           3.- IMPRIMIR DISPOSITIVOS DE RED
           4.- INVENTARIO
           5.- DISPOSITIVOS Y HOST
           6.- SALIR "" " )


def  ticket ():
    api_url  =  "https://sandboxapicem.cisco.com/api/v1/ticket"
    encabezados  = {
        "content-type" : "aplicación / json"
    }
    body_json  = {
        "username" : "devnetuser" ,
        "contraseña" : "Cisco123!"
    }
    
    resp = solicitudes . post ( api_url , json . dumps ( body_json ), encabezados = encabezados , verificar = Falso )
    
    print ( "Estado de solicitud de ticket:" , resp . status_code )
    respuesta_json  =  resp . json ()
    serviceTicket  =  response_json [ "respuesta" ] [ "serviceTicket" ]
    print ( "El ticket obtenido es:" , token )
     token de retorno

def   print_host ():
    url = "https://sandboxapicem.cisco.com/api/v1/host"
    ticket  =  get_ticket ()
    encabezados = {
        
        "Content_type" : "aplicación / json" ,
       
        "X-Auth-Token" : ticket_json
    }

def  print_device ():
    
    urllib3 . disable_warnings ( urllib3 . excepciones . InsecureRequestWarning )
    respuesta  =  solicitudes . get ( url , encabezados = encabezado , verificar  =  falso )
    print ( 100 * "·" , " \ n Solicitud de host de estado:" , respuesta . status_code , " \ n " , 100 * "·" )
    
    si  respuesta . status_code  ! =  200 :
        print ( "Existe un error en la solicitud:" , respuesta . status_code )
        aumento  de excepción ( "Código de estado no es igual a 200. texto de respuesta:"  +  Respuesta . texto )

    respuesta_json  =  respuesta . json ()

    hostList  = []
    i  =  0
    para el  elemento  en  response_json [ "respuesta" ]:
        
        i  + =  1

        hostX  = [ i ,
            item [ "hostIp" ],
            elemento [ "hostMac" ],
            item [ "hostType" ],
            item [ "connectedNetworkDeviceIpAddress" ],
            elemento [ "id" ]]
        hostList . agregar ( hostX )
    table_header  = [ "Numero" , "IP" , "MAC" , "Tipo de host" , "IP dispositivos conectados" , "ID" ]    
    imprimir ( tabular ( ListaCaliente , table_header ))

def  get_Host ( url , ticket ):    
    get_Network_Devices_url = url + "host"    
    encabezados = {
        "Content-type" : "application / json" ,
        "X-Auth-Token" : ticket_json ,
    }
    resp = solicitudes . get ( get_Network_Devices_url , encabezados = encabezados , verificar = Falso )     
    si  resp . status_code  ==  200 :
        resp_json = resp . json ()        
        Listado_equipos_red = []
        i = 0
        para  equipo  en  resp_json [ "respuesta" ]:
            i + = 1
            Disp = [
                i ,
                equipo [ "hostType" ],                
                equipo [ "hostMac" ],
                equipo [ "hostIp" ]
                ]

def  get_device_inventory ():
    device_endpoint  =  "dispositivo de red"

    prueba :
        ticket  =  get_ticket ()
        si  ticket  ==  - 1 :
            raise  Exception ( "Hubo un error al obtener el ServiceTicket" )
        encabezados  = {
            "content-type" : "aplicación / json" ,
            "X-Auth-Token" : ticket_json
        }
        resp  =  solicitudes . get ( api_url  +  device_endpoint , encabezados  =  encabezados , verificar  =  Falso )
        si  resp . status_code  ! =  200 :
            aumento  de excepción ( "El código de estado no es de texto 200. Respuesta:"  +  resp . texto )
        resp_json  =  resp . json ()
        i  =  0
        lista_dispositivo  = []
        para  dispositivo  en  resp_json [ "respuesta" ]:
            i  + =  1
            lista_dispositivo . append ([ i , dispositivo [ "familia" ], dispositivo [ "managementIpAddress" ]])
        volver  lista_dispositivo
    excepto  Excepción  como  e :
        print ( e . args [ 0 ])
    
def  get_hosts_and_devices ():
    lista_dispositivos  =  get_host_inventory ()
    lista_dispositivos  + =  get_device_inventory ()
    i  =  0
    para el  elemento  en  lista_dispositivos :
        i  + =  1
        elemento [ 0 ] =  i
    volver  lista_dispositivos

    mientras  cierto :
        

        menu :
            opcion  =  int ( input ( "Selecciona una de las opciones del menú:" ))
            si  opcion  ==  1 :
                print ( "Selecciono: {}" . format ( obtener_ticket ))
                get_ticket ()
            elif  opcion  ==  2 :
                print ( "Selecciono: {}" . format ( obtener_lista_host ))
                get_hosts_list ()
            elif  opcion  ==  3 :
                print ( "Selecciono: {}" . format ( obtener_lista_dispositivos_red ))
                get_network_devices_list ()
            elif  opcion  ==  4 :
                print ( "Selecciono: {}" . format ( obtener_inventario_dispositivos ))
                get_config_run ()
            elif  opcion  ==  5 :
                print ( "Selecciono: {}" . format ( obtener_dispositivos_y_host ))
                get_path_trace ()
            elif  opcion  ==  6 :
                print ( "Selecciono: {}" . format ( finalizar ))
                salida ()
            más :
                predeterminado ()
            pausa  =  input ( "Tecla intro para continuar" )    
        excepto  ValueError :
            predeterminado ()
            print ( "En caso de error pulsa 0 para salir." )

if  __name__  ==  "__main__" :
    main ()