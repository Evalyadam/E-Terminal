import os
import time
import winsound
import subprocess



# def check_password():
#     with open("secret_lol/psswd.txt", 'r') as psswd:
#         password = psswd.read()

# def change_psswd(new_psswd):
#     with open("secret_lol/psswd.txt", 'w') as psswd:
#         psswd.write(new_psswd)
#         return psswd

def create_file(file_name, content=""):
    with open(file_name, "w") as file:
        file.write(content)

def main():
    debug_mode = False  # Initialize debug_mode here
    print("Welcome to the E-terminal.")
    while True:
        user_input = input(">> ")
        if user_input.lower() in ("exit", "exit()"):
            time.sleep(1)
            break
        elif user_input.lower() == "version":
            print("E-Terminal Version 1.3")
            winsound.Beep(440, 500)
        elif user_input.lower() == "make_dir":
            dir_name = input("Enter directory name: ")
            winsound.Beep(220, 500)
            try:
                os.mkdir(dir_name)
                print(f"Directory '{dir_name}' created successfully.")
            except OSError as e:
                print(f"Failed to create directory: {e}")
        elif user_input.lower() == "write_file":
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            try:
                create_file(file_name, content)
                print(f"File '{file_name}' created successfully.")
            except Exception as e:
                print(f"Failed to create file: {e}")
        elif user_input.lower().startswith("cd "):
            dir_name = user_input[3:]
            try:
                os.chdir(dir_name)
                print(f"Changed directory to '{dir_name}'.")
            except OSError as e:
                print(f"Failed to change directory: {e}")
        elif user_input.lower() == "help":
            print("exit or exit(): Exits the terminal \n \n version: shows the version of the terminal \n \n make_dir: Makes a directory \n \n write_file: Writes a new file with content \n \n delete: deletes a file \n \n info/information: Displays information about the terminal. \n \n debug_mode/debug_mode_off: Turns debug mode on and off. \n \n SUPERUSR lets you accses the superuuser menu.")
        elif user_input.lower() in ("info", "information"):
            print("E-Terminal - (C) 2024 - V 1.3 - Built with Python3.9, For more information visit the GitHub repo at https://github.com/Evalyadam/E-Terminal")
        elif user_input.lower() == "debug_mode":
            usr_psswrd_inp = input("Enter Password: ")
            with open("secret_lol/psswd.txt", 'r') as psswd:
                password = psswd.read()
                if usr_psswrd_inp == password:
                    debug_mode = True
                    print("Debug Mode Enabled")
                    print("For more info on Debug mode, Visit https://github.com/Evalyadam/E-Terminal.")
                else:
                    print("Wrong password.")
        elif user_input.lower() == "debug_mode_off":
            if debug_mode:
                debug_mode = False
                print("Debug Mode Disabled.")
            else:
                print("ERR: Debug_Mode already disabled.")
        elif user_input.lower() == "superusr":
            if debug_mode:
                subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'python', 'debugmenu.py'])
            else:
                print("ERR: DEBUG_MODE TURNED OFF")
                winsound.Beep(440, 100)
        
        elif user_input.lower() == "psswd":
            psswd_check = input("Enter old password: \n")
            password_file_path = os.path.join('secret_lol', 'psswd.txt')
            if os.path.exists(password_file_path):
                with open(password_file_path, 'r') as psswd_file:
                    old_psswrd = psswd_file.read().strip()
                    if psswd_check == old_psswrd:
                        new_psswrd = input("Enter new password: \n")
                        with open(password_file_path, 'w') as file:
                            file.write(new_psswrd)
                        print(f'New password: {new_psswrd}')
                    else:
                        print("Wrong password.")
            else:
                print("Password file not found.")
        else:
            pass

if __name__ == "__main__":
    main()
