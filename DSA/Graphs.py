# Graphs are created through Dictionaries or Has maps.

# though Dictionaries are essential for creating Graphs a can be Dictionary of tuples, lists or arrays etc ...


# A simple graph using dictionary

graph1 = { # A graph that is a dictionary of lists 
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


graph2 = { # A graph that is a dictionary of tuples 
    'A': ('B', 'C'),
    'B': ('A', 'D', 'E'),
    'C': ('A', 'F'),
    'D': ('B'),
    'E': ('B', 'F'),
    'F': ('C', 'E'),
    'G': ('H'),
    'H': ('G')
}

import pandas as pd 

graph3 = {} # A graph of arrays 

array = pd.array([1, 2])
array2 = pd.array([3, 4])

graph3['A'] = (array)
graph3['B'] = (array2)

print(graph3)