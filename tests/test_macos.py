#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the test module that determines if the macos package is working correctly. The module contains the following classes:

    - test_macos: Contains Xcode that handles checking for Xcode command line tools and installing them.\
"""

import subprocess
import pytest
from macos.xcode import Xcode

# Helper class to simulate subprocess.CompletedProcess
class FakeCompletedProcess:
    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr

# Fake subprocess.run function simulating successful execution.
def fake_run_success(args, capture_output, text, check):
    # Simulate a successful execution returning a version string.
    return FakeCompletedProcess("xcode-select version 2395", "")

# Fake subprocess.run function simulating a command failure.
def fake_run_failure(args, capture_output, text, check):
    raise subprocess.CalledProcessError(
        returncode=1,
        cmd=args,
        output="",
        stderr="Command failed"
    )

def test_get_command_line_tools_version_success(monkeypatch):
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

def test_install_command_line_tools_success(monkeypatch):
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
