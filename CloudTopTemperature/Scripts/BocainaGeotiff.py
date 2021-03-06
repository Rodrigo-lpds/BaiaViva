#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/home/cendas/miniconda3/envs/DataEnv/bin/python3
#=========================# Required libraries ===========================================================
import sys # Import the "system specific parameters and functions" module
# Import the NetCDF Python interface
from netCDF4 import Dataset 
# Import the Matplotlib package
import matplotlib 
import matplotlib.pyplot as plt # Collection of functions that make matplotlib work like MATLAB
from mpl_toolkits.basemap import Basemap # Import the Basemap toolkit
from matplotlib.colors import LinearSegmentedColormap # Linear interpolation for color maps
from matplotlib.patches import Rectangle # Library to draw rectangles on the plot
#Import the Numpy package
import numpy as np 
from numpy.ma import masked_array
# Add the GDAL library
from osgeo import gdal
# Import local functions
from remap import remap # Import the Remap function
from cpt_convert import loadCPT # Import the CPT convert function
#======================================================================================================
# Load the Data =======================================================================================
# Path to the GOES-16 image file
path = sys.argv[1]
# Open the file using the NetCDF4 library
nc = Dataset(path)
#======================================================================================================
# Get the latitude and longitude image bounds
geo_extent = nc.variables['geospatial_lat_lon_extent']
min_lon = float(geo_extent.geospatial_westbound_longitude)
max_lon = float(geo_extent.geospatial_eastbound_longitude)
min_lat = float(geo_extent.geospatial_southbound_latitude)
max_lat = float(geo_extent.geospatial_northbound_latitude)
# Bocaina as a Center of the projection
degrees = 0
# Choose the visualization extent (min lon, min lat, max lon, max lat)
extent = [-47 - degrees ,-25 - degrees,-42+ degrees,-20 + degrees] #Bocaina
#extent = [-44 - degrees ,-27 - degrees,-38+ degrees,-21 + degrees] #Regiao Norte Fluminense
# Choose the image resolution (the higher the number the faster the processing is)
resolution = 2 
# Calculate the image extent required for the reprojection
H = nc.variables['goes_imager_projection'].perspective_point_height
x1 = nc.variables['x_image_bounds'][0] * H 
x2 = nc.variables['x_image_bounds'][1] * H 
y1 = nc.variables['y_image_bounds'][1] * H 
y2 = nc.variables['y_image_bounds'][0] * H 
Start = (path[path.find("_s")+2:path.find("_e")])
# Call the reprojection funcion
grid = remap(path, extent, resolution,  x1, y1, x2, y2)
# Read the data returned by the function ==============================================================
# If it is an IR channel subtract 273.15 to convert to ° Celsius
data = grid.ReadAsArray() - 273.15
# Make pixels outside the footprint invisible
data[data <= -180] = np.nan
#======================================================================================================
grid.GetRasterBand(1).WriteArray(data) # converte o grid para celsius
#======================================================================================================
# Export the result to GeoTIFF
driver = gdal.GetDriverByName('GTiff')
driver.CreateCopy('/home/cendas/GOES16_WS_Rodrigo/Geotiff/Bocaina/sistconvectivos_Bocaina'+str(Start)+'.tif', grid, 0)

# Add to the log file (called "G16_Log.txt") the NetCDF file name that I just processed.

# If the file doesn't exists, it will create one.
with open('/home/cendas/GOES16_WS_Rodrigo/Geotiff/Bocaina/G16_Log.txt', 'a') as log:
 log.write(path.replace('\\\\', '\\') + '\n')