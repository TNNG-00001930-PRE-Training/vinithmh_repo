def is_all_even_digits(number):
    # Check if all digits in the number are even
    return all(int(digit) % 2 == 0 for digit in str(number))

if __name__ == "__main__":
    # Initialize an empty list to store the numbers with all even digits
    even_digit_numbers = []

    # Iterate through the range from 1000 to 3000 (inclusive)
    for num in range(1000, 3001):
        if is_all_even_digits(num):
            even_digit_numbers.append(str(num))

    # Join the list of numbers into a comma-separated string
    result_str = ",".join(even_digit_numbers)

    # Print the result
    print("Numbers with all even digits between 1000 and 3000 (inclusive):")
    print(result_str)