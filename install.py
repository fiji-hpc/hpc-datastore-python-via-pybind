import sys
from typing import List
import distutils.sysconfig
import requests  # type: ignore
from os import path

BINARIES_PATH = 'https://github.com/somik861/hpc-datastore-cpp-pybind/tree/main/binaries'


def get_files_url() -> List[str]:
    module_name = 'hpc_datastore'
    suffix: str = distutils.sysconfig.get_config_var('EXT_SUFFIX')
    file_name = module_name + suffix
    url = path.join(BINARIES_PATH, sys.platform, file_name)

    req = requests.get(url)
    if (req.status_code == 404):
        return []

    out: List[str] = [url]

    if sys.platform == 'win32':
        for dll in [
            'PocoFoundation.dll',
            'PocoJSON.dll',
            'PocoNet.dll',
            'cbia.lib.i3dalgo.dyn.rel.x64.16.dll',
            'cbia.lib.i3dalgo.dyn.rel.x64.16.dll',
            'fmt.dll',
            'hdf5.dll',
            'hdf5_hl.dll',
            'jpeg62.dll',
            'libics.dll',
            'liblzma.dll',
            'libpng16.dll',
            'pcre.dll',
            'rxspencer.dll',
            'tiff.dll',
            'zlib1.dll',
        ]:
            out.append(path.join(BINARIES_PATH, sys.platform, 'dlls', dll))

    return out


def main():
    urls = get_files_url()
    if not urls:
        print("Your system is not supported")
        exit(1)


if __name__ == '__main__':
    main()
