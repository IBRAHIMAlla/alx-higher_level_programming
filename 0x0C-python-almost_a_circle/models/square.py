#!/usr/bin/python3
""" class Square,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ special method """
        str_sq = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_sq + str_id + str_xy + str_wh

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ special method """
        str_rec = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rec + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """ update """
        if args is not None and len(args) is not 0:
            list_a = ['id', 'size', 'x', 'y']
            for m in range(len(args)):
                if list_a[m] == 'size':
                    setattr(self, 'width', args[m])
                    setattr(self, 'height', args[m])
                else:
                    setattr(self, list_a[m], args[m])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns a dictionary """
        list_a = ['id', 'size', 'x', 'y']
        dict_r = {}

        for k in list_a:
            if k == 'size':
                dict_r[k] = getattr(self, 'width')
            else:
                dict_r[k] = getattr(self, k)

        return dict_r
