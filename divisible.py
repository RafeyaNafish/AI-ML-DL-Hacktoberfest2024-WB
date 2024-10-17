def all_digits_divide(n):
    # Convert the number to a string to easily access its digits
    num_str = str(n)
    
    for digit in num_str:
        # Convert the character back to an integer
        d = int(digit)
        
        # Skip if the digit is 0 to avoid division by zero
        if d == 0 or n % d != 0:
            return False
    return True

# Example usage:
number = 128
if all_digits_divide(number):
    print(f"All digits of {number} divide it.")
else:
    print(f"Not all digits of {number} divide it.")
