# coding: utf-8
"""
This module contains event manager for the current platform.
"""


# Local imports
from .compat import IS_LINUX
from .compat import IS_MACOS
from .compat import IS_WINOS
from .compat import UNSUPPORTED_PLATFORM_ERROR


# If the platform is Linux
if IS_LINUX:
    # Use event manager for Linux
    from .event_manager_x11 import EventManager

# If the platform is MacOS
elif IS_MACOS:
    # Use event manager for MACOS
    from .event_manager_macos import EventManager

# If the platform is Windows
elif IS_WINOS:
    # Use event manager for Windows
    from .event_manager_windows import EventManager

# If the platform is none of above
else:
    # Raise error
    raise UNSUPPORTED_PLATFORM_ERROR


# Suppress linter error
EventManager = EventManager
