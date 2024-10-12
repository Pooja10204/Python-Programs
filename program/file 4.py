def count_unique_characters(input_string):
#convert the string to a set to get unique characters, then return its length
   unique_chars=set(input_string)
   return len(unique_chars)
input_str="Hello, Guvi"
unique_count=count_unique_characters(input_str)
print(unique_count)