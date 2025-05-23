import numpy as np
from shapely.geometry import MultiPoint

def get_valid_data_frame(data_array):
    """
    Computes a polygon around valid (non-NaN) data points 
    in an xarray.DataArray using dimensions 'x' and 'y'.

    Parameters:
    - data_array: xarray.DataArray with dimensions including 'x' and 'y'

    Returns:
    - frame_polygon: shapely.geometry.Polygon or None
    """
    # Select just the 2D spatial slice (last over x/y, squeeze all others)
    data_2d = data_array.sel(x=data_array.x, y=data_array.y).squeeze()

    if data_2d.ndim != 2:
        raise ValueError("Data must be 2D after squeezing non-x/y dimensions.")

    valid_mask = ~np.isnan(data_2d.values)

    lat = data_array.lat.values
    lon = data_array.lon.values

    valid_lat = lat[valid_mask]
    valid_lon = lon[valid_mask]

    if len(valid_lat) < 3:
        return None  # Not enough valid points for a polygon

    points = MultiPoint(list(zip(valid_lon, valid_lat)))
    return points.convex_hull
