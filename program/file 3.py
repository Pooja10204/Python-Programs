def remove_vowels(input_string):
   vowels="aeiouAEIOU"
   result=' '.join([char for char in input_string if char not in vowels])
   return result
input_str="Hello, World!"
output_str=remove_vowels(input_str)
print(output_str)