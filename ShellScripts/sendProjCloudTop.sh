#!/bin/bash 

export WORK="/home/cendas/GOES16_WS_Rodrigo/CloudTopTemperature/Output/RJ/ConvectiveSystem/"  
cd $WORK
#Pega ultimo jpg processado na lista
ultimo=`tail -n1 Lista_JPG.txt`
#copia para a outra maquina via SSH
scp -P7654 ${ultimo} faho@146.164.165.132:/u/home/cendas/plataforma/satelite/SistConvectivos_RJ/.

