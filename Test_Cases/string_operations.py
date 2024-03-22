"""
String Operations:
Test cases for string concatenation
Test cases for string slicing
Test cases for string formatting
Test cases for string manipulation methods (e.g., upper(), lower(), strip(), replace())
"""

def concatenate_strings(str1, str2):
    return str1 + str2

def slice_string(string, start, end):
    return string[start:end]

def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

def upper_string(string):
    return string.upper()

def lower_string(string):
    return string.lower()

def strip_string(string):
    return string.strip()

def replace_string(string, old, new):
    return string.replace(old, new)


