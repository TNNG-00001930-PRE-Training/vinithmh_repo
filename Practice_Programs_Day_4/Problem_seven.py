"""
7. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input
"""

def is_all_even_digits(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

if __name__ == "__main__":
    even_digit_numbers = []

    for num in range(1000, 3001):
        if is_all_even_digits(num):
            even_digit_numbers.append(str(num))

    result_str = ",".join(even_digit_numbers)
    
    print("Numbers with all even digits between 1000 and 3000 (inclusive):")
    print(result_str)
