#!/usr/bin/python3
""" class Base """
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
        list_dic = []

        if not list_objs:
            pass
        else:
            for m in range(len(list_objs)):
                list_dic.append(list_objs[m].to_dictionary())

        l = cls.to_json_string(list_dic)

        with open(filename, 'w') as y:
            y.write(l)

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
            nw = cls(10, 10)
        else:
            nw = cls(10)
        nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        """ Returns a list of obj """
        fln = "{}.json".format(cls.__name__)

        if os.path.exists(fln) is False:
            return []

        with open(fln, 'r') as y:
            list_s = y.read()

        list_c = cls.from_json_string(list_s)
        list_i = []

        for m in range(len(list_c)):
            list_i.append(cls.create(**list_c[m]))

        return list_i

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV """
        fln = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_d = [0, 0, 0, 0, 0]
            list_k = ['id', 'width', 'height', 'x', 'y']
        else:
            list_d = ['0', '0', '0', '0']
            list_k = ['id', 'size', 'x', 'y']

        matx = []

        if not list_objs:
            pass
        else:
            for o in list_objs:
                for v in range(len(list_k)):
                    list_d[v] = o.to_dictionary()[list_k[v]]
                matx.append(list_d[:])

        with open(fln, 'w') as writeFile:
            wr = csv.wr(writeFile)
            wr.writerows(matx)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV """
        fln = "{}.csv".format(cls.__name__)

        if os.path.exists(fln) is False:
            return []

        with open(fln, 'r') as readFile:
            re = csv.re(readFile)
            csv_l = list(re)

        if cls.__name__ == "Rectangle":
            list_k = ['id', 'width', 'height', 'x', 'y']
        else:
            list_k = ['id', 'size', 'x', 'y']

        matx = []

        for csv_elem in csv_l:
            dict_cs = {}
            for v in enumerate(csv_elem):
                dict_cs[list_k[v[0]]] = int(v[1])
            matx.append(dict_cs)

        list_i = []

        for m in range(len(matx)):
            list_i.append(cls.create(**matx[m]))

        return list_i
