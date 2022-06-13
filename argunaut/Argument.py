"""
Data class for storing properties of an argument
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Argument():
    long_name: str
    required: bool = False
    arg_type: str = 'string'
    short_name: Optional[str] = None
    default_val: Optional[str] = None
    choices: Optional[list] = None
    help_msg: Optional[str] = None
    group_name: Optional[str] = None
    nargs: Optional[str] = None
