"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    print(items)
    for item in items:
        item = str(item)
        if item not in frequencies.keys():
            frequencies[item] = 1
        else:
            frequencies.update({item: frequencies.get(item)+1})
    print(frequencies)

    return frequencies
