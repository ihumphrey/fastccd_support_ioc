#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from . import cin_functions
from . import cin_register_map

# Clear the Focus bit
cin_functions.clearFocusBit()

# Set Number of Exposures to value = 0000
cin_functions.WriteReg(cin_register_map.REG_NUMBEROFEXPOSURE_REG, "0000", 1)

# Set the Focus bit
cin_functions.setFocusBit()

# Start Triggers
cin_functions.WriteReg("8001", "0100", 1)
