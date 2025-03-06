#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the macos.platform module that gets the MacOS version. 
"""

import sys

class AnyOsDetector:
    def detect_os():
        if sys.platform.startswith("darwin"):
            return "MacOS"
        elif sys.platform.startswith("win"):
            return "Windows"
        elif sys.platform.startswith("linux"):
            return "Linux"
        else:
            return "Unknown"
        
if __name__ == '__main__':
    # Add the project root directory to the Python path
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    import utils.unit_test as utils

    utils.print_unit_test_header("detect_os")
    os = AnyOsDetector.detect_os()
    if os:
        print("OS:", os)
    else:
        print("This is not a known OS.")
