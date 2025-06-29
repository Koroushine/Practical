def p29():
    try:
        with open("source.txt", 'r') as file, open("dest.txt", 'w') as file1:
            line_count = 1
            for i in file:
                if line_count % 2 != 0:
                    file1.write(i)
                    print("One line written")
                line_count += 1
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    p29()
