def longest_common_substring(str1, str2):
    # Create a matrix to store lengths of longest common suffixes
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    longest_length = 0  # Store the length of the longest common substring
    longest_substring = ""  # Store the longest common substring

    # Fill the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
  if str1[i - 1] == str2[j - 1]:  # Check for matching characters
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                # Update the longest substring if a new maximum length is found
                if matrix[i][j] > longest_length:
                    longest_length = matrix[i][j]
                    longest_substring = str1[i - longest_length:i]
            else:
                matrix[i][j] = 0  # No match

    return longest_substring
str1 = "python"
str2 = "programming"
result = longest_common_substring(str1, str2)
print(f"Longest common substring: '{result}'")