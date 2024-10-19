# Graphs can be created through Dictionaries or Hashmaps.

# though Dictionaries are essential for creating Graphs it can be made with Dictionary of tuples, Dictionary lists or arrays even with matrices ...

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