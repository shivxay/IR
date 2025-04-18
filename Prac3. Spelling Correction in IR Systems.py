# A Naive recursive Python program to find the minimum number
# of operations to convert str1 to str2
def editDistance(str1, str2, m, n):
    # If first string is empty, the only option is to insert all characters of second string into first
    if m == 0:
        return n
    # If second string is empty, the only option is to remove all characters of first
    if n == 0:
        return m
    # If last characters of two strings are the same, nothing much to do. Ignore the last characters and get the count for the remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)
    # If last characters are not the same, consider all three operations on the last character of the first string,
    # recursively compute the minimum cost for all three operations and take the minimum of the three values.
    return 1 + min(
        editDistance(str1, str2, m, n - 1),  # Insert
        editDistance(str1, str2, m - 1, n),  # Remove
        editDistance(str1, str2, m - 1, n - 1)  # Replace
    )
# Driver code
str1 = "sunday"
str2 = "saturday"
print('Edit Distance is:', editDistance(str1, str2, len(str1), len(str2)))
