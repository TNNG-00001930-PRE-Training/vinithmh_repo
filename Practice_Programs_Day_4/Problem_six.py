"""
6. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

def remove_duplicates_and_sort(input_str):
    # Split the input string into a list of words
    words = input_str.split()

    # Remove duplicates by converting the list to a set
    unique_words = set(words)

    # Sort the unique words alphabetically
    sorted_unique_words = sorted(unique_words)

    # Join the sorted unique words back into a whitespace-separated string
    result_str = ' '.join(sorted_unique_words)

    return result_str

if __name__ == "__main__":
    input_str = input("Enter a sequence of whitespace-separated words: ")
    result_str = remove_duplicates_and_sort(input_str)
    print("Words after removing duplicates and sorting:", result_str)
