from SingleLinkedList import SingleLinkedList
from DoubleLinkedList import DoubleLinkedList
#from colorama import *
#init()

inst_dll = DoubleLinkedList()
inst_sll = SingleLinkedList()

class MenuOpciones: 
    def __init__(self):
        self.opciones = []

    def primer_menu(self):
        print('Menú de opciones: ')
        print('a. Listas simplemente enlazadas')
        print('b. Listas doblemente enlazadas')
        print('c. Salir')
        respuesta = input('R/ ')

        return respuesta

    def sub_menu_numero1(self):
        print('Submenú: ')
        print('a. Añadir nodo')
        print('b. Eliminar nodo')
        print('c. Consultar valor contenido en el nodo')
        print('d. Modificar valor de nodo')
        print('e. Invertir toda la lista')
        print('f. validación especial')

        respuesta = input('R/ ')
        return respuesta

    def sub_menu_numero2(self):
        print(' 1. Al inicio')
        print(' 2. Al final')
        print(' 3. En una posición espcífica')

        respuesta = input('R/ ')
        return respuesta

    def sub_menu_numero3(self):
        print(' 1. Punto 5')
        print(' 2. Punto 6')

        respuesta = input('R/ ')
        return respuesta

    def verificar_respuesta_sub_menu1(Self, respuesta):
        if respuesta == 'a':
            return Self.sub_menu_numero2()
        elif respuesta == 'b':
            return Self.sub_menu_numero2()
        elif respuesta == 'f':
            return Self.sub_menu_numero3()
        else: 
            return respuesta

    def verificar_respuesta1(self, respuesta):
        if respuesta == 'a':
            primer_paso = self.sub_menu_numero1()
            self.accion_singlelinkedlist(respuesta)
        elif respuesta == 'b':
            primer_paso = self.sub_menu_numero1()
            self.accion_doublelinkedlist(primer_paso)
        elif respuesta == 'c':
            return None
    
    def accion_doublelinkedlist(self, respuesta):
        if respuesta == 'a':
            segunda_response = self.sub_menu_numero2()
            if segunda_response == '1':
                value = int(input('Ingresa el valor: '))
                inst_dll.push_head_node(value)
            elif segunda_response == '2':
                value = int(input('Ingresa el valor: '))
                inst_dll.push_tail_node(value)
            elif segunda_response == '3':
                index = int(input('Ingresa el indice: '))
                value = int(input('Ingresa el valor: '))
                inst_dll.insert_node(index, value)
        elif respuesta == 'b':
            segunda_response = self.sub_menu_numero2()
            if segunda_response == '1':
                inst_dll.shift_node()
            elif segunda_response == '2':
                inst_dll.pop_node()
            elif segunda_response == '3':
                index = int(input('Ingresa el indice: '))
                value = int(input('Ingresa el valor: '))
                inst_dll.shift_search_node(index)
        elif respuesta == 'c':
            index = int(input('Ingresa el indice: '))
            inst_dll.get_node_value(index)
        elif respuesta == 'd':
            index = int(input('Ingresa el indice: '))
            value = int(input('Ingresa el nuevo valor: '))
            inst_dll.update_node_value(index, value)
        elif respuesta == 'e':
            inst_dll.reverse_nodes()
        elif respuesta == 'f':
            segunda_response = self.sub_menu_numero3()
            if segunda_response == '1':
                print('Continuará')
            elif segunda_response == '2':
                print('Continuará')
        else: 
            print('Respuesta incorrecta')
            self.sub_menu_numero1()

    def accion_singlelinkedlist(self, respuesta):
        if respuesta == 'a':
            segunda_response = self.sub_menu_numero2()
            if segunda_response == '1':
                value = int(input('Ingresa el valor: '))
                inst_sll.push_head_node(value)
            elif segunda_response == '2':
                value = int(input('Ingresa el valor: '))
                inst_sll.push_tail_node(value)
            elif segunda_response == '3':
                index = int(input('Ingresa el indice: '))
                value = int(input('Ingresa el valor: '))
                inst_sll.insert_new_node(index, value)
        elif respuesta == 'b':
            segunda_response = self.sub_menu_numero2()
            if segunda_response == '1':
                inst_sll.shift_head_node()
            elif segunda_response == '2':
                inst_sll.pop_node()
            elif segunda_response == '3':
                index = int(input('Ingresa el indice: '))
                value = int(input('Ingresa el valor: '))
                inst_sll.remove_node(index)
        elif respuesta == 'c':
            index = int(input('Ingresa el indice: '))
            inst_sll.get_node_value(index)
        elif respuesta == 'd':
            index = int(input('Ingresa el indice: '))
            value = int(input('Ingresa el nuevo valor: '))
            inst_sll.update_node_value(index, value)
        elif respuesta == 'e':
            inst_sll.reverse_nodes()
        elif respuesta == 'f':
            segunda_response = self.sub_menu_numero3()
            if segunda_response == '1':
                print('Continuará')
            elif segunda_response == '2':
                print('Continuará')
        else: 
            print('Respuesta incorrecta')
            self.sub_menu_numero1()