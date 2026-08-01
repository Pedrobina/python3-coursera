#A nested list (lst) is provided below. Use indexing and the in operator to create variables with Boolean values. See comments for further instructions. Do not hard code.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
# Use indexing and the 'in' operator to assign values to the variables according to the instructions below
# No hardcoding!

# Test to see if 'yellow' is in the third list of lst. Save to variable `yellow`
yellow = 'yellow'  in lst[2]
# Test to see if 4 is in the second list of lst. Save to variable `four`
four = 4 in lst[1]
# Test to see if 'orange' is in the first element of lst. Save to variable `orange`
orange = 'orange' in lst[0]




assert yellow == True, "yellow does not have the correct value"
assert four == False, "four does not have the correct value"
assert orange == True, "orange does not have the correct value"