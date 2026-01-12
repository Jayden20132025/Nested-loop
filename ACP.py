# Decimal to Binary Conversion Program

# Take input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert decimal to binary
binary_number = bin(decimal_number)

# Display the result
print("Binary equivalent:", binary_number[2:])
