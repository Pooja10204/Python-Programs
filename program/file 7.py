from collections import Counter

def most_frequent_character(input_string):
    # Count the frequency of each character
    frequency = Counter(input_string)
    
    # Find the character with the highest frequency
    most_frequent = max(frequency, key=frequency.get)
    
    return most_frequent
 
input_str = "hello world"
result = most_frequent_character(input_str)
print(f"The most frequent character is: '{result}'")