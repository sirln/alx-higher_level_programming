#!/usr/bin/python3

'''
Singly linked list class module
'''


class Node:
    '''
    Node class
    '''
    def __init__(self, data, next_node=None):
        '''
        private square instance initialization

        Arguments
        ---------
        data : int
            singly linked list data/value
        next_node: Node, optional
            the next node in the singly linked list or None
            (default value is None)

        Raises
        ------
        TypeError
            if argument(data) is not an integer.
            if argument(next_node) is not a Node or None.

        Methods
        -------
        data()
            get/retrive Node
        data(value)
            set node data
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        gets node data

        Returns
        -------
        int
            node data value
        '''
        return (self.__data)

    @data.setter
    def data(self, value):
        '''
        sets node data

        Arguments
        -------
        value : int
            node data value

        Raises
        ------
        TypeError
            if argument(value) is not an integer.
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        gets next node in the singly linked list

        Returns
        -------
        Node
            next node in the linked list
        '''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        '''
        sets next node in the single linked list

        Arguments
        -------
        value : Node
            next node data value

        Raises
        ------
        TypeError
            if argument(value) is not an integer.
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''
    SinglyLinkedList class
    '''

    def __init__(self):
        '''
        Initializing an empty SinglyLinkedList instance
        '''
        self.__head = None

    def sorted_insert(self, value):
        '''
        Insert new Node  into the correct sorted position
        in the list (increasing order)

        Arguments
        ---------
        value : int
            new_node data value
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        '''
        return a string representation of linked list
        '''
        linked_list = ''
        temp = self.__head
        while temp is not None:
            linked_list = linked_list + str(temp.data) + '\n'
            temp = temp.next_node
        return (linked_list.strip())
