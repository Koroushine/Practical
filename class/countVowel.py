def countv(s):
    vowel = "aeiou"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
    return count
s = input("Enter a string: ")
print("Number of vowels in the string:", countv(s))