def is_int(x):
    x_string = str(x)
    if (type(x) == float):
        for i in range(x_string.index('.')+1, len(x_string)):
            if (x_string[i] != '0'):
                return False
            else:
                return True
    elif (type(x) == int):
        return True
    else:
        return False

