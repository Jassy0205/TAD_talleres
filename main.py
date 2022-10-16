'''
    Author: Jassy
    Date: 14/10/2022
    Description: python
'''

#1. Desde el archivo importamos la clase 
from ast import Try
from MenuOpciones import MenuOpciones

inst_menu = MenuOpciones()

respuesta = inst_menu.primer_menu()
while True:
    seguir_adelante = inst_menu.verificar_respuesta1(respuesta)
    seguir_adelante.split(sep=',')
    print(seguir_adelante)
    break 

