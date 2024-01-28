import os
import sys

def replace_text_in_file(file_path, text_to_find, new_text):
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = content.replace(text_to_find, new_text)

    with open(file_path, 'w') as file:
        file.write(modified_content)


#main:

path_config = "./build/SDL2_imageTargets.cmake"
path_release = "./build/SDL2_image-release-x86_64-data.cmake"
path_debug = "./build/SDL2_image-debug-x86_64-data.cmake"

if not os.path.isfile(path_config):
    print(f"SDL2_image is not installed in this project", file=sys.stderr)
    exit(1)

replace_text_in_file(path_config, "SDL2_image-static", "SDL2_image")

if os.path.isfile(path_release):
    replace_text_in_file(path_release, "SDL2_image-static", "SDL2_image")

if os.path.isfile(path_debug):
    replace_text_in_file(path_debug, "SDL2_image-static", "SDL2_image")
