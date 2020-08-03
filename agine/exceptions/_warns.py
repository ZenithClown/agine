# -*- encoding: utf-8 -*-

import warnings

class LimitedFunctionality(Warning):
	"""Warning is Raised when Limited-Working Functionality is Available"""

class TypeWarning(Warning):
	"""Warning is Raised if any of the argument-type is Wrong, but can be Fixed"""

class EncounteredNaN(Warning):
	"""Warning if data contains NaN Values"""

class DuplicateRecords(Warning):
	"""Warning is raised if DataFrame contains Duplicate Records"""

class ZeroDistanceNeighbor(Warning):
	"""Warning is Raised if the Neighbor is at 0 units Distance from Parent"""