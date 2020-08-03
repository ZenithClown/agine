# -*- encoding: utf-8 -*-

"""API is useful for (1) Exposing Functionalities, with init-time Option Registrations, and (2) Setting up agine-Environment"""

# (2) agine-Environment Setup
from .OSOptions import OSOptions
AVLBL_OPTIONS = OSOptions.module_functionality()
print(f'\tDetected OS            : {OSOptions.OSName}-{OSOptions.OSVersion}')
print(f'\tscikit-learn Options   : {OSOptions.is_sklearn_available}')
print(f'\tThreading Availibilty  : {OSOptions.is_threading_possible}')
print(f'\tTensorflow Availibilty : {OSOptions.is_tensorflow_available}')

# (1) init-Time Option Registrations
from ..commons import * # this is alaways Available!

if 'point-function' in AVLBL_OPTIONS:
	from ..core.point_function import *
	from ..commons.GeographicalFunctions import * # though this is under commons, but requires Shapely and pyProj for Operations

if 'line-of-sight' in AVLBL_OPTIONS:
	pass