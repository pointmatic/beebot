#!/bin/bash
#
# Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)
#
# This source code is licensed under the Mozilla Public License Version 2.0 found in the
# LICENSE file in the root directory of this source tree.
#
#============================================================================================================================================================================================
#
# This is the utils.unit_test module with helper funtions for direct unit tests with code.

# Remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -r {} +

# Remove .egg-info directories
find . -type d -name "*.egg-info" -exec rm -r {} +

# Remove build directories
find . -type d -name "build" -exec rm -r {} +

# Remove dist directories
find . -type d -name "dist" -exec rm -r {} +

echo "Cleanup complete."