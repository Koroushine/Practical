def vowel_count():
    with open("file1.txt", 'r') as file:
        text = file.read()
    words = text.split()
    print(words)
    no_word = len(words)
    cout = 0
    vowels = "aeiouAEIOU"
    for word in words:
        for char in words:
            if char in vowels:
                cout = cout+1
    print(f'\nNo. of words are: {no_word}')
    print(f'No. of vowels are : {cout}')

if __name__ == "__main__":
    vowel_count()