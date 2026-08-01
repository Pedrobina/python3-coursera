#A nested list (nested) is provided below. Use indexing and the in operator to create variables with Boolean values. See comments for further instructions. Do not hard code.
nested = {
    'data': ['finding', 23, ['exercises', 'hangout', 34]],
    'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics', ['physics', 'chemistry', 'biology']]]
}

# Check to see if the string 'data' is a key in nested. If it is, assign True to the variable data, otherwise assign False.
data = 'data' in nested

# Check to see if the integer 24 is in the value of the key 'data' in nested. If it is, assign True to the variable twentyfour, otherwise assign False.
twentyfour = 24 in nested['data']

# Check to see that the string 'whole' is *not* in the value of the key 'window' in nested. If it's not, then assign True to the variable whole, otherwise assign False.
whole = 'whole'  not in nested['window']

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign True to the variable physics, otherwise False.
physics = 'physics' in nested




assert data == True, "data does not have the correct value"
assert twentyfour == False, "twentyfour does not have the correct value"
assert whole == False, "whole does not have the correct value"
assert physics == False, "physics does not have the correct value"