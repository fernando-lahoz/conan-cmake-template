import os
import subprocess
import sys

def exec(command):
    try:
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = p.communicate()
        returncode = p.returncode
        return True, stdout, stderr, returncode

    except Exception as e:
        return False, "", "", None

def settings_str(build_type):
    if sys.platform.startswith('win'):
        platform = "Windows"
    elif sys.platform.startswith('linux'):
        platform = "Linux"
    else:
        platform = "<your os> #Windows|Linux|..."

    settings = f"""[settings]
arch=x86_64
build_type={build_type}
os={platform}
compiler=gcc
compiler.version=<your gcc version> #x.y (not x.y.z)
compiler.cppstd=17
compiler.libcxx=libstdc++11
"""
    if sys.platform.startswith('win'):
        settings = settings + """
[buildenv]
CC=<full path to your C compiler executable>
CXX=<full path to your C++ compiler executable>
"""
    return settings

#main:

print("=== Configuring project profiles ===")

if not os.path.exists("./scripts/.project_name"):
    print("No project name detected.")
    project_name = input("Please insert the name of the project: ")
    with open("./scripts/.project_name", 'w') as file:
        file.write(project_name)
else:
    with open("./scripts/.project_name", 'r') as file:
        project_name = file.read()
    
    print(f"Project name detected: {project_name}")
print()

exec(f"conan profile detect")
ok, output, _, _ = exec(f"conan profile path default")
if not ok:
    print("Error: conan is not installed", file=sys.stderr)
    exit(1)
path = os.path.dirname(output)

debug_profile = os.path.join(path, f"{project_name}_Debug")
release_profile = os.path.join(path, f"{project_name}_Release")

if os.path.exists(debug_profile) and os.path.exists(release_profile):
    print("Debug and release profiles already exists for this project.")
else:
    with open(debug_profile, 'w') as file:
        file.write(settings_str("Debug"))
    with open(release_profile, 'w') as file:
        file.write(settings_str("Release"))
    print("Default debug and release profiles have been saved.")

print("Please check this files and configure them with your custom values:")
print(f"\t{debug_profile}")
print(f"\t{release_profile}")
input("=== Press any key to continue ===")