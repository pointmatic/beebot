#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the macos package that contains modules for working with macOS-specific
functionality. The package contains the following modules:

    - xcode: Contains Xcode that handles checking for Xcode command line tools and installing them.
    - platform: Contains Platform that handles checking for the macOS version.
"""

# Import specific classes or functions from submodules
from .xcode import Xcode

# Define what is exported when 'from my_package import *' is used
__all__ = ['Xcode', 'platform']

# Optional: define package-level variables or initialization code
__version__ = '0.1.1'