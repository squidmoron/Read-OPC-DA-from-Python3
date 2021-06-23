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

AVG_CTArm		= 0
AVG_CTFront		=''
AVG_CTBack		=''
AVG_CTNeck		=''
AVG_CTConnector	=''

#------------------------------------------------------------------------
class dataOPC:
  def __init__(self, value, quality, datetime):
    self.value = value
    self.quality = quality
    self.datetime = datetime
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
		if(value.quality=="Good"):
			return value
	except :
		print("============================= read problem =============================")
	opc.close()
#------------------------------------------------------------------------

while 1 :
	try:
		AVG_CTArm=readOPC('Random.Real8')
		print(AVG_CTArm.value)
	except:
		print("Can not read opc data or data equal to Not Good")
	time.sleep(1)