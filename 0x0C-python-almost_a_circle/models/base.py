#!/usr/bin/python3
""" Module that within class Base """
import json
import csv
import os.path


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        list_d = []

        if not list_objs:
            pass
        else:
            for m in range(len(list_objs)):
                list_d.append(list_objs[m].to_dictionary())

        lis = cls.to_json_string(list_d)

        with open(filename, 'w') as y:
            y.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an obj """
        if cls.__name__ == "Rectangle":
            ne = cls(10, 10)
        else:
            ne = cls(10)
        ne.update(**dictionary)
        return ne

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as y:
            list_str = y.read()

        list_cls = cls.from_json_string(list_str)
        list_in = []

        for i in range(len(list_cls)):
            list_in.append(cls.create(**list_cls[i]))

        return list_in

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_d = [0, 0, 0, 0, 0]
            list_key = ['id', 'width', 'height', 'x', 'y']
        else:
            list_d = ['0', '0', '0', '0']
            list_key = ['id', 'size', 'x', 'y']

        mat = []

        if not list_objs:
            pass
        else:
            for ob in list_objs:
                for km in range(len(list_key)):
                    list_d[km] = ob.to_dictionary()[list_key[km]]
                mat.append(list_d[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            read = csv.reader(readFile)
            csv_list = list(read)

        if cls.__name__ == "Rectangle":
            list_key = ['id', 'width', 'height', 'x', 'y']
        else:
            list_key = ['id', 'size', 'x', 'y']

        mat = []

        for csv_elem in csv_list:
            dict_csv = {}
            for km in enumerate(csv_elem):
                dict_csv[list_key[km[0]]] = int(km[1])
            matrix.append(dict_csv)

        list_in = []

        for i in range(len(mat)):
            list_in.append(cls.create(**mat[i]))

        return list_in
