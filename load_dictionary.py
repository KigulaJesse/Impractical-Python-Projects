"""Load a text file as a list

    Arguments:
    - text file name and file directory if needed

    Exceptions:
    - IOError if filename not found

    Returns
    - A list of words in a text file in lower case.

    Requires import sys for error logging in color

"""

import sys

def load(file):
    """Open a text file and return a list of lowercase strings"""
    loaded_txt = None
    try:
        with open(file,"r") as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [ x.lower() for x in loaded_txt]

    except IOError as e:
        print(f"{e}\n Error opening {file}. Terminating program",file=sys.stderr)
    return loaded_txt
