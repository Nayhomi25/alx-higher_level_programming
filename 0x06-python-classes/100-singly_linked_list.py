#!/usr/bin/python3
""" Singly linked lists """


class Node:
    """ Private instance attribute: data and next_node """

    def __init__(self, data, next_node=None):
        """ initializes attributes data and next_node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """ setter for data """
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter for next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for next_node """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class for a Singly linked list """
    def __init__(self):
        """ initialize class """
        self.head = None

    def __str__(self):
        """To string method"""
        result = ""
        node = self.head
        while node:
            result += str(node.data) + '\n'
            node = node.next_node
        return result[:-1]

    def sorted_insert(self, value):
        """Inserts a new node at sorted position"""
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new_node.next_node = node.next_node
        node.next_node = new_node
