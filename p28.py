def thaimei():
        with open ("file2.txt", 'r') as korou:
            satees = korou.read()
        with open("thaimeifile.txt", 'w') as file1:
            file1.write(satees)
            print("Successfully copied!") 
if __name__=="__main__":
    thaimei()

