def file_copy():
    try:
        with open ("file1.txt", 'r') as file:
            text = file.read()
        with open("file1copy.txt", 'w') as file1:
            file1.write(text)
            print("Successfully copied!") 
    except Exception as e:
        print(e)
if __name__=="__main__":
    file_copy()