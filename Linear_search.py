def linear_search(list, key):
    """if key is in the list returns its position in the list,
       otherwise returns -1 and the list get's iterated through a loop while comparing it with the key value"""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

l = [1,5,8,6,2,8,8,2,2,55,45,5,5,54,55,565,6]

print("The key value is found at : ",linear_search(l,565)," using linear search\n\nWhere", linear_search.__doc__)