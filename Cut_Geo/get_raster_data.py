import os
import numpy as np
from osgeo import gdal
import sys
#------------------------------------------------------------------------------------
#Região Metropolitana:
#extent = [-44.080 ,-21,-42.20,-23.60] #<ulx> <uly> <lrx> <lry>
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#Bocaina:
extent = [-45, -21 ,-42, -24] #<ulx> <uly> <lrx> <lry>

#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#Sudeste:
#extent = [-54,-13.50,-38,-26] #<ulx> <uly> <lrx> <lry>
#------------------------------------------------------------------------------------

#directory = r'C:\Users\Administrator\Documents\Plot Geotiff\data'
#dataset = []
#for filename in os.listdir(directory):
#    if filename.endswith(".tif"):
#        ds = gdal.Open(os.path.join(directory, filename))
#        ds = gdal.Translate('./Cropped_tifs/cropped_'+ filename, ds, projWin = extent) #<ulx> <uly> <lrx> <lry> talvez.. = [-47,-20 ,-42,-25] 
#        ds = None
#    else:
#        continue
#directory = r'C:\Users\Administrator\Documents\Plot Geotiff\data'
#dataset = []
#for filename in os.listdir(directory):
#    if filename.endswith(".tif"):
#        ds = gdal.Open(os.path.join(directory, filename))
#        ds = gdal.Translate('./Cropped_tifs/cropped_'+ filename, ds, projWin = extent) #<ulx> <uly> <lrx> <lry> talvez.. = [-47,-20 ,-42,-25] 
#        ds = None
#    else:
#        continue

import rasterio
#C:\Users\Administrator\Documents\Plot Geotiff\BaiaViva\Cut_Geo\Cropped_tifs\cropped_wc2.1_2.5m_prec_2018-05.tif
with rasterio.open(r"C:\Users\Administrator\Documents\Plot Geotiff\BaiaViva\Cut_Geo\Cropped_tifs\cropped_wc2.1_2.5m_prec_2018-05.tif", 'r') as ds:
    arr = ds.read(1)  # read all raster values

#print(arr[0])  # this is a 3D numpy array, with dimensions [band, row, col]
from matplotlib import pyplot as plt
#plt.imshow(arr, interpolation='nearest')
#plt.show()

def convert_tif_to_txt(tif_array,extent):
    min_lat,max_lat, min_lon,max_lon = extent[3],extent[1],extent[0],extent[2]
    arquivo = open("teste.txt", "a")
    #arquivo.write("Lat | Long | Dado")
    max_row,max_col = arr.shape
    range_lat = abs(max_lat - min_lat)
    range_lon = abs(max_lon - min_lon)

    pace_row = np.arange(max_lat, min_lat, -np.round(range_lat/max_row,2))
    pace_col = np.arange(min_lon, max_lon, np.round(range_lon/max_col,2))
    #print(pace_col)

    for index_y,array_y in enumerate(tif_array):
        for index_x,array_x in enumerate(array_y):
            #arquivo.write("\n")
            arquivo.write(str(np.round(pace_row[index_y],3))+","+ str(np.round(pace_col[index_x],3))+","+ str(array_x)+"\n")
convert_tif_to_txt(arr,extent)
