#!/usr/bin/python3
""" Defines the class Node"""


class Node:
    """
    defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        instatiate the instantiate a node
        Args:
            Data - value to insert into node
            next_node - pointer to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve the data """

        return self.__data

    @data.setter
    def data(self, value):
        """Set data attribute """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ Retrieve the next_node attribute"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set the next node """

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list """

    def __init__(self):
        """ Initializing the singly linked list """

        self.head = None

    def __str__(self):
        """make list printable"""

        printlist = ""
        index = self.head
        while index:
            printlist += str(index.data) + "\n"
            index = index.next_node
        return printlist[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """

        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        index = self.head
        while index.next_node and index.next_node.data < value:
            index = index.next_node
        if index.next_node:
            new.next_node = index.next_node
        index.next_node = new
