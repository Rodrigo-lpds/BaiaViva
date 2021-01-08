#!/bin/bash
source /home/cendas/miniconda3/bin/activate DataEnv

CHANNELS=('CH01' 'CH02' 'CH03' 'CH04' 'CH05' 'CH06' 'CH07' 'CH08' 'CH09' 'CH10' 'CH11' 'CH12' 'CH13' 'CH14' 'CH15' 'CH16')
qtdCH=${#CHANNELS[@]}

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorConvSystemRJ.py

#/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorRJ.py
#printf "\nAs projecoes centradas no Rio de Janeiro estao atualizadas\n\n"


#/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorSouthAmerica.py
#printf "\nAs projecoes Sulamericanas estao atualizadas\n\n" 

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorBocaina.py

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorRegNorteFluminense.py

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Scripts/monitorRegSerraMetro.py

#Deixa apenas as ultimas 48 projecoes no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/RJ/ConvectiveSystem/'
cd $WORK
ls -t | tail -n +51 | xargs rm

#Deixa apenas as ultimas 48 projecoes no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/Bocaina/'
cd $WORK
ls -t | tail -n +51 | xargs rm 

#Deixa apenas as ultimas 48 projecoes no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/RegiaoNorteFluminense/'
cd $WORK
ls -t | tail -n +51 | xargs rm 

#Deixa apenas as ultimas 48 projecoes no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/RegiaoSerraMetro/'
cd $WORK
ls -t | tail -n +51 | xargs rm  


#Deixa apenas 10 projecoes/imagens no diretorio
#for ((Channel=0; Channel< qtdCH; Channel++)) do
#export WORK='/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/RJ/Projections/'${CHANNELS[$Channel]}'/'
#cd $WORK

#ls -t | tail -n +11 | xargs rm 

#done
#Deixa apenas 10 projecoes/imagens no diretorio
#for ((Channel=0; Channel< qtdCH; Channel++)) do
#export WORK='/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/South_America/Projections/'${CHANNELS[$Channel]}'/'

#cd $WORK

#ls -t | tail -n +11 | xargs rm --

#done


#Deixa apenas os 120 arquivos NetCDF no diretorio
export WORK='/home/cendas/GOES16_WS_Rodrigo/Samples/CloudTopTemp_Samples/'
cd $WORK

ls -t | tail -n +21| xargs rm 
