import sys
from typing import List
import distutils.sysconfig
from os import path

try:
    import requests  # type: ignore
except ModuleNotFoundError:
    print('Please install requests package using: pip3 install requests')
    exit(1)


BINARIES_PATH = 'https://github.com/somik861/hpc-datastore-cpp-pybind/blob/main/binaries/'


def url_join(*args) -> str:
    final = ''
    for url in args:
        if not final.endswith('/') and final:
            final += '/'
        final += url

    return final


def get_files_url() -> List[str]:
    module_name = 'hpc_datastore'
    suffix: str = distutils.sysconfig.get_config_var('EXT_SUFFIX')
    file_name = module_name + suffix
    url = url_join(BINARIES_PATH, sys.platform, file_name)

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
            out.append(url_join(BINARIES_PATH, sys.platform, 'dlls', dll))

    return out


def download_files(urls: List[str], prefixes: List[str]) -> None:
    for url in urls:
        filename = url.split('/')[-1]
        print(f"Downloading {filename} ... ", end='', flush=True)

        full_url = url + '?raw=true'
        req = requests.get(full_url)
        for prefix in prefixes:
            open(path.join(prefix, filename), 'wb').write(req.content)

        print("[OK]")


def main():

    urls = get_files_url()
    if not urls:
        print("Your system is not supported")
        exit(1)

    prefixes: list[str] = []

    if len(sys.argv) == 1:
        for syspath in sys.path:
            if 'dynload' in syspath:
                prefixes.append(syspath)
                break

    prefixes.extend(sys.argv[1:])

    download_files(urls, prefixes)


if __name__ == '__main__':
    main()
