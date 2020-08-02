# -*- encoding: utf-8 -*-

"""API is useful for (1) Exposing Functionalities, with init-time Option Registrations, and (2) Setting up agine-Environment"""

# (2) agine-Environment Setup
from .OSOptions import OSOptions
AVLBL_OPTIONS = OSOptions.module_functionality()
print(f'\tDetected OS            : {OSOptions.OSName}-{OSOptions.OSVersion}')
print(f'\tThreading Availibilty  : {OSOptions.is_threading_possible}')
print(f'\tTensorflow Availibilty : {OSOptions.is_tensorflow_available}')

# (1) init-Time Option Registrations
from ..commons import * # this is alaways Available!

if 'point-function' in AVLBL_OPTIONS:
	pass

if 'line-of-sight' in AVLBL_OPTIONS:
	pass