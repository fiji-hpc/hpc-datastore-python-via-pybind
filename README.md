# HPC Datastore CPP - pybind

## Introduction
This project contains python bindings for HPC Datastore CPP. 

## Binaries
In binaries folder, you can find pre-compiled binaries. Most of the time, this is what you need as there is pretty
much no point in building them from source. Make sure to select your binary correctly, that is, check your OS and python version,
otherwise, you will not be able to import the module. In some special cases, where there is binary satisfying your needs, 
you also have an option do build module from source. That way, you can be sure that the module will work on your machine.
I will try to make sure, that binaries are recompiled for every bigger update.

### Linux
To use prebuilt library on linux, simply download corresponding file from [binaries/linux](binaries/linux), place it into your project
and import it as usual (`import hpc_datastore`).

### Windows
To use prebuilt library on windows, download library file from [binaries/windows](binaries/windows) and place it into your project.
You will also need all DLLs located at [binaries/windows/dlls](binaries/windows/dlls). Place DDLs into the same directory as downloaded binary.
It is reccommended to put binary with DLLs into subfolder. If you want pack more binaries into your project (e. g. for compatibilty), you can place all of them into one subfolder (DLLs will be shared). After all of that, import library as usual (`import hpc_datastore`).

## Installation
Download (or build) module and insert it into your python project. If you have got correct binary, you shall be able to 
import module just like any other, that is: **import hpc_datastore**

## Building from source
It is important to mention, that project is using C++20 and you will need *gcc-11.3.0* or newer (*gcc-12.1.0* is also fine).
I did not test *clang++*.

To obtain all sources, run `git submodule update --init`.

Make sure you have working [vcpkg](https://github.com/microsoft/vcpkg-tool) installation. Everything except *i3d library* 
will  be downloaded through vcpkg. There are also static versions of *i3d library*, so you will most likely need not to 
install *i3d library* at all. 

If you have prerequesities, create `build` folder and inside run:
```bash
cmake -DCMAKE_TOOCHAIN_FILE=<vcpkg>/scripts/buildsystems/vcpkg.cmake ../
```
(Make sure to replace <vcpkg> with path to your vcpkg installation.)

And then simply `make`.

## All Build scripts
These scripts are developer-friendly scripts that use *anaconda* to create all necessary python enviromnents and compile
all needed binaries in one click. These scripts are used for generating provided binaries and you do not need to worry about them.
(On the other hand, if you still want to use them, make sure to *source* them inside your bash shell, otherwise anaconda
eviromnent will not be functional). 

## Redistribution with project
You will ofcourse need to ship binaries with your project (Or you can create a script that downloads your need binaries depending on your system). Pre-build binaries are built with older system in mind, so you should have no problems using them on not-ancient.
