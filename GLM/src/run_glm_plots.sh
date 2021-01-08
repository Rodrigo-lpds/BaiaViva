#!/bin/bash
source /home/cendas/miniconda3/bin/activate DataEnv

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitor_bocaina.py

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitor_serrana.py

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitor_norte.py

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitor_rj.py

/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitor_sudeste.py

#/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitor_brasil.py



#Deixa apenas as ultimas 192 projecoes no diretorio
export WORK="/home/cendas/GOES16_WS_Rodrigo/GLM/Output/Bocaina/"
cd $WORK
ls -t | tail -n +195 | xargs rm

#Deixa apenas as ultimas 192 projecoes no diretorio
export WORK="/home/cendas/GOES16_WS_Rodrigo/GLM/Output/Brasil/"
cd $WORK
ls -t | tail -n +195 | xargs rm 

#Deixa apenas as ultimas 192 projecoes no diretorio
export WORK="/home/cendas/GOES16_WS_Rodrigo/GLM/Output/RegiaoNorte/"
cd $WORK
ls -t | tail -n +195 | xargs rm 

#Deixa apenas as ultimas 192 projecoes no diretorio
export WORK="/home/cendas/GOES16_WS_Rodrigo/GLM/Output/RegiaoSerrana/"
cd $WORK
ls -t | tail -n +195 | xargs rm  

#Deixa apenas as ultimas 192 projecoes no diretorio
export WORK="/home/cendas/GOES16_WS_Rodrigo/GLM/Output/RJ/"
cd $WORK
ls -t | tail -n +195 | xargs rm  

#Deixa apenas as ultimas 192 projecoes no diretorio
export WORK="/home/cendas/GOES16_WS_Rodrigo/GLM/Output/Sudeste/"
cd $WORK
ls -t | tail -n +195 | xargs rm  