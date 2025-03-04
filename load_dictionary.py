"""Python module to load file"""
import sys

def load(file_name):
    """Function that loads a file"""
    try:
        with open(file_name,"r", encoding="utf-8") as file:
            loaded_text = file.read().strip().split()
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print(f"{e}\nError opening {file_name}. Terminating program.",file=sys.stderr)
        sys.exit(1)

load("2of4brif.txt")
