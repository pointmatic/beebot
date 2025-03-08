#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the beezeebot_cli module that handles command-line argument parsing and performs an appropriate action. 
"""

import argparse

from components.xcode import Xcode
from components.brew import Brew
from components.asdf import Asdf

# Homebrew
def get_brew_version_msg():
    """Get the version of the Homebrew utility."""
    result = Brew.get_homebrew_version()
    if result['success']:
        msg = "version: " + result['stdout']
    else:
        msg = "Homebrew is not installed. \nInstall using this command: beezeebot_cli.py -i brew"
    return msg

def install_brew():
    """Install the Homebrew utility."""
    print("Installing foo... (this is pseudocode for the installation process)")

# Xcode Command-Line Tools
def get_xcode_select_version_msg():
    """Get the version of the Xcode command-line interface tools utility."""
    result = Xcode.get_command_line_tools_version()
    if result['success']:
        msg = "version: " + result['stdout']
    else:
        msg = "Xcode command-line tools are not installed. \nInstall using this command: beezeebot_cli.py -i xcode-select"
    return msg

def install_xcode_select():
    """Install the Xcode command-line interface tools utility."""
    print("Installing Xcode command-line interface tools... (this is pseudocode for the installation process)")

def get_asdf_version_msg(): 
    """Get the version of the asdf programming language version manager."""
    result = Asdf.get_asdf_version()
    if result['success']:
        msg = "version: asdf " + result['stdout']
    else:
        msg = "asdf is not installed. \nInstall using this command: beezeebot_cli.py -i asdf"
    return msg

def install_asdf():
    """Install the asdf programming language version manager."""
    print("Installing asdf... (this is pseudocode for the installation process)")
    
# MacOS version
def get_macos_version_msg():
    """Get the version of the macOS operating system."""
    print("Getting macOS version... (this is pseudocode for the version check)")

# Options
def get_options_msg():
    """Lists the options of which utilities and applications are available."""
    options = [
        "  brew: Homebrew package manager",
        "  xcode-select: Xcode command-line tools",
        "  asdf: programming language version manager"
    ]
    msg = "Available options for --version and --install parameters:\n" + "\n".join(options)
    return msg

# Scan
def scan():
    """Scans the computer for installed utilities and applications."""
    print("Scanning for applications... (this is pseudocode for scanning)")

# Command-line argument parsing
def parse_command_line_args():
    """
    Parses command-line arguments and routes to the appropriate internal functions.
    
    Supported command-line arguments:
      -h, --help                 : Displays this help message.
      -i, --install APPLICATION  : Installs the specified utility or application.
      -v, --version APPLICATION  : Retrieves the version of the specified utility or application.
      -l, --list TYPE            : Lists either 'installed' utilities / applications, or the 'options' of which are available.
      -p, --plugin APPLICATION 
                   PLUGIN        : Installs the specified utility or app plugin.
    """
    parser = argparse.ArgumentParser(
        description="BeeZeeBot is an AI utility and application configurator. If you have ever tried to install an Ollama model and run a chat interface for the first time on your Mac, you know that it's a multi-step process with configuration and some technical decisions. Rather than all that hassle, BeeZeeBot will handle all the dependencies for you so you don't have to type in 15 command-line instructions just to get something installed and ready to use. Whether you're an experienced developer or you have no idea how to use the command line, BeeZeeBot is here to help you get set up with AI apps, data science tools, and it will even configure a software development environment for Python, Ruby, or C++ using VS Code."
    )
    
    # Create a mutually exclusive group so that only one of -i or -v is provided.
    group = parser.add_mutually_exclusive_group(required=False)

    group.add_argument(
        '-i', '--install',
        metavar='APPLICATION',
        help='Install the specified utility or application.'
    )
    group.add_argument(
        '-v', '--version',
        metavar='APPLICATION',
        help='Get the version of the specified utility or application.'
    )
    group.add_argument(
        '-p', '--plugin',
        nargs=2,
        metavar=('APPLICATION', 'PLUGIN'),
        help='Install the plugin for the specified utility or application.'
    )
    group.add_argument(
        '-o', '--options',
        action='store_true',
        help='Lists the options of which utilities and applications are available.'
    )
    group.add_argument(
        '-s', '--scan',
        action='store_true',
        help='Scans the computer for installed utilities and applications.'
    )
    
    args = parser.parse_args()
    
    # Route the command to the proper functions.
    if args.install:
        app = args.install.lower()
        if app == 'brew':
            install_brew()
        elif app == 'xcode-select':
            install_xcode_select()
        else:
            print(f"Installation function for '{app}' is not supported.")
    
    elif args.version:
        app = args.version.lower()
        if app == 'brew':
            print(get_brew_version_msg())
        elif app == 'xcode-select':
            print(get_xcode_select_version_msg())
        elif app == 'asdf':
            get_asdf_version_msg()
        elif app == 'macos':
            get_macos_version_msg()
        else:
            print(f"Version function for '{app}' is not supported.")

    elif args.plugin:
        app = args.plugin[0].lower()
        plugin = args.plugin[1].lower()
        if app == 'brew':
            install_brew_plugin(plugin)
        if app == 'asdf':
            install_brew_plugin(plugin)
        else:
            print(f"Installation function for '{app}' is not supported.")
    
    elif args.options:
            print(get_options_msg())

    elif args.scan:
            scan()        

    else:
        parser.print_help()

if __name__ == '__main__':
    parse_command_line_args()