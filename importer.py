import glob
import os.path
import sys

def imp_files ():
    # imports all py files
    py_files=(glob.glob("*.py")) 

    # removes this file of the list
    py_files.remove(sys.argv[0])
    py_files.sort()
    return(py_files)

def menu ():
    # clear the shell
    os.system('clear')
    files = imp_files()
    # Generate the output of the menu
    print("Following files are in this directory: \n")
    for index in range(0,len(files)):
            print(index, files[index])
    
    # Choosing the options

    option = input("Which file do you want to run? Press q to exit this program: \n")
    a= list(range(0,len(files)))
    if (option in str(a)):
        #os.path.dirname declares the position of the file
        exec(compile(open((os.path.dirname(sys.argv[0]) + files[int(option)])).read(),files[int(option)], 'exec'))
        pause = input("Push any button to return") 
        menu()
    elif (option == "q"):
        print("Bye")

    else:
        print("Please decide between the files or press q to exit")
        input("Push any button to return")
        menu()

menu()
