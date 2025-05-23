from shapely.geometry import MultiPoint
import numpy as np

def get_valid_data_frame(data_array, level_idx=(0, 0)):
    """
    Computes a convex hull polygon around valid (non-NaN) data points 
    in an xarray DataArray with shape [eps, ref_time, y, x].

    Parameters:
    - data_array: xarray.DataArray
    - level_idx: tuple, index to select the 2D slice (e.g., (0, 0) for [eps, ref_time])

    Returns:
    - frame_polygon: shapely.geometry.Polygon or None
    """
    data_2d = data_array.values[level_idx[0], level_idx[1]]
    valid_mask = ~np.isnan(data_2d)

    lat = data_array.lat.values
    lon = data_array.lon.values

    valid_lat = lat[valid_mask]
    valid_lon = lon[valid_mask]

    if len(valid_lat) < 3:
        return None  # Can't create a polygon with fewer than 3 points
    points = MultiPoint(list(zip(valid_lon, valid_lat)))
    return points.convex_hull
