#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the components.brew module that handles Homebrew actions. 
"""

from components.subproc import Subproc

class Asdf:
    # asdf plugins
    PLUGINS = ["python", "nodejs", "ruby"]

    @staticmethod
    def get_asdf_version():
        """
        Executes the 'asdf --version' command and returns a dictionary with:
            - success: True if command succeeds, False otherwise.
            - stdout: Standard output from the command.
            - stderr: Standard error output from the command.
        """ 

        result = Subproc.run_command(['asdf', '--version'])
        return result

    @staticmethod
    def get_plugin_versions(plugin_name):
        """
        Executes the 'asdf <plugin_name> list' command and returns a dictionary with:
            - success: True if command succeeds, False otherwise.
            - stdout: Standard output from the command.
            - stderr: Standard error output from the command.
        """ 

        result = Subproc.run_command(['asdf', plugin_name, 'list'])
        return result

    @staticmethod
    def install_plugin(plugin_name, version=None):
        """
        Performs asdf plugin installation using the command:
            asdf install <plugin_name> <version>
        
        Returns:
            A dictionary with the following keys:
                - success: True if the command executed successfully, False otherwise.
                - stdout: The standard output of the command (stripped).
                - stderr: The standard error output of the command (stripped).
        """

        if plugin_name not in Asdf.PLUGINS:
            return {
                "success": False,
                "stdout": "",
                "stderr": f"Plugin '{plugin_name}' not found in the list of available plugins."
            }
        
        command = ["asdf", "install", plugin_name]
        result = Subproc.run_command(command)
        return result
    
