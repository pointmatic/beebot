#!/usr/bin/env python3
"""
Copyright (c) 2025 Pointmatic, (https://www.pointmatic.com)

This source code is licensed under the Mozilla Public License Version 2.0 found in the
LICENSE file in the root directory of this source tree.

============================================================================================================================================================================================

This is the components.installable_component, the abstract class for all installable components.
"""

from abc import ABC, abstractmethod

class InstallableComponent(ABC):
    @abstractmethod
    def install(self):
        """Install the component."""
        pass

    @abstractmethod
    def uninstall(self):
        """Uninstall the component."""
        pass

    @abstractmethod
    def check_version(self):
        """Check the component's version."""
        pass
