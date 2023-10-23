#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints the  x elememts of a list.
    Args:
        my_list (list): This is the list to print elements from.
        x (int): The number of elements to print from  my_list int.
    Returns:
        The number of elements printed.
    """
    printed_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
        except IndexError:
            break
    print("")
    return (printed_elements)
