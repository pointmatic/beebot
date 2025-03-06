#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the beezeebot_cli module that handles command-line argument parsing and performs an appropriate action. 
"""

import argparse

# Homebrew
def get_brew_version():
    """Get the version of the Homebrew utility."""
    print("Getting version of Homebrew... (this is pseudocode for the version check)")
def install_brew():
    """Install the Homebrew utility."""
    print("Installing foo... (this is pseudocode for the installation process)")

# Xcode Command-Line Tools
def get_xcode_select_version():
    """Get the version of the Xcode command-line interface tools utility."""
    print("Getting version of Xcode command-line interface tools... (this is pseudocode for the version check)")
def install_xcode_select():
    """Install the Xcode command-line interface tools utility."""
    print("Installing Xcode command-line interface tools... (this is pseudocode for the installation process)")

# MacOS version
def get_macos_version():
    """Get the version of the macOS operating system."""
    print("Getting macOS version... (this is pseudocode for the version check)")

# Options
def get_options():
    """Lists the options of which utilities and applications are available."""
    print("Listing the options... (this is pseudocode for options)")

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
            get_brew_version()
        elif app == 'xcode-select':
            get_xcode_select_version()        
        else:
            print(f"Version function for '{app}' is not supported.")

    elif args.options:
            get_options()        

    elif args.scan:
            scan()        

    else:
        parser.print_help()

if __name__ == '__main__':
    parse_command_line_args()