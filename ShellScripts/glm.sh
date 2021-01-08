/home/cendas/miniconda3/envs/DataEnv/bin/python3 /home/cendas/GOES16_WS_Rodrigo/GLM/src/monitorGLM.py


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