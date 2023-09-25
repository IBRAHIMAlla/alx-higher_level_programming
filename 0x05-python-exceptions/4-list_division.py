#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    n_list = []
    rslt = 0
    for m in range(0, list_length):
        try:
            rslt = (my_list_1[m] / my_list_2[m])
        except TypeError:
            rslt = 0
            print("wrong type")
        except ZeroDivisionError:
            rslt = 0
            print("division by 0")
        except IndexError:
            rslt = 0
            print("out of range")
        finally:
            n_list.append(rslt)
    return n_list
