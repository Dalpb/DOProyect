#!/bin/bash

# activo mi venv
python3 -m venv venv

# activo el ambiente
source venv/bin/activate

# Instalar mis  dependencias :D
pip install fastapi==0.115.6
pip install pandas==2.2.3
pip install opsvis==1.1.13
pip install openseespy==3.7.0.6
pip install openseespylinux==3.7.0.6
pip install matplotlib==3.10.0
pip install numpy==1.26.1  
pip install uvicorn==0.23.0 
