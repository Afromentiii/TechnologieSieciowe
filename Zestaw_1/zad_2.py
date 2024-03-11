FILE_TO_COPY = "lab1zad1.png"

file_name = input("Enter filename: ")
destination_file = open(FILE_TO_COPY, "wb")

try:
    f = open(file_name, "rb")
    destination_file.write(f.read())
    print("Copying operation successful.")
    
    f.close()
except FileNotFoundError:
    print("Wrong filename.")
    
destination_file.close()