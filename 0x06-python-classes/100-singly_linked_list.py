#!/usr/bin/python3
"""Define a class Node"""


class Node:
    """ singly linked list
        Attributes:
            data (int): data
            next_node (Node, optional): node
    """

    def __init__(self, data, next_node=None):
        """Initialize
        args:
            data (int)
            next_node (Node)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter
        returns:
            data (int)
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter
        args:
            value (int): value to set
        returns:
            None
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """data getter
        returns:
            data (int)
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """data setter
        args:
            value (Node)
        returns:
            None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class
    """

    def __init__(self):
        """Initialize"""
        self.__head = None

    def sorted_insert(self, value):
        """insert node
        args:
            value (int): value for node
        """
        n = Node(value)
        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n
        else:
            tp = self.__head
            while (tp.next_node is not None and
                    tp.next_node.data < value):
                tp = tp.next_node

            n.next_node = tp.next_node
            tp.next_node = n

    def __str__(self):
        """Define the print()"""
        v = []
        tp = self.__head
        while tp is not None:
            v.append(str(tp.data))
            tp = tp.next_node
        return ('\n'.join(v))
