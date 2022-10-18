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
        else: 
            print('Intenta de nuevo')
            return 'False'
    
    #Con este metodo se llaman a las funciones de la DoubleLinkedList dependiendo de la que se haya elegido en el sub_menu_numero1
    def accion_doublelinkedlist(self, respuesta):
        if respuesta == 'a':

            print(Fore.MAGENTA + 'a. Añadir nodo')
            segunda_response = self.sub_menu_numero2()

            add_node_list = self.añadir_double_list(segunda_response)
            if add_node_list == True:
                return True

        elif respuesta == 'b':
            self.eliminar_double_list()

        elif respuesta == 'c':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)
            value = inst_dll.get_node_value(index)
            print(Fore.YELLOW + f'El valor del nodo solicitado es: {value}')
            self.verificar_show_list('doble')

        elif respuesta == 'd':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)
            value = input('Ingresa el nuevo valor: ')
            value = self.verificar_numero(value)

            print(Fore.YELLOW)
            inst_dll.update_node_value(index, value)
            inst_dll.show_list()

        elif respuesta == 'e':
            print(Fore.YELLOW)
            inst_dll.reverse_nodes()
            self.verificar_show_list('doble')

        elif respuesta == 'f':
            print(Fore.MAGENTA + 'f. Validación especial')
            print(Fore.YELLOW)
            caso_especial = self.validacion_especial_double_list()
            if caso_especial == True:
                return True

        elif respuesta == 'g':
            return False
        else: 
            print(Fore.RED + 'Respuesta incorrecta. Intentalo de nuevo')
            return True
        
        return self.verificar_continuidad('doble')

    #Con este metodo se llaman a las funciones de la SingleLinkedList dependiendo de la que se haya elegido en el sub_menu_numero1
    def accion_singlelinkedlist(self, respuesta):
        if respuesta == 'a':

            print(Fore.MAGENTA + 'a. Añadir nodo')
            segunda_response = self.sub_menu_numero2()

            add_node_list = self.añadir_single_list(segunda_response)
            if add_node_list == True:
                return True

        elif respuesta == 'b':
            self.eliminar_single_list()

        elif respuesta == 'c':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)

            value = inst_sll.get_node_value(index)
            print(Fore.YELLOW + f'El valor del nodo solicitado es: {value}')
            self.verificar_show_list('simple')

        elif respuesta == 'd':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)
            value = input('Ingresa el nuevo valor: ')
            print(Fore.YELLOW)
            value = self.verificar_numero(value)

            inst_sll.update_node_value(index, value)
            inst_sll.show_info_sll()

        elif respuesta == 'e':
            print(Fore.YELLOW)
            inst_sll.reverse_nodes()
            inst_sll.show_info_sll()

        elif respuesta == 'f':
            print(Fore.MAGENTA + 'f. Validación especial')
            print(Fore.YELLOW)
            inst_sll.validar_reverse_raiz_cuadrada()
            inst_sll.show_info_sll()

        elif respuesta == 'g':
            return False
        else: 
            print(Fore.RED + 'Respuesta incorrecta')
            return True

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
            self.verificar_show_list(tipo)

    #Con el siguiente metodo se pregunta al usuario si desea continuar modificando la lista actual o si desea parar
    def verificar_continuidad(self, tipo):
        repeticion_ciclo = input(Fore.GREEN  + f'Desea continuar haciendo algo más en la lista {tipo}? Responda con 1 para si y con 0 para no: ')
        if repeticion_ciclo == '1':
            return True
        elif repeticion_ciclo == '0': 
            return False
        else: 
            print(Fore.RED + f'Valor invalido. Intentalo de nuevo')
            return self.verificar_continuidad(tipo)

    #Con el siguiente metodo se valida que el dato ingresado sea un valor de tipo numerico
    def verificar_numero(self, value):
        try: 
            numero_yea = int(value)
            return numero_yea
        except: 
            print(Fore.RED + f'El valor no es numerico. Intentalo de nuevo')
            numero_try = input(Fore.GREEN + 'Ingresa el valor: ')
            return self.verificar_numero(numero_try)
    
    #En este metodo se ingresa un valor al inicio, final o en una posición especifica según el valor 
    #que se ingresa como "second_response" utilizando las funciones ya hechas en la clase DoubleLinkedList
    def añadir_double_list(self, second_response):
        if second_response != '1' and second_response != '2' and second_response != '3' and second_response != '4':
            print(Fore.RED + f'El valor es invalido\n')
            return True  
        else:
            value = input('Ingresa el valor del nodo: ')
            value = self.verificar_numero(value)
            existe_node = inst_dll.verificar_existencia(value)

            if  existe_node == True:
                print(Fore.RED + 'El nodo ya existe en la lista')
            else:
                if second_response == '1':
                    inst_dll.push_head_node(value)
                    self.verificar_show_list('doble')
                elif second_response == '2':
                    inst_dll.push_tail_node(value)
                    self.verificar_show_list('doble')
                elif second_response == '3':
                    index = input('Ingresa el indice: ')
                    index = self.verificar_numero(index)
                    inst_dll.insert_node(index, value)
                    self.verificar_show_list('doble')
                elif second_response == '4':
                    return True 

    #En este metodo se elimina un valor al inicio, final o en una posición especifica 
    # esto utilizando las funciones ya hechas en la clase DoubleLinkedList
    def eliminar_double_list(self):
        print(Fore.MAGENTA + 'b. Eliminar nodo')
        segunda_response = self.sub_menu_numero2()
        if segunda_response == '1':
            inst_dll.shift_node()
        elif segunda_response == '2':
            inst_dll.pop_node()
        elif segunda_response == '3':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)
            inst_dll.shift_search_node(index)
        self.verificar_show_list('doble')

    #En este metodo se ingresa un valor al inicio, final o en una posición especifica según el valor 
    #que se ingresa como "segunda_response" utilizando las funciones ya hechas en la clase SingleLinkedList
    def añadir_single_list(self, segunda_response):
        if segunda_response != '1' and segunda_response != '2' and segunda_response != '3' and segunda_response != '4':
            print(Fore.RED + f'El valor es invalido\n')
            return True  
        else:
            value = input('Ingresa el valor: ')
            value = self.verificar_numero(value)
            existe_node = inst_dll.verificar_existencia(value)

            if  existe_node == True:
                print(Fore.RED + 'El nodo ya existe en la lista')
            else:
                if segunda_response == '1':
                    inst_sll.push_head_node(value)
                    self.verificar_show_list('simple')
                elif segunda_response == '2':
                    inst_sll.push_node(value)
                    self.verificar_show_list('simple')
                elif segunda_response == '3':
                    index = input('Ingresa el indice: ')
                    index = self.verificar_numero(index)
                    inst_sll.insert_new_node(index, value)
                    self.verificar_show_list('simple')
                elif segunda_response == '4':
                    return True

    #En este metodo se elimina un valor al inicio, final o en una posición especifica 
    # esto utilizando las funciones ya hechas en la clase SingleLinkedList
    def eliminar_single_list(self):
        print(Fore.MAGENTA + 'b. Eliminar nodo')
        segunda_response = self.sub_menu_numero2()
        if segunda_response == '1':
            inst_sll.shift_head_node()
        elif segunda_response == '2':
            inst_sll.pop_node()
        elif segunda_response == '3':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)
            inst_sll.remove_node(index)
        self.verificar_show_list('simple')
            

    #En este metodo se hacen las dos validaciones epeciales posibles para
    # la DobleLinkedList, esto utilizando las funciones desarrolladas en dicha clase
    def validacion_especial_double_list(self):
        segunda_response = self.sub_menu_numero3()
        if segunda_response == '1':
            index = input('Ingresa el indice: ')
            index = self.verificar_numero(index)
            inst_dll.update_node_value_cuadrado(index)
            inst_dll.show_list()
        elif segunda_response == '2':
            inst_dll.validar_reverse_raiz_cuadrada()
            inst_dll.show_list
        elif segunda_response == '3':
            return True



