#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the xcode module that handles checking for Xcode command line tools and installing them.
"""

import subprocess

class Xcode:
    @staticmethod
    def get_command_line_tools_version():
        """
        Executes the 'xcode-select --version' command and returns a dictionary with:
            - success: True if command succeeds, False otherwise.
            - stdout: Standard output from the command.
            - stderr: Standard error output from the command.
        """
        try:
            result = subprocess.run(
                ['xcode-select', '--version'],
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
    def install_command_line_tools():
        """
        Attempts to install the Xcode Command Line Tools by running the 'xcode-select --install' command.
        Returns a dictionary with:
            - success: True if the installation process was initiated successfully, False otherwise.
            - stdout: Standard output from the command.
            - stderr: Standard error output from the command.
        """
        try:
            result = subprocess.run(
                ['xcode-select', '--install'],
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
    def list_software_updates():
        """
        Lists available MacOS software updates using the 'softwareupdate -l' command.

        Returns:
            A dict with keys:
                - success: True if the command succeeds, False otherwise.
                - stdout: Standard output (stripped).
                - stderr: Standard error (stripped).

            Note: 
                - The 'softwareupdate -l' command requires root privileges to run successfully.
                - The output may vary based on the system's current state. 
                - The command may take some time to complete.
                - The error message will contain the "No new software available." message if no updates are available.
                - There appears to be a way to install updates according to the help list (softwareupdate --help).
                - UNKNOWN: where the output for available updates will go (possibly stderr).
        """
        try:
            result = subprocess.run(
                ['softwareupdate', '-l'],
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
    def list_software_updates_history():
        """
        List historical MacOS software updates using the 'softwareupdate --history' command.

        Returns:
            A dict with keys:
                - success: True if the command succeeds, False otherwise.
                - stdout: Standard output (stripped).
                - stderr: Standard error (stripped).

            Note: 
                - The 'softwareupdate -l' command requires root privileges to run successfully.
                - The output may vary based on the system's current state. 
                - The command may take some time to complete.
                - The error message will contain the "No new software available." message if no updates are available.
                - There appears to be a way to install updates according to the help list (softwareupdate --help).
                - UNKNOWN: where the output for available updates will go (possibly stderr).
        """
        try:
            result = subprocess.run(
                ['softwareupdate', '--history'],
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

# unit tests
def print_unit_test_header(name):
    print("\n=====================================================================================================")
    print("Unit Test: ", name)
    print("=====================================================================================================")

if __name__ == '__main__':
    # Check for, and if necessary, install the Xcode Command Line Tools version.
    print_unit_test_header("get_command_line_tools_version")
    version_info = Xcode.get_command_line_tools_version()
    if version_info['success']:
        print("Xcode Command Line Tools version:", version_info['stdout'])
    else:
        print_unit_test_header("install_command_line_tools")
        print("Xcode Command Line Tools not installed. Attempting installation...")
        install_info = Xcode.install_command_line_tools()
        if install_info['success']:
            print("Installation initiated successfully. Please follow the GUI prompts.")
        else:
            print("Failed to initiate installation. Error details:", install_info['stderr'])

    # List available macOS software updates.
    print_unit_test_header("list_software_updates")
    updates_info = Xcode.list_software_updates()
    if updates_info['success']:
        print(updates_info['stdout'])
        print(updates_info['stderr'])
    else:
        print("Failed to list software updates. Error details:", updates_info['stderr'])

    # List historical macOS software updates.
    print_unit_test_header("list_software_updates_history")
    history_info = Xcode.list_software_updates_history()
    if history_info['success']:
        print("Software updates history:")
        print(history_info['stdout'])
    else:
        print("Failed to list software updates history. Error details:", history_info['stderr'])
