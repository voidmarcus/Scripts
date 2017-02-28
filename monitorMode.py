#!/usr/bin/env python

# Importar modulos
import os
import subprocess
import re

imput = 0

os.system("reset")

teste = subprocess.getoutput ("ifconfig | grep \"wl([^ || :]*)\" -E -o")

listaWireless = re.findall('(wl+[^\n]*)', teste)

print(listaWireless)

os.system ("sudo ifconfig"+listaWireless[imput]+" down")

os.system ("sudo iwconfig "+listaWireless[imput]+" mode monitor")

os.system ("sudo ifconfig "+listaWireless[imput]+" up")
