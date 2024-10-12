def count_words(input_string):
    # Split the string into words using spaces as delimiters
    words = input_string.split()
    return len(words)
input_str = "Hello, how are you?"
word_count = count_words(input_str)
print(f"Number of words: {word_count}")