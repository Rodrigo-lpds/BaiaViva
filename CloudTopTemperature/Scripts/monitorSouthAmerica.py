#!/usr/bin/python3
# -*- coding: utf-8 -*-

import glob # Unix style pathname pattern expansion
import os # Miscellaneous operating system interfaces
# Directory where you have the GOES-16 Files
dirname = '/home/cendas/GOES16_WS_Rodrigo/Samples/CloudTopTemp_Samples/'
# Put all file names on the directory in a list
G16_files = []
for filename in sorted(glob.glob(dirname+'OR_ABI-L2-CMI*.nc')):
 G16_files.append(filename)
# If the log file doesn't exist yet, create one
file = open('/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/South_America/G16_Log.txt', 'a')
file.close()
# Put all file names on the log in a list
logSouthAmerica = []
with open('/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/South_America/G16_Log.txt') as file:
 logSouthAmerica = file.readlines()
# Remove the line feed
logSouthAmerica = [x.strip() for x in logSouthAmerica]
# Compare the directory list with the file list
# Loop through all files in the directory
for x in G16_files:
 # If a file is not on the log, process it
 if x not in logSouthAmerica:
  os.system("/home/cendas/miniconda3/envs/DataEnv/bin/python3 " + "\"/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/SouthAmerica.py\"" + " " + "\"" + x.replace('\\','\\\\') + "\"")
 
