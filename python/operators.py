a = 24
b = 16

# comparison
print(a == b)  # equals
print(a > b)  # greater than
print(a < b)  # less than
print(a != b)  # not equals
print(a >= b)  # greater than or equal
print(a <= b)  # less than or equal

# operators
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a ** b)  # exponentiation
print(a // b)  # floor division
print(a % b)  # modulus

# boolean built-in methods
greeting = 'Hello World!'
print(greeting)
print(greeting.isalpha())  # only letters
print(greeting.islower())  # only lowercase characters
print(greeting.startswith('H'))  # stars with [argument]
print(greeting.endswith('!'))  # ends with [argument]
print(greeting.isdigit())  # only numbers

# string slicing
print(len(greeting))  # length of string (or array)
print(greeting[6:11])  # prints characters 6-10

# String methods
white_space = 'space at the end                                 '
print(white_space)
print(len(white_space))  # length of string (or array)
print(len(white_space.strip()))  # deletes white space at end of string
example_text = 'here`s Some text with a LOT of text'
print(example_text)
print(example_text.count('text'))  # counts the times [argument] appears in the string
print(example_text.lower())  # converts string to lowercase
print(example_text.upper())  # converts string to uppercase
print(example_text.capitalize())  # capitalises first letter
print(example_text.replace('with', 'and'))  # replaces [argument1] with [argument2]
