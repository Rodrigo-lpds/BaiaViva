import os
from osgeo import gdal

#------------------------------------------------------------------------------------
#Região Metropolitana:
#extent = [-44.080 ,-21,-42.20,-23.60] #<ulx> <uly> <lrx> <lry>
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#Bocaina:
#extent = [-45, -21 ,-42, -24] #<ulx> <uly> <lrx> <lry>
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#Sudeste:
#extent = [-54,-13.50,-38,-26] #<ulx> <uly> <lrx> <lry>
#------------------------------------------------------------------------------------

directory = r'C:\Users\Administrator\Documents\Plot Geotiff\data'
dataset = []
for filename in os.listdir(directory):
    if filename.endswith(".tif"):
        ds = gdal.Open(os.path.join(directory, filename))
        ds = gdal.Translate('./Cropped_tifs/cropped_'+ filename, ds, projWin = extent) #<ulx> <uly> <lrx> <lry> talvez.. = [-47,-20 ,-42,-25] 
        ds = None
    else:
        continue



