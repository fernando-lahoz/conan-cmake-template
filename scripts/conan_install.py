import os
import sys

def delete_directory(directory_path):
    try:
        os.rmdir(directory_path)
        print(f"Directory '{directory_path}' successfully deleted.")
    except OSError as e:
        print(f"Error: {e}")

#main:

if not os.path.exists("./scripts/.project_name"):
    print("No project name found. Maybe you have not config your conan profiles.")
    print()
    os.system("python3 ./scripts/conan_config_profiles.py")
else:
    with open("./scripts/.project_name", 'r') as file:
        project_name = file.read()

mode = ""
if len(sys.argv) > 1:
    mode = sys.argv[1]
    if mode != "Release" and mode != "Debug":
        mode = ""
if mode == "":
    mode = input("Specify build mode (*Debug*|Release): ")
    if (mode == ""):
        mode = "Debug"
    while mode != "Release" and mode != "Debug":
        mode = input("Specify build mode (*Debug*|Release): ")
        if (mode == ""):
            mode = "Debug"

delete_directory("./build/")
os.system(f"conan install . --output-folder=build --build=missing -pr={project_name}_{mode}")