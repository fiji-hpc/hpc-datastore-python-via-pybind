# HPC Datastore CPP - pybind

## Introduction
This project contains python bindings for HPC Datastore CPP. 

## Binaries
In binaries folder, you can find pre-compiled binaries. Most of the time, this is what you need as there is pretty
much no point in building them from source. Make sure to select your binary correctly, that is, check your OS and python version,
otherwise, you will not be able to import the module. In some special cases, where there is binary satisfying your needs, 
you also have an option do build module from source. That way, you can be sure that the module will work on your machine.
I will try to make sure, that binaries are recompiled for every bigger update.

## Installation
Download (or build) module and insert it into your python project. If you have got correct binary, you shall be able to 
import module just like any other, that is: **import hpc_datastore**

## Building from source
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
