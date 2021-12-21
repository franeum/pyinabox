#!/usr/bin/env python3

import sys
import subprocess

PY_EXECUTABLE = sys.executable


def install_package(package_name, upgrade=False):
    args = [PY_EXECUTABLE, '-m', 'pip', 'install', package_name]

    if upgrade:
        args.append('--upgrade')

    res = subprocess.check_call(args)
    return res == 0


if __name__ == '__main__':
    install_package('pip', True)
    install_package('serial')
    install_package('esptool')
