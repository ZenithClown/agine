# -*- encoding: utf-8 -*-

import warnings
from platform import system, release

from ..exceptions import LimitedFunctionality

def check_imports(module_names):
	_unavailable = []
	for i in module_names:
		try:
			__import__(i)
		except ImportError:
			_unavailable.append(i)

	return _unavailable

class _env_setup:
	"""Sets the OS-Options"""
	def __init__(self):
		self.OSName    = system()
		self.OSVersion = release()

	@property
	def is_threading_possible(self):
		if 'lin' in self.OSName.lower():
			return True
		elif 'darwin' in self.OSName.lower():
			return True
		else:
			return False # Multi-Threading Creates problem in Windows-Environment

	@property
	def is_tensorflow_available(self):
		try:
			__import__('tensorflow')
			return True
		except ImportError:
			return False

	def module_functionality(self):
		__global_options__ = ['point-function', 'line-of-sight']
		# Check what are the available pkgs - on which global-functionality is set
		point_func = ['pandas', 'fiona', 'shapely', 'geopandas']
		line_of_st = ['rasterio']

		AVLBL_OPTIONS = ['commons']
		for opts, libs in zip(__global_options__, [point_func, line_of_st]):
			_check = check_imports(libs)
			if not _check:
				AVLBL_OPTIONS.append(opts)
			else:
				warnings.warn(f"{opts} Functionality is NOT Available, as {_check} are Required.", LimitedFunctionality)
				_input = input('Do you want to Continue? (Y/n) ')
				if (_input == 'n') or (_input == 'N'):
					raise ImportError(f'{_check} required for {opts}')

		return AVLBL_OPTIONS

OSOptions = _env_setup() # Create a Object - that can be accessed from Everywhere!