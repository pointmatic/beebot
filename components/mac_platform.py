#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the components.mac_platform module that gets the MacOS version. 
"""

import platform

class MacPlatform:
    @staticmethod
    def get_macos_version():
        """
        Returns the macOS version as a string.
        platform.mac_ver() returns a tuple like ('10.15.7', ('', '', ''), 'x86_64')
        """
        version = platform.mac_ver()[0]
        return version

if __name__ == '__main__':
    # Add the project root directory to the Python path
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    import utils.unit_test as utils

    utils.print_unit_test_header("get_macos_version")
    version = MacPlatform.get_macos_version()
    if version:
        print("macOS version:", version)
    else:
        print("This is not a macOS system or the version could not be determined.")
