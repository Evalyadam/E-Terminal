import os
import time
import winsound

def create_file(file_name, content=""):
    with open(file_name, "w") as file:
        file.write(content)

def main():
    print("Welcome to the E-terminal.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit()" or user_input.lower() == "exit":
            time.sleep(1)
            break
        if user_input.lower() == "version":
            print("E-Terminal Version 1.1")
            winsound.Beep(440, 500)
        
        
        if user_input.lower() == "make_dir":
            dir_name = input("Enter directory name: ")
            winsound.Beep(220, 500)
            try:
                os.mkdir(dir_name)
                print(f"Directory '{dir_name}' created successfully.")
            except OSError as e:
                print(f"Failed to create directory: {e}")
        
        
        if user_input.lower() == "write_file":
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            try:
                create_file(file_name, content)
                print(f"File '{file_name}' created successfully.")
            except Exception as e:
                print(f"Failed to create file: {e}")
        
        
        if user_input.lower().startswith("cd "):
            dir_name = user_input[3:]
            try:
                os.chdir(dir_name)
                print(f"Changed directory to '{dir_name}'.")
            except OSError as e:
                print(f"Failed to change directory: {e}")
        
        
        if user_input.lower() == "help_us":
            time.sleep(1)
            print("THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS THIS IS NOT WHAT IT SEEMS.")
        
        
        if user_input.lower() == "help":
            print("exit or exit(): Exits the terminal \n \n version: shows the version of the terminal \n \n make_dir: Makes a directory \n \n write_file: Writes a new file with content \n \n delete: deletes a file \n \n info/information: Displays information about the terminal. \n \n Specter: {redacted} \n \n friend: {redacted} \n \n HELP_US: {redacted}")
        
        
        if  user_input.lower() == "info" or user_input.lower() == "information":
            print("E-Terminal - (C) 2024 - V 1.1 - Built in Python3.9, For more information visit the github repo at https://github.com/Evalyadam/E-Terminal")
        
        
        if user_input.lower() == "Specter":
            print("2003, Josh Davidson and his cousin, Oliver Dhamer, decided to work together to make a terminal. They would regret their actions; As they would get weird nightmares day. after. day. They would delete the project and distribute it through github to get rid of the curse.")
        
        else:
            print("")

if __name__ == "__main__":
    main()
