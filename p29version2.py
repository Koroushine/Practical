def copyfun():
    with open("file1copy.txt", 'r') as thaimei:
        with open("File1copy2.txt", "w") as korou:
            line_no = 1
            for line in thaimei:
                if line_no % 2 == 0:
                    korou.write(line)
                    print(line ,end = "")
                line_no += 1 

if __name__ == "__main__":
    copyfun()