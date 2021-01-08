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
from headerNetcdf import getBand,convertDate # Import band and convert date function
from os import listdir
from os.path import isfile, join,splitext
import sys # Import the "system specific parameters and functions" module
import datetime # Library to convert julian day to dd-mm-yyyy


def plot(sistemas_convectivos_nc,glm_nc,local,extent,resolution=2):
    
    if(local=='Brasil'):
        degrees = 10
        label_fontsize = 50
    elif(local=='Sudeste'):
        degrees = 5
        label_fontsize = 8
    else:
        degrees = 2   
        resolution = 0.8     
        label_fontsize = 8
    
    g16glm = Dataset(glm_nc,'r')
    nc = Dataset(sistemas_convectivos_nc)

    # Get the latitude and longitude image bounds
    geo_extent = nc.variables['geospatial_lat_lon_extent']
    min_lon = float(geo_extent.geospatial_westbound_longitude)
    max_lon = float(geo_extent.geospatial_eastbound_longitude)
    min_lat = float(geo_extent.geospatial_southbound_latitude)
    max_lat = float(geo_extent.geospatial_northbound_latitude)

    # Choose the visualization extent (min lon, min lat, max lon, max lat)
    #extent = [-45.0, -24.5, -39.0, -20.7] 

    # Choose the image resolution (the higher the number the faster the processing is)
    #resolution = 0.8 #2

    # Calculate the image extent required for the reprojection
    H = nc.variables['goes_imager_projection'].perspective_point_height
    x1 = nc.variables['x_image_bounds'][0] * H 
    x2 = nc.variables['x_image_bounds'][1] * H 
    y1 = nc.variables['y_image_bounds'][1] * H 
    y2 = nc.variables['y_image_bounds'][0] * H 

    # Call the reprojection funcion
    grid = remap(sistemas_convectivos_nc, extent, resolution,  x1, y1, x2, y2)
    tipos = ["todos","event","group","flash"]
    for formato in range(4):
        glm_variables = [False,False,False,False]
        glm_variables[formato] = True
        #print(glm_variables)
        # Read the data returned by the function ==============================================================
        # If it is an IR channel subtract 273.15 to convert to ° Celsius
        data = grid.ReadAsArray() - 273.15

        # Make pixels outside the footprint invisible
        data[data <= -180] = np.nan

        # Define the size of the saved picture =================================================================
        DPI = 150
        fig = plt.figure(figsize=(data.shape[1]/float(DPI), data.shape[0]/float(DPI)), frameon=False, dpi=DPI)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        ax = plt.axis('off')

        # Plot the Data =======================================================================================

        # Create the basemap reference for the Rectangular Projection
        bmap = Basemap(llcrnrlon=extent[0], llcrnrlat=extent[1], urcrnrlon=extent[2], urcrnrlat=extent[3], epsg=4326)

        # Draw the countries and Brazilian states shapefiles
        bmap.readshapefile('/home/cendas/GOES16_WS_Rodrigo/GLM/src/BRA_adm1','BRA_adm1',linewidth=0.50,color='#000000')

        if(local=='Brasil'):
            bmap.readshapefile('/home/cendas/GOES16_WS_Rodrigo/GLM/src/ne_10m_coastline','ne_10m_coastline',linewidth=0.50,color='#000000')

        #ne_10m_coastline
        # Draw parallels and meridians
        if(not(local=='Brasil')):
            bmap.drawparallels(np.arange(-90.0, 90.0, degrees), linewidth=0.3, dashes=[4, 4], color='white', labels=[True,False,False,True], fmt='%g', labelstyle="+/-", size=8)
            bmap.drawmeridians(np.arange(0.0, 360.0, degrees), linewidth=0.3, dashes=[4, 4], color='white', labels=[True,False,False,True], fmt='%g', labelstyle="+/-", size=8)
        else: 
            bmap.drawparallels(np.arange(-90.0, 90.0, degrees), linewidth=0.3, dashes=[4, 4], color='white', labels=[True,False,False,True], fmt='%g', labelstyle="+/-", size=30)
            bmap.drawmeridians(np.arange(0.0, 360.0, degrees), linewidth=0.3, dashes=[4, 4], color='white', labels=[True,False,False,True], fmt='%g', labelstyle="+/-", size=30)
        #Split the dataset with temperatures above and below -20°C 
        temp = -80
        tempAbove= masked_array(data,data<temp)
        tempBelow = masked_array(data,data>=temp)

        # Converts a CPT file to be used in Python 

        cptSquareRoot = loadCPT('/home/cendas/GOES16_WS_Rodrigo/GLM/src/Square Root Visible Enhancement.cpt')
        # Makes a linear interpolation
        cpt_convert_SquareRoot = LinearSegmentedColormap('cpt', cptSquareRoot) 

        # Plot the GOES-16 channel with the converted CPT colors (you may alter the min and max to match your preference)
        plot_SquareRoot = bmap.imshow(tempAbove, origin='upper', cmap=cpt_convert_SquareRoot, vmin=-80, vmax=100)      

        # ===================== LEGENDA ==========================

        # Get the unit based on the channel. If channels 1 trough 6 is Albedo. If channels 7 to 16 is BT.
        Unit = "Cloud Top Temperature [°C]"

        # Choose a title for the plot
        Title = " Geostationary Lightning Mapper (GLM) - GOES Satellite"
        Latitude = "Latitude"
        Longitude = "Longitude"

        # Add a black rectangle in the bottom to insert the image description
        lon_difference = (extent[2] - extent[0]) # Max Lon - Min Lon
        # Add the image description inside the black rectangle
        lat_difference = (extent[3] - extent[1]) # Max lat - Min lat
        if(not(local=='Brasil')):
        #Labels and its positions #
            plt.text(extent[0] + lon_difference * 0.5, extent[3] + lat_difference * 0.035,Title, horizontalalignment='center', color = 'black', size=9)
            
            plt.text(extent[0] + lon_difference * 0.5, extent[3] + lat_difference * 0.065," ", horizontalalignment='center', color = 'black', size=10)
            
            plt.text(extent[0] + lon_difference * 0.5, extent[1] - lat_difference * 0.11,Longitude, horizontalalignment='center',color = 'black', size=10)
            
            plt.text(extent[0] + lon_difference * 0.5, extent[1] - lat_difference * 0.15," ", horizontalalignment='center', color = 'black', size=18)    
            
            plt.text(extent[0] - lon_difference * 0.15, extent[1] + lat_difference * 0.5 ,Latitude, verticalalignment ='center', rotation = "vertical", color = 'black', size=10) 
      
        else:
            plt.text(extent[0] + lon_difference * 0.5, extent[3] + lat_difference * 0.035,Title, horizontalalignment='center', color = 'black', size=40)
            
            plt.text(extent[0] + lon_difference * 0.5, extent[3] + lat_difference * 0.065," ", horizontalalignment='center', color = 'black', size=10)
            
            plt.text(extent[0] + lon_difference * 0.5, extent[1] - lat_difference * 0.11,Longitude, horizontalalignment='center',color = 'black', size=40)
            
            plt.text(extent[0] + lon_difference * 0.5, extent[1] - lat_difference * 0.15," ", horizontalalignment='center', color = 'black', size=18)    
            
            plt.text(extent[0] - lon_difference * 0.15, extent[1] + lat_difference * 0.5 ,Latitude, verticalalignment ='center', rotation = "vertical", color = 'black', size=40) 
         
        # ========================================
        if(glm_variables[0]):#Todos
            # Get Events, Group and flash from Glm file
            event_lat = g16glm.variables['event_lat'][:]
            event_lon = g16glm.variables['event_lon'][:]

            group_lat = g16glm.variables['group_lat'][:]
            group_lon = g16glm.variables['group_lon'][:]

            flash_lat = g16glm.variables['flash_lat'][:]
            flash_lon = g16glm.variables['flash_lon'][:]


            # Plot events as large blue dots
            event_x, event_y = bmap(event_lon, event_lat)
            bmap.plot(event_x, event_y, 'bo', markersize=7,label='Events')

            # Plot groups as medium green dots
            group_x, group_y = bmap(group_lon, group_lat)
            bmap.plot(group_x, group_y, 'go', markersize=3,label='Group')

            # Plot flashes as small red dots
            flash_x, flash_y = bmap(flash_lon, flash_lat)
            bmap.plot(flash_x, flash_y, 'ro', markersize=1,label='Flash')
            plt.legend(fontsize=label_fontsize,loc=4)
        else:
            if(glm_variables[1]):
                # Get Events from Glm file
                event_lat = g16glm.variables['event_lat'][:]
                event_lon = g16glm.variables['event_lon'][:]
                # Plot events as large blue dots
                event_x, event_y = bmap(event_lon, event_lat)
                bmap.plot(event_x, event_y, 'bo', markersize=7,label='Events')
            if(glm_variables[2]):
                # Get Group from Glm file
                group_lat = g16glm.variables['group_lat'][:]
                group_lon = g16glm.variables['group_lon'][:]
                # Plot groups as medium green dots
                group_x, group_y = bmap(group_lon, group_lat)
                bmap.plot(group_x, group_y, 'go', markersize=3,label='Group')
            if(glm_variables[3]):
                # Get Flash from Glm file
                flash_lat = g16glm.variables['flash_lat'][:]
                flash_lon = g16glm.variables['flash_lon'][:]    
                # Plot flashes as small red dots
                flash_x, flash_y = bmap(flash_lon, flash_lat)
                bmap.plot(flash_x, flash_y, 'ro', markersize=1,label='Flash')
            plt.legend(fontsize=label_fontsize,loc=4)
            #plt.show()
        Start = glm_nc[glm_nc.find('_s')+1:glm_nc.find("_e")-3] 
        year = int(Start[1:5])
        dayjulian = int(Start[5:8]) - 1 # Subtract 1 because the year starts at "0"
        dayconventional = datetime.datetime(year,1,1) + datetime.timedelta(dayjulian) # Convert from julian to conventional
        month = dayconventional.strftime('%m')
        day = dayconventional.strftime('%d')
        hour = int(Start[8:12])
        plt.savefig('/home/cendas/GOES16_WS_Rodrigo/GLM/Output/'+local+'/glm_'+ str(year)+str(month)+str(day)+'_'+ str(hour)+'_'+ tipos[formato]+'.png', dpi=DPI, pad_inches=0, transparent=True,bbox_inches='tight')
        plt.close()
    


def get_proper_glm(mypath,sispath):  
  #mypath = "/home/cendas/Temperature-Analysis/samples/"
  onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and splitext(f)[1] == '.nc']
  intervalo = sispath[sispath.find('_s')+1:sispath.find("_e")-3]
  #print(intervalo)
  glmfiles = []
  for ncfile in onlyfiles:
    if(intervalo in ncfile):
      glmfiles.append(ncfile)
  glmfiles.sort()
  return (mypath+glmfiles[0])

#Channel 13)
#sis_path = "OR_ABI-L2-CMIPF-M6C13_G16_s20203031740189_e20203031749508_c20203031750004.nc"

#GLM
#lm_path = 'OR_GLM-L2-LCFA_G16_s20203031800000_e20203031800204_c20203031800226.nc'
glm_folder = '/home/cendas/GOES16_WS_Rodrigo/Samples/GLM_Samples/'
sis_path = sys.argv[1]
try:
  glm_path = get_proper_glm(glm_folder,sis_path)
  print(glm_path)
  #locais = {'Brasil':  [-74, -34.0, -34.0, 5.30], 'Sudeste': [-53.15, -25.5, -39.0, -14.0], 'RJ': [-45.0, -24.5, -39.0, -20.7], 'Bocaina':[-47 ,-25,-42,-20], 'RegiaoSerrana': [-46,-26,-40,-19], 'RegiaoNorte': [-44,-27,-38,-21]}
  local = 'RegiaoSerrana'
  extent = [-46,-26,-40,-19]
  plot(sis_path,glm_path,local,extent)
  #for local in locais:
   #   plot(sis_path,glm_path,local,locais[local])
  
  
  # If the file doesn't exists, it will create one.
  with open('/home/cendas/GOES16_WS_Rodrigo/GLM/Output/RegiaoSerrana/G16_Log.txt', 'a') as log:
   log.write(sis_path.replace('\\\\', '\\') + '\n')
except:
  pass    