#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # this will hold our division results
    new_list = []
 
    # loop through each position up to list_length
    for i in range(list_length):
        # start with 0 as the default result
        result = 0
 
        try:
            # try to divide the two elements
            result = my_list_1[i] / my_list_2[i]
 
        except ZeroDivisionError:
            # can't divide by 0
            print("division by 0")
 
        except (ValueError, TypeError):
            # one of the elements is not a number
            print("wrong type")
 
        except IndexError:
            # one of the lists is too short
            print("out of range")
 
        finally:
            # always add the result to the new list
            new_list.append(result)
 
    return new_list
