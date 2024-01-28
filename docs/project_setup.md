# Project setup

## Toolchain
The C++ compilation toolchain we are going to install consists in the powerful
combination of GCC as the compiler, CMake as the build tool, and Ninja to
enhance compilation efficiency.

### Linux
To install all this tools in any Linux distribution we can use the native package
manager:

```shell
pacman -S gcc g++ make cmake ninja #Arch
apt-get install gcc g++ make cmake ninja-build #Debian/Ubuntu
dnf install gcc g++ make cmake ninja-build #Fedora
yum install gcc g++ make cmake ninja-build #Centos
```

To check the installation execute them with `--version`:

```shell
gcc --version
g++ --version
make --version
cmake --version
ninja --version 
```

### Windows (MinGW)
There are several ways to install GCC on Windows (most of which are part of the
[MinGW project](https://www.mingw-w64.org/)). The simplest one is to use
[MSYS2](https://www.msys2.org/), a collection of tools and libraries that
includes a Linux terminal and a package manager (`pacman`), which has one of the
latest versions of GCC. You can download an installer (`.exe`) from their last
[github release](https://github.com/msys2/msys2-installer/releases) or the
[official site](https://www.msys2.org/).

Once MSYS2 has been installed we can launch its terminal and install the tools:

```shell
pacman -S mingw-w64-ucrt-x86_64-gcc \
          mingw-w64-ucrt-x86_64-make \
          mingw-w64-ucrt-x86_64-cmake \
          mingw-w64-ucrt-x86_64-ninja   
```

You will need to add your MSYS2 binaries directory to the PATH
([tutorial](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Adding-folder-path-to-Windows-PATH-environment-variable.html)).
With a default installation this directory should be located at `C:\msys64\ucrt64\bin`.
Reset your machine to apply changes and check you can execute every tool:

```shell
gcc --version
g++ --version
make --version
cmake --version
ninja --version 
```

More MSYS2 packages can be found in [this page](https://packages.msys2.org/base).

## Code Editor: VSCode/VSCodium
This project has been configured for the Visual Studio Code editor. You can 
download a pure open source build from the
[VSCodium github releases](https://github.com/VSCodium/vscodium/releases) or the
privative version from Microsoft's [VSCode official site](https://code.visualstudio.com/download). If you chose this last one we highly recommend to disable telemetry:

 1) Open VSCode.
 2) Press `Ctrl` + `shift` + `P` and look for *"Preferences: Open User Settings (JSON)"*.
 3) Add this line to the JSON:
```
{
    ...
    "telemetry.enableTelemetry": false,
    ...
}
```

### Extensions
To make C++ developing easier you should install the following extensions
from the marketplace:
 - `ms-vscode.cpptools-extension-pack`: includes C/C++ IntelliSense, debugging
      support and the CMakeTools extension in order to integrate CMake's building
      and testing utilities.
 - `jeff-hykin.better-cpp-syntax`: improves syntax highlighting for newer and
      more complex features of the language.

## Package Manager
We will use [Conan](https://conan.io/) to manage dependencies. You will first
need to install [Python 3](https://www.python.org/) and the
[pip package manager](https://pip.pypa.io/en/stable/installation/). Then you can
install Conan using pip:
```
pip install conan
```
This will install conan in your Python 3 `Scripts` directory, e.g. `C:\Python310\Scripts`.
Add this directory to the PATH, restart to apply changes and check:
```
conan --version
```

## Configuration and Building
This project has some python scripts to streamline the configuration and building
process. There are
some VSCode tasks written to execute these scripts with a few mouse clicks.
To run a task go to the upper menu and click in *Terminal>Run Task...*, or press
`Ctrl` + `shift` + `P` and look for *"Tasks: Run Task"*. Execute them in this order:

 1) **Config profiles:** Configurate your conan profile for the project, specifying
     your C/C++ compiler version and the C++ standard.
 2) **Install dependencies:** Install all dependencies written in `conanfile.txt`.
 3) **CMake Config\*:** Configurate the CMake project in order to enhance
     intellisense and enable the building process. 
 4) **Build:** Build the project. Libraries will link statically.

__*__*If you are using a Windows environment it would may require to patch
SDL2_image target files inside the build directory using the
[corresponding script](../scripts/patch_sdl2_image.py).*

