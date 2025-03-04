#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the pytest test module that determines if the macos package is working correctly. 

Helper Classes:
    - FakeCompletedProcessOutput: encapsulates mock output.

Helper Functions:
    - fake_run_failure() has a consistent output

Inline Functions:
    - There are custome versions of fake_run_success() functions are defined inline for each test function.

"""

import subprocess
import pytest
from macos.xcode import Xcode

# Helper class to simulate subprocess.CompletedProcess
class FakeCompletedProcessOutput:
    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr

# Helper functions
def fake_run_failure(args, capture_output, text, check):
    # Simulate a failed execution.
    raise subprocess.CalledProcessError(
        returncode=1,
        cmd=args,
        output="",
        stderr="Command failed"
    )


# Test functions

def test_get_command_line_tools_version_success(monkeypatch):
    def fake_run_success(args, capture_output, text, check):
        # Simulate a successful execution returning a version string.
        return FakeCompletedProcessOutput("xcode-select version 2395", "")

    # Replace subprocess.run with our fake success function.
    monkeypatch.setattr(subprocess, "run", fake_run_success)
    result = Xcode.get_command_line_tools_version()
    assert result["success"] is True
    assert result["stdout"] == "xcode-select version 2395"
    assert result["stderr"] == ""

def test_get_command_line_tools_version_failure(monkeypatch):
    # Replace subprocess.run with our fake failure function.
    monkeypatch.setattr(subprocess, "run", fake_run_failure)
    result = Xcode.get_command_line_tools_version()
    assert result["success"] is False
    assert result["stdout"] == ""
    assert "Command failed" in result["stderr"]

'''
NOTE: we do not know the exact output of the 'xcode-select --install' command, so we cannot simulate it.
def test_install_command_line_tools_success(monkeypatch):
    def fake_run_success(args, capture_output, text, check):
        # Simulate a successful execution returning a version string.
        return FakeCompletedProcessOutput("xcode-select version 2395", "")

    # Test installation method with a simulated successful execution.
    monkeypatch.setattr(subprocess, "run", fake_run_success)
    result = Xcode.install_command_line_tools()
    assert result["success"] is True
    assert result["stdout"] == "xcode-select version 2395"
    assert result["stderr"] == ""

def test_install_command_line_tools_failure(monkeypatch):
    # Test installation method with a simulated failure.
    monkeypatch.setattr(subprocess, "run", fake_run_failure)
    result = Xcode.install_command_line_tools()
    assert result["success"] is False
    assert result["stdout"] == ""
    assert "Command failed" in result["stderr"]
'''

def test_list_software_updates_success_no_updates(monkeypatch):
    def fake_run_success(args, capture_output, text, check):
        # Simulate a successful execution returning a version string.
        return FakeCompletedProcessOutput("Software Update Tool\n\nFinding available software", "No new software available.")

    # Simulate a successful software update list with no updates.
    monkeypatch.setattr(subprocess, "run", fake_run_success)
    result = Xcode.list_software_updates()
    # Note: The fake success function returns the same output as for xcode-select.
    assert result["success"] is True
    assert result["stdout"] == "Software Update Tool\n\nFinding available software"
    assert result["stderr"] == "No new software available."

'''
NOTE: we do not know the exact output of the 'softwareupdate --list' command when there are updates, so we cannot simulate it.
def test_list_software_updates_success_updates(monkeypatch):
    def fake_run_success(args, capture_output, text, check):
        # Simulate a successful execution returning a version string.
        return FakeCompletedProcessOutput("Software Update Tool\n\nFinding available software", "???TBD???")

    # Simulate a successful software update list with one or more updates.
    monkeypatch.setattr(subprocess, "run", fake_run_success)
    result = Xcode.list_software_updates()
    # Note: The fake success function returns the same output as for xcode-select.
    assert result["success"] is True
    assert result["stdout"] == "Software Update Tool\n\nFinding available software"
    assert result["stderr"] == "???TBD???"
'''

def test_list_software_updates_failure(monkeypatch):       
    # Simulate a failure in checking software updates.
    monkeypatch.setattr(subprocess, "run", fake_run_failure)
    result = Xcode.list_software_updates()
    assert result["success"] is False
    assert result["stdout"] == ""
    assert "Command failed" in result["stderr"]

def test_list_software_updates_history_success(monkeypatch):
    def fake_run_success(args, capture_output, text, check):
        # Simulate a successful execution returning a version string.
        return FakeCompletedProcessOutput("Display Name                                       Version    Date                  \n------------                                       -------    ----                  \nmacOS Sonoma 14.5                                  14.5       05/21/2024, 18:55:51  \nCommand Line Tools for Xcode                       15.3       06/20/2024, 22:46:56  \nmacOS Sonoma 14.6.1                                14.6.1     08/15/2024, 14:55:24  \nmacOS Sequoia 15.0.1                               15.0.1     10/07/2024, 01:33:24  \nCommand Line Tools for Xcode                       16.0       10/09/2024, 20:29:31  \nCommand Line Tools for Xcode                       16.1       11/05/2024, 16:39:56  \nmacOS Sequoia 15.1                                 15.1       11/05/2024, 16:41:08  \nmacOS Sequoia 15.1.1                               15.1.1     11/22/2024, 09:44:22  \nCommand Line Tools for Xcode                       16.2       12/30/2024, 14:14:11  \nmacOS Sequoia 15.2                                 15.2       12/30/2024, 14:15:27  \nmacOS Sequoia 15.3                                 15.3       02/07/2025, 12:31:47  \nmacOS Sequoia 15.3.1                               15.3.1     02/20/2025, 02:19:30", "")

    # Simulate a successful software update check.
    monkeypatch.setattr(subprocess, "run", fake_run_success)
    result = Xcode.list_software_updates_history()
    # Note: The fake success function returns the same output as for xcode-select.
    assert result["success"] is True
    assert result["stdout"] == "Display Name                                       Version    Date                  \n------------                                       -------    ----                  \nmacOS Sonoma 14.5                                  14.5       05/21/2024, 18:55:51  \nCommand Line Tools for Xcode                       15.3       06/20/2024, 22:46:56  \nmacOS Sonoma 14.6.1                                14.6.1     08/15/2024, 14:55:24  \nmacOS Sequoia 15.0.1                               15.0.1     10/07/2024, 01:33:24  \nCommand Line Tools for Xcode                       16.0       10/09/2024, 20:29:31  \nCommand Line Tools for Xcode                       16.1       11/05/2024, 16:39:56  \nmacOS Sequoia 15.1                                 15.1       11/05/2024, 16:41:08  \nmacOS Sequoia 15.1.1                               15.1.1     11/22/2024, 09:44:22  \nCommand Line Tools for Xcode                       16.2       12/30/2024, 14:14:11  \nmacOS Sequoia 15.2                                 15.2       12/30/2024, 14:15:27  \nmacOS Sequoia 15.3                                 15.3       02/07/2025, 12:31:47  \nmacOS Sequoia 15.3.1                               15.3.1     02/20/2025, 02:19:30"
    assert result["stderr"] == ""

def test_list_software_updates_history_failure(monkeypatch):
    # Simulate a failure in checking software updates.
    monkeypatch.setattr(subprocess, "run", fake_run_failure)
    result = Xcode.list_software_updates_history()
    assert result["success"] is False
    assert result["stdout"] == ""
    assert "Command failed" in result["stderr"]
