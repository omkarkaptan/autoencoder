from sys import version_info

def stdin_read(what):
    py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

    if py3:
      response = input(what)
    else:
      response = raw_input(what)

    return response

def read_number(what):
    number = stdin_read(what)
    # PERFORM TYPE CHECKS
    return int(number)
