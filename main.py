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
inst_menu.verificar_respuesta1(respuesta)

# ------------------------------ Solo SingleLinkedList -----------------------------

'''
  Author: Jassy
  Date: 30/09/2022
  Description: python
'''

#1. Desde el archivo importamos la clase 
from ast import Try
from interior import SingleLinkedList

inst_sll = SingleLinkedList()

inst_sll.push_node('C')
inst_sll.push_head_node('B')
inst_sll.push_node('D')
inst_sll.push_head_node('A')

inst_sll.show_info_sll()
inst_sll.pop_node()
inst_sll.show_info_sll()
print(inst_sll.get_node_value(4))
print(inst_sll.update_node_value(2, True))
inst_sll.show_info_sll()
inst_sll.remove_node(2)
inst_sll.show_info_sll()
