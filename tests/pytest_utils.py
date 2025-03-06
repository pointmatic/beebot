#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

Support functions for pytest. 

Helper Classes:
    - FakeCompletedProcessOutput: encapsulates mock output.

Helper Functions:
    - fake_run_failure() has a consistent output

Inline Functions:
    - There are custome versions of fake_run_success() functions are defined inline for each function needed.

"""


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

