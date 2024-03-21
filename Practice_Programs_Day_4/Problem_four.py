"""
4. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""

class StringOperation:

    def __init__(self):
        pass

    def getString(self):
        input_string = input("Enter a string: ")
        return input_string
    
    def printString(self, input_string):
        print(input_string.upper())

    
def test_string_operation():
    string_op = StringOperation()
    input_string = string_op.getString()
    string_op.printString(input_string)

test_string_operation()
