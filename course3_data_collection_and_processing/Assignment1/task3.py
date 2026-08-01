#A nested list (L) is provided below. Use indexing and the in operator to create variables with Boolean values. See comments for further instructions. Do not hard code.
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Check if 'hola' is in the list L. Save to variable name test1
test1 = 'hola' in L

# Check if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L

# Check if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]

assert test1 == False, "test1 does not have the correct value"
assert test2 == True, "test2 does not have the correct value"
assert test3 == True, "test3 does not have the correct value"