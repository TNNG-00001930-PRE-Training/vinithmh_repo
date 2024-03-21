"""
2. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()
"""

def form_dictionary(num):
    numbers = []
    squares = []

    numbers = [i for i in range(1, num+1)]

    squares = [i*i for i in range(1, num+1)]

    result_dict = dict(zip(numbers, squares))
    return result_dict

num = int(input("Enter the number:"))

result = form_dictionary(num)
print(result)    