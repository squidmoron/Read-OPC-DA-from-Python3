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
#from win10toast import ToastNotifier
#toaster = ToastNotifier()

#toaster.show_toast("Python for Read OPC DA","Reading OPC DA",duration=25)

#--------------------------Variable All----------------------------------
#host ='Matrikon.OPC.Simulation'
host  ='CoDeSys.OPC.DA'
pywintypes.datetime = pywintypes.TimeType
opc = OpenOPC.client()

#-----for trial read data opc
opc.connect(host)
x=opc.read('PLC_GW3..FrontTorso_TimeOut')
print(x)

DT_CountDipping =""
DT_CountLeg =""
DT_CountArm =""
DT_CountFrontTorso =""
DT_CountHipConnector =""
DT_CountUnloading =""
DT_CountNeck =""

AVG_CTArmAssy =""
AVG_CTDipping =""
AVG_CTFrontTorso =""
AVG_CTHipConnector =""
AVG_CTLegAssy =""
AVG_CTNeckConnector =""
AVG_CTUnload =""

FrontTorso_TimeOut=''

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
		AVG_CTArmAssy=readOPC('PLC_GW3..AVG_CTArmAssy')
		AVG_CTDipping=readOPC('PLC_GW3..AVG_CTDipping')
		AVG_CTFrontTorso=readOPC('PLC_GW3..AVG_CTFrontTorso')
		AVG_CTHipConnector=readOPC('PLC_GW3..AVG_CTHipConnector')
		AVG_CTLegAssy=readOPC('PLC_GW3..AVG_CTLegAssy')
		AVG_CTNeckConnector=readOPC('PLC_GW3..AVG_CTNeckConnector')
		AVG_CTUnload=readOPC('PLC_GW3..AVG_CTUnload')

		DT_CountDipping=readOPC('PLC_GW3..DT_CountDipping')
		DT_CountLeg=readOPC('PLC_GW3..DT_CountLeg')
		DT_CountArm=readOPC('PLC_GW3..DT_CountArm')
		DT_CountFrontTorso=readOPC('PLC_GW3..DT_CountFrontTorso')
		DT_CountHipConnector=readOPC('PLC_GW3..DT_CountHipConnector')
		DT_CountUnloading=readOPC('PLC_GW3..DT_CountUnloading')

		FrontTorso_TimeOut=readOPC('PLC_GW3..FrontTorso_TimeOut')

		print(AVG_CTArmAssy.value)
		print(AVG_CTDipping.value)
		print(AVG_CTFrontTorso.value)
		print(AVG_CTHipConnector.value)
		print(AVG_CTLegAssy.value)
		print(AVG_CTNeckConnector.value)
		print(AVG_CTUnload.value)

		print(DT_CountDipping.value)
		print(DT_CountLeg.value)
		print(DT_CountArm.value)
		print(DT_CountFrontTorso.value)
		print(DT_CountHipConnector.value)
		print(DT_CountUnloading.value)
		print(FrontTorso_TimeOut.value)
		print("==================================================")
	except:
		print("Can not read opc data or data equal to Not Good")
	time.sleep(2)