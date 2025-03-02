#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import subprocess

class Xcode:
    @staticmethod
    def get_command_line_tools_version():
        """
        Executes the 'xcode-select --version' command to check if the Xcode command-line tools are installed.
        Returns:
            A string representing the version number (and associated text) if the command succeeds,
            or None if an error occurs.
        """
        try:
            # Run the command and capture the output
            result = subprocess.run(
                ['xcode-select', '--version'],
                capture_output=True,  # Capture both stdout and stderr
                text=True,            # Return output as a string
                check=True            # Raise an exception if the command fails
            )
            # Return the output (e.g., "xcode-select version 2395.")
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            # Return None if an error occurs
            return None

if __name__ == '__main__':
    version = Xcode.get_command_line_tools_version()
    if version:
        print("Xcode Command Line Tools version:", version)
    else:
        print("Failed to retrieve the version.")