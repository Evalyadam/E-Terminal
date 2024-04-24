import os
import time
import winsound
import sys
import requests
running = True

def rlimet():
    new_limit = input("\nEnter new recursion limit: ")
    try:
        new_limit = int(new_limit)
        sys.setrecursionlimit(new_limit)
        print("Recursion limit updated successfully.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

banner = "------------- SuperUser Menu-------------"

print(banner)

running = True

while running:
    user_input = input(">>")

    if user_input == "help":
        print("super-info: Gives  E X T R A  info. \nrlimit: Sets the recursion limit. \nget-rlimit: Prints the recursion limit. \ndfp install: Installs a package from a URL (Note: both save path and url are user input).")

    if user_input == "super-info":
        print(f"Python Version: {sys.version}, Operating Sys info: {sys.platform}")

    if user_input == "rlimit":
        rlimet()
    
    if user_input == "get-rlimit":
        print(sys.getrecursionlimit)
    
    if user_input == "dfp install":
        url = input("URL: ")
        save_path = input("Save path: ")
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
                print(f"File downloaded and saved to {save_path}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
