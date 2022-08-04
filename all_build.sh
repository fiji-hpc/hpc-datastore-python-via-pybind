#! /bin/bash

VCPKG_PATH="${1}"
REMOVE="${2}"

# python version
function ensure_env
{
    if ! conda env list | grep "^__${1} " 
    then
        conda create -y -n "__${1}" python=${1}
    fi
}

# python version
function remove_env
{
    if  conda env list | grep "^__${1} "
    then
        conda env remove -y -n "__${1}"
    fi
}
# python version 
function build_version 
{
    rm -rf build_all
    mkdir build_all
    cd build_all
    conda activate "__${1}"

    cmake -DCMAKE_TOOLCHAIN_FILE="${VCPKG_PATH}" -DPYBIND11_PYTHON_VERSION=${1} ../
    make

    mkdir -p ../build_binaries
    mv *.so ../build_binaries

    conda deactivate
    cd ..
    rm -rf build_all
}

PY_VERSIONS="3.6 3.7 3.8 3.9 3.10"

for VER in $PY_VERSIONS
do
    echo "Building version: ${VER}"
    ensure_env ${VER}
    build_version ${VER}

    if [ "${REMOVE}" = "YES" ]
    then
        remove_env ${VER}
    fi
done


