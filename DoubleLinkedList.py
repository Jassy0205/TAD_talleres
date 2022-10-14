class DoubleLinkedList: 

    #Se crea la clase nodo
    class Node: 
        #Con este metodo se inicializa la clase nodo
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    #Con este metodo se inicializa la clase DoubleLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #Metodo para insertar un nuevo nodo en una posicion especifica
    def insert_node(self, index, value):
        new_node = self.Node(value)

        if index == 0:
            self.push_head_node(value)
        elif index == self.length:
            self.push_tail_node(value)
        elif index > 0 and index < self.length:
            current_node = self.head

            for i in range(index-1):
                current_node = current_node.next

            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next.previous = new_node
            current_node.next = new_node
            self.length+=1
        else:
            print('index out of range')

    #Con este metodo se agragan nodos al inicio de la lista
    def push_head_node(self, value):
        new_node = self.Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length+=1

    #Con este metodo se agragan nodos al final de la lista
    def push_tail_node(self, value):
        new_node = self.Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    #Metodo para imprimir la lista
    def show_list(self):
        print_sll = []
        current_node = self.head
        count_node = 0

        while count_node !=  self.length: 
            print_sll.append(current_node.value)
            current_node = current_node.next
            count_node+=1

        print(f'lista actual: {print_sll} \n cantidad de nodos {self.length}' )

    #Metodo para eliminar nodos de la lista al incio
    def shift_node(self):
        if self.length == 0:  
            self.head = None
            self.tail = None 
        elif self.head != None: 
            remove_node = self.head 
            self.head = remove_node.next  
            remove_node.next = None 
            self.head.previous = None
        self.length-=1

    #Metodo para eliminar el nodo al final de la lista
    def pop_node(self):
        if self.length == 0:  
            self.head = None
            self.tail = None 
        else: 
            remove_node = self.tail 
            self.tail = remove_node.previous  
            remove_node.previous = None
            self.tail.next = None
        self.length-=1

    #Metodo para eliminar el nodo ubicado en una posición espeficifica (inghresada)
    def shift_search_node(self, index):
        if self.length == 0:
            print('Lista vacía')
        elif index == 1: 
            self.shift_node()
        elif index == self.length+1:
            self.pop_node()
        else:
            count_node = 1
            current_node = self.head

            while current_node is not None:
                if count_node == index:
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                    current_node.next = None
                    current_node.previous = None
                    self.length-=1
                    break
                current_node = current_node.next
                count_node+=1

    #Metodo que retorna el valor del nodo que se encuentra en la posicion ingresada
    def get_node_value(self, index):
        if index > 1 and index < self.length:
            contador = 1
            current_node = self.head

            while contador < self.length and contador < index:
                contador += 1
                current_node = current_node.next

            return current_node.value
        elif index == self.length:
            return self.tail.value
        elif index == 1: 
            return self.head.value
        else: 
            return None

    #Metodo que retorna el nodo que se encuentra en la posicion ingresada
    def get_node(self, index):
        if index > 1 and index < self.length:
            contador = 1
            current_node = self.head

            while contador < self.length and contador < index:
                contador += 1
                current_node = current_node.next

            return current_node
        elif index == self.length:
            return self.tail
        elif index == 1: 
            return self.head
        else: 
            return None

    #Metodo que permite actualizar el valor del nodo en una posicion ingresada
    def update_node_value(self, index, value):
        search_node = self.get_node(index)
        if search_node != None: 
            search_node.value = value #encontró el nodo y se puede actualizar
            return search_node.value
        else: 
            print('No se encontró el nodo a buscar')
            return None

    #Metodo que permite invertir toda la lista
    def reverse_nodes(self):
        if self.length == 0: 
            print('Lista vacía')
        else:
            current_node1 = self.head
            cu = current_node1.next
            current_node1.next = None
            current_node1.previous = cu
            self.tail = current_node1

            while cu is not None:
                cu.previous = cu.next
                cu.next = current_node1
                current_node1 = cu
                cu = cu.previous

            self.head = current_node1