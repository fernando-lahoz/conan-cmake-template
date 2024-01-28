import os
import sys

#main:

if not os.path.exists("./scripts/.project_name"):
    print("No project name found. Maybe you have not config nor installed your conan profiles.")
    print()
    os.system("python3 ./scripts/conan_config_profiles.py")
    os.system("python3 ./scripts/conan_install.py")
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

os.system(f"cmake -S\".\" -B\"build\" -G Ninja -DCMAKE_TOOLCHAIN_FILE=\"conan_toolchain.cmake\" -DCMAKE_CXX_COMPILER=g++ -DCMAKE_BUILD_TYPE={mode}")