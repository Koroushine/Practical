def v():
    with open ("file1copy.txt", "r") as thaimei:
        text = thaimei.read()
    words = text.split()
    cout = 0
    word_count = len(words)
    vowels = "aeiouAEIOU"
    for word in words:
        for char in words:
            for char in vowels:
                cout += 1
    
    print(f'The no of words are {word_count}')
    print(f'The no of vowels are : {cout}')

if __name__ == "__main__":
    v()