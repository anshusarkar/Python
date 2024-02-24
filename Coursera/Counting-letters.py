def count(text:str):
    result={}
    for letter in text:
        if letter not in result:
            result[letter] = 0 # The letter becomes a key to the dict result
        else:
            result[letter] += 1 # The value of the dict incresses +1 if multiple instances of a letter is found in the given string
    return result

print(count("CA-CA-CHEE-CHEE"))