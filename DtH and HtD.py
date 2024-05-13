def validate_decimal_input(decimal):
    try:
        int(decimal)
        return True
    except ValueError:
        return False

def validate_hexadecimal_input(hexadecimal):
    valid_hex_digits = "0123456789ABCDEF"
    for char in hexadecimal:
        if char.upper() not in valid_hex_digits:
            return False
    return True

def decimal_to_hexadecimal(decimal):
    if not validate_decimal_input(decimal):
        return "Invalid input. Please enter a valid decimal number."

    decimal = int(decimal)  # Convert to integer
    hex_digits = "0123456789ABCDEF"  # Hexadecimal digits
    hexadecimal = ""

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    if not validate_hexadecimal_input(hexadecimal):
        return "Invalid input. Please enter a valid hexadecimal number."

    hex_digits = "0123456789ABCDEF"  # Hexadecimal digits
    decimal = 0

    for digit in hexadecimal:
        decimal = decimal * 16 + hex_digits.index(digit.upper())

    return decimal

# Test the functions
decimal_input = input("Enter a decimal number: ")
hexadecimal_output = decimal_to_hexadecimal(decimal_input)
print("Hexadecimal equivalent:", hexadecimal_output)

hexadecimal_input = input("Enter a hexadecimal number: ")
decimal_output = hexadecimal_to_decimal(hexadecimal_input)
print("Decimal equivalent:", decimal_output)
