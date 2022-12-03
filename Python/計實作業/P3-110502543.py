"""
Practice 3
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
def create_file():
    file_1=input("Create a file: ",)
    write_1 = input("Write something: ",)
    file = open("ncu.txt", 'w')
    file.write(write_1)
    file.close()
    print("File name:",file_1)
    print("Context:",write_1)
create_file()





