# Function to find whether the given strings are Anagram or Not
def anagram(S1, S2):
    # Make the two string lower cased.
    S1 = S1.replace(' ', '').lower()
    S2 = S2.replace(' ', '').lower()

    # Check whether the length of two strings are equal or not.
    if len(S1) != len(S2):
        return False

    # Initialize an empty dictionary to store the count.
    count = {}

    # Add the letters into the count dictionary
    for letter in S1:  # For every letter in the first string
        if letter in count:  # If letter is already in my dictionary, then
            count[letter] += 1  # Add 1 to that letter key
        else:
            count[letter] = 1

    # Applying the above as a reverse logic on the second string.
    for letter in S2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Checking whether the count is empty. If empty then return as Anagram, if not otherwise.
    for k in count:
        if count[k] != 0:
            return False

    return True


if __name__ == '__main__':
    S1 = 'Clint Eastwood'
    S2 = 'old West action'
    print(f"Anagram is {anagram(S1, S2)}")
