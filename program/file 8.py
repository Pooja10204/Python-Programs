def is_anagram(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare the sorted versions of both strings
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "Listen"
string2 = "Silent"
result = is_anagram(string1, string2)
print(result)