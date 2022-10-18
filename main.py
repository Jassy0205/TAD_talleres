'''
    Author: Jassy
    Date: 14/10/2022
    Description: python
'''

#1. Desde el archivo importamos la clase 
from colorama import *
init()
from ast import Try
from re import A
from MenuOpciones import MenuOpciones

inst_menu = MenuOpciones()

respuesta = inst_menu.primer_menu()
seguir_adelante = inst_menu.verificar_respuesta1(respuesta)
seguir_adelante = seguir_adelante.split(',')

while True:  
    if  seguir_adelante[0] == 'salir':
        print(Fore.GREEN + 'Ten un buen día!')
        break
    elif seguir_adelante[0] == 'True': 
        seguir_adelante = inst_menu.verificar_respuesta1(seguir_adelante[1])
        seguir_adelante = seguir_adelante.split(sep=',')
    elif seguir_adelante[0] == 'False':
        respuesta = inst_menu.primer_menu()
        seguir_adelante = inst_menu.verificar_respuesta1(respuesta)
        seguir_adelante = seguir_adelante.split(sep=',')


