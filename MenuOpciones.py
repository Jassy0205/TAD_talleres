from SingleLinkedList import SingleLinkedList
from DoubleLinkedList import DoubleLinkedList
from colorama import *
init()

inst_dll = DoubleLinkedList()
inst_sll = SingleLinkedList()

#Creamos la clase Menú de Opciones
class MenuOpciones: 
    #Con este metodo se inicializa la clase menu
    def __init__(self):
        self.opciones = []

    #Con este metodo se despliega el menu principal, donde se dan a conocer las opciones de listas que hay 
    # y devuelve la opción que se haya escogido
    def primer_menu(self):
        print(Fore.RED + 'Menú de opciones: ')
        print(Fore.BLUE + 'a. Listas simplemente enlazadas')
        print('b. Listas doblemente enlazadas')
        print('c. Salir')

        respuesta = input('R/ ')
        print("\n")

        return respuesta

    #Con este metodo se despliega el primer sub-menú, donde se elige lo que se quiera 
    # hacer con el tipo de lista que se escogió antes, y devuelve la opción elegida
    def sub_menu_numero1(self):
        print(Fore.BLUE + 'Submenú:  ')
        print(Fore.MAGENTA + 'a. Añadir nodo')
        print('b. Eliminar nodo')
        print('c. Consultar valor contenido en el nodo')
        print('d. Modificar valor de nodo')
        print('e. Invertir toda la lista')
        print('f. Validación especial')
        print('g. Atrás')

        respuesta = input('R/ ')
        print("\n")

        return respuesta

    #Con este metodo se despliega el segundo sub-menú, opciones ligadas a las respuestas a o b del submenú numero 1
    #Retorna la opción que haya sido escogida
    def sub_menu_numero2(self):
        print(Fore.CYAN + ' 1. Al inicio')
        print(' 2. Al final')
        print(' 3. En una posición espcífica')
        print(' 4. Atrás')

        respuesta = input('R/ ')
        print("\n")

        return respuesta

    #Con este metodo se despliega el tercer sub-menú, opciones ligadas a las respuesta f del submenú numero 1
    #Retorna la opción que haya sido escogida
    def sub_menu_numero3(self):
        print(' 1. Punto 5')
        print(' 2. Punto 6')
        print(' 3. Atrás')

        respuesta = input('R/ ')
        print("\n")
        
        return respuesta

    #Con este metodo se verifica la respuesta enviada después del despliegue del menú principal, para recibirla respuesta del sub_menu_numero1
    #y si es a o b, enviandola luego a un metodo que actúa dependiendo del tipo de lista en la que se quiere trabajar 
    #si es c, se cierra el proceso y retorna un None
    def verificar_respuesta1(self, respuesta):
        if respuesta == 'a':
            primer_paso = self.sub_menu_numero1()
            seguimiento_menu = self.accion_singlelinkedlist(primer_paso)
            return (str(seguimiento_menu) + ',a')
        elif respuesta == 'b':
            primer_paso = self.sub_menu_numero1()
            seguimiento_menu = self.accion_doublelinkedlist(primer_paso)
            return (str(seguimiento_menu) + ',b')
        elif respuesta == 'c':
            return 'salir'
    
    #Con este metodo se llaman a las funciones de la DoubleLinkedList dependiendo de la que se haya elegido en el sub_menu_numero1
    def accion_doublelinkedlist(self, respuesta):
        if respuesta == 'a':

            print(Fore.MAGENTA + 'a. Añadir nodo')
            segunda_response = self.sub_menu_numero2()

            value = int(input('Ingresa el valor del nodo: '))
            existe_node = inst_dll.verificar_existencia(value)

            if  existe_node == True:
                print(Fore.RED + 'El nodo ya existe en la lista')
            else:
                if segunda_response == '1':
                    inst_dll.push_head_node(value)
                elif segunda_response == '2':
                    inst_dll.push_tail_node(value)
                elif segunda_response == '3':
                    index = int(input('Ingresa el indice: '))
                    inst_dll.insert_node(index, value)
                self.verificar_show_list('doble')

        elif respuesta == 'b':
            print(Fore.MAGENTA + 'b. Eliminar nodo')
            segunda_response = self.sub_menu_numero2()
            if segunda_response == '1':
                inst_dll.shift_node()
            elif segunda_response == '2':
                inst_dll.pop_node()
            elif segunda_response == '3':
                index = int(input('Ingresa el indice: '))
                inst_dll.shift_search_node(index)
            self.verificar_show_list('doble')

        elif respuesta == 'c':
            index = int(input('Ingresa el indice: '))
            value = inst_dll.get_node_value(index)
            print(Fore.YELLOW + f'El valor del nodo solicitado es: {value}')
            self.verificar_show_list('doble')

        elif respuesta == 'd':
            index = int(input('Ingresa el indice: '))
            value = int(input('Ingresa el nuevo valor: '))
            inst_dll.update_node_value(index, value)
            inst_dll.show_list()

        elif respuesta == 'e':
            inst_dll.reverse_nodes()
            self.verificar_show_list('doble')
        elif respuesta == 'f':
            segunda_response = self.sub_menu_numero3()
            if segunda_response == '1':
                print('Continuará')
            elif segunda_response == '2':
                inst_dll.validar_reverse_raiz_cuadrada()
                inst_dll.show_list()
        elif respuesta == 'g':
            return False
        else: 
            print('Respuesta incorrecta')
            self.sub_menu_numero1()
        
        return self.verificar_continuidad('doble')

    #Con este metodo se llaman a las funciones de la SingleLinkedList dependiendo de la que se haya elegido en el sub_menu_numero1
    def accion_singlelinkedlist(self, respuesta):
        if respuesta == 'a':

            print(Fore.MAGENTA + 'a. Añadir nodo')
            segunda_response = self.sub_menu_numero2()
            
            value = int(input('Ingresa el valor: '))
            existe_node = inst_dll.verificar_existencia(value)

            if  existe_node == True:
                print(Fore.RED + 'El nodo ya existe en la lista')
            else:
                if segunda_response == '1':
                    inst_sll.push_head_node(value)
                elif segunda_response == '2':
                    inst_sll.push_node(value)
                elif segunda_response == '3':
                    index = int(input('Ingresa el indice: '))
                    inst_sll.insert_new_node(index, value)
                self.verificar_show_list('simple')

        elif respuesta == 'b':
            print(Fore.MAGENTA + 'b. Eliminar nodo')
            segunda_response = self.sub_menu_numero2()
            if segunda_response == '1':
                inst_sll.shift_head_node()
            elif segunda_response == '2':
                inst_sll.pop_node()
            elif segunda_response == '3':
                index = int(input('Ingresa el indice: '))
                inst_sll.remove_node(index)
            self.verificar_show_list('simple')

        elif respuesta == 'c':
            index = int(input('Ingresa el indice: '))
            value = inst_sll.get_node_value(index)
            print(Fore.YELLOW + f'El valor del nodo solicitado es: {value}')
            self.verificar_show_list('simple')
        elif respuesta == 'd':
            index = int(input('Ingresa el indice: '))
            value = int(input('Ingresa el nuevo valor: '))
            inst_sll.update_node_value(index, value)
            inst_sll.show_info_sll()
        elif respuesta == 'e':
            inst_sll.reverse_nodes()
            inst_sll.show_info_sll()
        elif respuesta == 'f':
            inst_sll.validar_reverse_raiz_cuadrada()
            inst_sll.show_info_sll()
        elif respuesta == 'g':
            return False
        else: 
            print('Respuesta incorrecta')
            self.sub_menu_numero1()

        return self.verificar_continuidad('simple')

    #Con el siguiente metodo se pregunta al usuario si desea ver la lista una vez que realice la acción que desee
    def verificar_show_list(self, tipo):
        show_list_consola = input(Fore.RED + 'Desea ver la lista? Responda con 1 para si y con 0 para no: ')
        print(Fore.YELLOW)

        if show_list_consola == '1':
            if tipo == 'simple':
                inst_sll.show_info_sll()
            else: 
                inst_dll.show_list()
        elif show_list_consola != '0': 
            print('Intentalo de nuevo')
            self.verificar_show_list(self, tipo)

    #Con el siguiente metodo se pregunta al usuario si desea continuar modificando la lista actual o si desea parar
    def verificar_continuidad(self, tipo):
        repeticion_ciclo = input(Fore.RED + f'Desea continuar haciendo algo más en la lista {tipo}? Responda con 1 para si y con 0 para no: ')
        if repeticion_ciclo == '1':
            return True
        elif repeticion_ciclo == '0': 
            return False
        else: 
            return None

