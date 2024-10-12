def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for comparison
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
input_str = "madam"
result = is_palindrome(input_str)
print(result)