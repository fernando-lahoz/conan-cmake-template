# VSCode problem solver

## CMakeTools buttons do not work properly
 1) Make sure you first compile the project using tasks.
 2) Press `Ctrl` + `shift` + `P` and look for *"CMake: Configure"*
 3) Choose `conan_toolchain.cmake`
 4) Restart VSCode.

## Intellisense does not find included files
 1) Press `Ctrl` + `shift` + `P` and look for *"C/C++: Select Intellisense confguration"*.
 2) Choose *CMakeTools*.
 3) Press `Ctrl` + `shift` + `P` and look for *"Preferences: Open User Settings"*.
 4) In user settings look for *"C_Cpp mergeConfigurations"* and set it true.
 5) Reconfigure CMake using tasks.
