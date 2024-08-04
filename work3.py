"""work3.py"""

import re

def split_string_by_delimiters(s, delimiters):
    pattern = f"[{re.escape(delimiters)}]+"
    return re.split(pattern, s)

if __name__ == "__main__":
    s = input("Введите строку: ")
    delimiters = input("Введите разделители: ")
    result = split_string_by_delimiters(s, delimiters)
    print(result)

