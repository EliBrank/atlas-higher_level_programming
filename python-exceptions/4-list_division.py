#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    for i in range(list_length):
        next_num = 0
        try:
            next_num = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            list_result.append(next_num)

    return list_result
