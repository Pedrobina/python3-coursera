#Below, we have provided a nested dictionary, sports. Index into the dictionary to create variables that we have listed in the code window.

sports = {
    'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'],
    'diving':   ['springboard', 'platform', 'synchronized'],
    'track':    ['sprint', 'distance', 'jumps', 'throws'],
    'gymnastics': {
        'women':['vault', 'floor', 'uneven bars', 'balance beam'],
        'men':  ['vault', 'parallel bars', 'floor', 'rings']
    }
}

# Assign the string 'backstroke' to the variable v1
v1 = sports['swimming'][2]

# Assign the string 'platform' to the variable v2
v2 = sports['diving'][1]

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the variable v3
v3 = sports['gymnastics']['women']

# Assign the string 'rings' to the variable v4
v4 = sports['gymnastics']['men'][3]

assert v1 == 'backstroke'
assert v2 == 'platform'
assert v3 == ['vault', 'floor', 'uneven bars', 'balance beam']
assert v4 == 'rings'
