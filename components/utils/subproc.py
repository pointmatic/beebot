#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the components.subproc module that manages shell actions. 
"""

import subprocess

class Subproc:
    @staticmethod
    def run_command(command):
        """
        Executes the specified command (string or list) and returns a dictionary with:
            - success: True if command succeeds, False otherwise.
            - stdout: Standard output from the command.
            - stderr: Standard error output from the command.
        """
        try:
            result = subprocess.run(
                command,
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
