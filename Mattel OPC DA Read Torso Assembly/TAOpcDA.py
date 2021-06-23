#------------------------------------------------------------------------
#-----Name    : Aditya Ferdianto       --------------------------------
#-----Prog    : Python for Read OPC DA --------------------------------
#-----Company : Mattel Inc.            --------------------------------
#-----Date    : June 2021              --------------------------------
#------------------------------------------------------------------------

import OpenOPC
import win32pdh
import Pyro4
import time
import datetime
import pywintypes

#import influxdb
#import json
#from influxdb import InfluxDBClient
#from win10toast import ToastNotifier

#--------------------------Variable All----------------------------------
#host ='Matrikon.OPC.Simulation'
host ='CoDeSys.OPC.DA'
pywintypes.datetime = pywintypes.TimeType
opc = OpenOPC.client()

#-----for trial read data opc
#opc.connect(host)
#x=opc.read('Random.Real8')
#print(x)

Gv_PartCount =""
GV_StdCycle =""
GVI_LastCycleTime =""
GV_IntRunTime =""
GV_IntDownTime =""
GV_IntUpTime =""
Gv_Target_HMI =""
GV_StartUp =""
DT_CountDipping =""
DT_CountLeg =""
DT_CountArm =""
DT_CountFrontTorso =""
DT_CountHipConnector =""
DT_CountUnloading =""
DT_CountNeck =""
GVI_TotalCycleTime =""
GVI_DownTimeDipping =""
GVI_DownTimeArm =""
GVI_DownTimeFrontTorso =""
GVI_DownTimeHip =""
GVI_DownTimeLeg =""
GVI_DownTimeNeck =""
FrontTorso_TimeOut =""
DippingStation_TimeOut =""
ArmAssy_TimeOut =""
HipConnector_TimeOut =""
LegStation_TimeOut =""
NeckConnector_TimeOut =""
Unload_TimeOut =""
DT_Stop_FrontTorso =""
DT_Stop_ArmStation =""
DT_Stop_DippingStation =""
DT_Stop_HipConnector =""
DT_Stop_LegStation =""
DT_Stop_Material =""
DT_Stop_NeckConnector =""
DT_Stop_Unloading =""
RunFlat =""
GVI_ResetValue =""
AVG_CTArmAssy =""
AVG_CTDipping =""
AVG_CTFrontTorso =""
AVG_CTHipConnector =""
AVG_CTLegAssy =""
AVG_CTNeckConnector =""
AVG_CTUnload =""

#------------------------------------------------------------------------
class dataOPC:
  def __init__(self, value, quality, datetime):
    self.value = value
    self.quality = quality
    self.datetime = datetime[8:10]+'-'+datetime[5:7]+'-'+datetime[:4]+' '+datetime[10:18]
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
def readDataOPC() :
	try :
		Gv_PartCount=readOPC('PLC_GW3..Gv_PartCount')
		GV_StdCycle=readOPC('PLC_GW3..GV_StdCycle')
		GVI_LastCycleTime=readOPC('PLC_GW3..GVI_LastCycleTime')
		GV_IntRunTime=readOPC('PLC_GW3..GV_IntRunTime')
		GV_IntDownTime=readOPC('PLC_GW3..GV_IntDownTime')
		GV_IntUpTime=readOPC('PLC_GW3..GV_IntUpTime')
		Gv_Target_HMI=readOPC('PLC_GW3..Gv_Target_HMI')
		GV_StartUp=readOPC('PLC_GW3..GV_StartUp')
		DT_CountDipping=readOPC('PLC_GW3..DT_CountDipping')
		DT_CountLeg=readOPC('PLC_GW3..DT_CountLeg')
		DT_CountArm=readOPC('PLC_GW3..DT_CountArm')
		DT_CountFrontTorso=readOPC('PLC_GW3..DT_CountFrontTorso')
		DT_CountHipConnector=readOPC('PLC_GW3..DT_CountHipConnector')
		DT_CountUnloading=readOPC('PLC_GW3..DT_CountUnloading')
		DT_CountNeck=readOPC('PLC_GW3..DT_CountNeck')
		GVI_TotalCycleTime=readOPC('PLC_GW3..GVI_TotalCycleTime')
		GVI_DownTimeDipping=readOPC('PLC_GW3..GVI_DownTimeDipping')
		GVI_DownTimeArm=readOPC('PLC_GW3..GVI_DownTimeArm')
		GVI_DownTimeFrontTorso=readOPC('PLC_GW3..GVI_DownTimeFrontTorso')
		GVI_DownTimeHip=readOPC('PLC_GW3..GVI_DownTimeHip')
		GVI_DownTimeLeg=readOPC('PLC_GW3..GVI_DownTimeLeg')
		GVI_DownTimeNeck=readOPC('PLC_GW3..GVI_DownTimeNeck')
		FrontTorso_TimeOut=readOPC('PLC_GW3..FrontTorso_TimeOut')
		DippingStation_TimeOut=readOPC('PLC_GW3..DippingStation_TimeOut')
		ArmAssy_TimeOut=readOPC('PLC_GW3..ArmAssy_TimeOut')
		HipConnector_TimeOut=readOPC('PLC_GW3..HipConnector_TimeOut')
		LegStation_TimeOut=readOPC('PLC_GW3..LegStation_TimeOut')
		NeckConnector_TimeOut=readOPC('PLC_GW3..NeckConnector_TimeOut')
		Unload_TimeOut=readOPC('PLC_GW3..Unload_TimeOut')
		DT_Stop_FrontTorso=readOPC('PLC_GW3..DT_Stop_FrontTorso')
		DT_Stop_ArmStation=readOPC('PLC_GW3..DT_Stop_ArmStation')
		DT_Stop_DippingStation=readOPC('PLC_GW3..DT_Stop_DippingStation')
		DT_Stop_HipConnector=readOPC('PLC_GW3..DT_Stop_HipConnector')
		DT_Stop_LegStation=readOPC('PLC_GW3..DT_Stop_LegStation')
		DT_Stop_Material=readOPC('PLC_GW3..DT_Stop_Material')
		DT_Stop_NeckConnector=readOPC('PLC_GW3..DT_Stop_NeckConnector')
		DT_Stop_Unloading=readOPC('PLC_GW3..DT_Stop_Unloading')
		RunFlat=readOPC('PLC_GW3..RunFlat')
		GVI_ResetValue=readOPC('PLC_GW3..GVI_ResetValue')
		AVG_CTArmAssy=readOPC('PLC_GW3..AVG_CTArmAssy')
		AVG_CTDipping=readOPC('PLC_GW3..AVG_CTDipping')
		AVG_CTFrontTorso=readOPC('PLC_GW3..AVG_CTFrontTorso')
		AVG_CTHipConnector=readOPC('PLC_GW3..AVG_CTHipConnector')
		AVG_CTLegAssy=readOPC('PLC_GW3..AVG_CTLegAssy')
		AVG_CTNeckConnector=readOPC('PLC_GW3..AVG_CTNeckConnector')
		AVG_CTUnload=readOPC('PLC_GW3..AVG_CTUnload')

		print(Gv_PartCount)
		print(GV_StdCycle)
		print(GVI_LastCycleTime)
		print(GV_IntRunTime)
		print(GV_IntDownTime)
		print(GV_IntUpTime)
		print(Gv_Target_HMI)
		print(GV_StartUp)
		print(DT_CountDipping)
		print(DT_CountLeg)
		print(DT_CountArm)
		print(DT_CountFrontTorso)
		print(DT_CountHipConnector)
		print(DT_CountUnloading)
		print(DT_CountNeck)
		print(GVI_TotalCycleTime)
		print(GVI_DownTimeDipping)
		print(GVI_DownTimeArm)
		print(GVI_DownTimeFrontTorso)
		print(GVI_DownTimeHip)
		print(GVI_DownTimeLeg)
		print(GVI_DownTimeNeck)
		print(FrontTorso_TimeOut)
		print(DippingStation_TimeOut)
		print(ArmAssy_TimeOut)
		print(HipConnector_TimeOut)
		print(LegStation_TimeOut)
		print(NeckConnector_TimeOut)
		print(Unload_TimeOut)
		print(DT_Stop_FrontTorso)
		print(DT_Stop_ArmStation)
		print(DT_Stop_DippingStation)
		print(DT_Stop_HipConnector)
		print(DT_Stop_LegStation)
		print(DT_Stop_Material)
		print(DT_Stop_NeckConnector)
		print(DT_Stop_Unloading)
		print(RunFlat)
		print(GVI_ResetValue)
		print(AVG_CTArmAssy)
		print(AVG_CTDipping)
		print(AVG_CTFrontTorso)
		print(AVG_CTHipConnector)
		print(AVG_CTLegAssy)
		print(AVG_CTNeckConnector)
		print(AVG_CTUnload)

	except:
		print("Can not read opc data or data equal to Not Good")

while 1 :
	try :
		readDataOPC()
	except:
		print("Read OPC Error")

	time.sleep(.1)
