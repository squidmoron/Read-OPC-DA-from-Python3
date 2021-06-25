#------------------------------------------------------------------------
#-----Name 		: Aditya Ferdianto       --------------------------------
#-----Prog 		: Python for Read OPC DA --------------------------------
#-----Company 	: Mattel Inc.            --------------------------------
#-----Date		: June 2021              --------------------------------
#------------------------------------------------------------------------

import OpenOPC
import win32pdh
import Pyro4
import time
import datetime
import pywintypes

import influxdb
import json
from influxdb import InfluxDBClient
from win10toast import ToastNotifier
#toaster = ToastNotifier()

#toaster.show_toast("Python for Read OPC DA","Reading OPC DA",duration=25)

#--------------------------Variable All----------------------------------
host ='Matrikon.OPC.Simulation'
pywintypes.datetime = pywintypes.TimeType
opc = OpenOPC.client()

#-----for trial read data opc
opc.connect(host)
x=opc.read('Random.Real8')
print(x)

AVG_CTArm				=''
AVG_CTFront			=''
AVG_CTBack			=''
AVG_CTNeck			=''
AVG_CTConnector	=''

#------------------------------------------------------------------------
class dataOPC:
  def __init__(self, valueOPC, qualityOPC, datetimeOPC):
    self.valueOPC = valueOPC
    self.qualityOPC = qualityOPC
    self.datetimeOPC = datetimeOPC
#------------------------------------------------------------------------
def parsing(x):
  x=x.replace(' ','').replace("'","").replace('(','').replace(')','')
  x=x.split(',')
  return x
#------------------------------------------------------------------------
def readOPC(variable) :
	opc.connect(host)
	try	:
		value=parsing(str(opc.read(variable)))
		value=dataOPC(value[0],value[1],value[2])
		if(value.qualityOPC=="Good"):
			return value
	except :
		print("============================= read problem =============================")
	opc.close()
#------------------------------------------------------------------------

while 1 :
	try:
		AVG_CTArm=readOPC('Random.Real8')
		print(round(float(AVG_CTArm.valueOPC),2))
	except:
		print("Can not read opc data or data equal to Not Good")
	time.sleep(.1)