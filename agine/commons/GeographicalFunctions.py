# -*- encoding: utf-8 -*-

import pyproj
from shapely import geometry
from functools import partial
from shapely.ops import transform
from shapely.geometry import Point, Polygon

from ..config import DATUM

# Check https://gis.stackexchange.com/questions/121256/ and
# Check https://gis.stackexchange.com/questions/289044/ for More Information
# NOTE : this converts everything into 'm'

def create_circle_polygon(centerLon : int or float, centerLat : int or float, radius : int or float = 10000) -> Polygon:
	'''Create a Circle from the given [longitude, latitude] with the given Radius

	: param centerLat : Center Latitude - in WGS84
	: param centerLon : Center Longitude - in WGS84

	: param radius    : Radius of the Circle, in 'm' ONLY. Default 10000 = 10 km

	Returns shapely.Polygon Object
	'''
	local_azimuthal_projection = f"+proj=aeqd +R=6371000 +units=m +lat_0={centerLat} +lon_0={centerLon}"

	WGS84_to_AEQD = partial( # AEQD = Azimuthal Equidistance Projection
			pyproj.transform,
			pyproj.Proj(local_azimuthal_projection),
			pyproj.Proj(f"+proj=longlat +datum={DATUM} +no_defs")
		)

	AEQD_to_WGS84 = partial(
			pyproj.transform,
			pyproj.Proj(local_azimuthal_projection),
			pyproj.Proj(f"+proj=longlat +datum={DATUM} +no_defs")
		)

	point = Point(float(centerLon), float(centerLat)) # Center-Point
	point = transform(WGS84_to_AEQD, point)

	circular_poly = point.buffer(radius)
	circular_poly = transform(AEQD_to_WGS84, circular_poly)

	return circular_poly