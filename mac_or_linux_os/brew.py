#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the maclinux.brew module that handles Homebrew actions. 
"""

import subprocess

class Brew:
    @staticmethod
    def get_homebrew_version():
        """
        Executes the 'brew --version' command and returns a dictionary with:
            - success: True if command succeeds, False otherwise.
            - stdout: Standard output from the command.
            - stderr: Standard error output from the command.
        """
        try:
            result = subprocess.run(
                ['brew', '--version'],
                capture_output=True,
                text=True,
                check=True
            )
            return {
                'success': True,
                'stdout': result.stdout.strip(),
                'stderr': result.stderr.strip()
            }
        except subprocess.CalledProcessError as e:
            return {
                'success': False,
                'stdout': e.stdout.strip() if e.stdout else "",
                'stderr': e.stderr.strip() if e.stderr else str(e)
            }

    @staticmethod
    def install_homebrew():
        """
        Runs the Homebrew installation script using the command:
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        Returns:
            A dictionary with the following keys:
                - success: True if the command executed successfully, False otherwise.
                - stdout: The standard output of the command (stripped).
                - stderr: The standard error output of the command (stripped).
        """
        command = ["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            return {
                "success": True,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip()
            }
        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "stdout": e.stdout.strip() if e.stdout else "",
                "stderr": e.stderr.strip() if e.stderr else str(e)
            }

if __name__ == '__main__':
    # Add the project root directory to the Python path
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    import utils.unit_test as utils

    utils.print_unit_test_header("Brew.get_homebrew_version")
    result = Brew.get_homebrew_version()
    if result["success"]:
        print("Homebrew version:", result["stdout"])
    else:
        print("Homebrew is not installed.")
        print("Error:", result["stderr"])

    utils.print_unit_test_header("Brew.install_homebrew")
    result = Brew.install_homebrew()
    if result["success"]:
        print("Homebrew installation initiated successfully.")
        print("Output:", result["stdout"])
    else:
        print("Homebrew installation failed.")
        print("Error:", result["stderr"])
