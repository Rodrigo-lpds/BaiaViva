#!/bin/bash
source /home/cendas/miniconda3/bin/activate DataEnv

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorBocaina.py


/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorRegNorteFluminense.py
#printf "\nAs projecoes TRUE COLOR Sulamericanas estao atualizadas\n\n" "/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorRegNorteFluminense.py"

#Deixa apenas as ultimas 72 projecoes no diretorio
#export WORK='/home/cendas/GOES16_WS_Rodrigo/TrueColor/Output/RJ/'
#cd $WORK
#ls -t | tail -n +11 | xargs rm 
#Deixa apenas as ultimas 48 geotiffs no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/Geotiff/Bocaina/'
cd $WORK
ls -t | tail -n +51 | xargs rm 

#Deixa apenas as ultimas 48 geotiffs no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/Geotiff/RegiaoNorteFluminense/'
cd $WORK
ls -t | tail -n +51 | xargs rm 
