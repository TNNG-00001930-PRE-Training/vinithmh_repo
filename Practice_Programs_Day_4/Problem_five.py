"""
5. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def sort_words(input_str):
    # Split the input string into a list of words
    words = input_str.split(',')

    # Sort the list of words alphabetically
    sorted_words = sorted(words)

    # Join the sorted words back into a comma-separated string
    sorted_str = ','.join(sorted_words)

    return sorted_str

if __name__ == "__main__":
    input_str = input("Enter a comma-separated sequence of words: ")
    sorted_str = sort_words(input_str)
    print("Sorted words:", sorted_str)
