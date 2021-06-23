import OpenOPC
import win32pdh
import Pyro4
import time
import datetime

import pywintypes

pywintypes.datetime = pywintypes.TimeType

opc = OpenOPC.client()
opc.connect('CoDeSys.OPC.DA')

while 1 :

    try	:
        #print(opc.list())
        avg_CTArm = opc.read('PLC_GW3..AVG_CTArmAssy')
        avg_CTFront = opc.read('PLC_GW3..AVG_CTFrontTorso')
        print("Average CT Arm   :",avg_CTArm)
        print("Average CT Front :",avg_CTFront)
    except (OpenOPC.TimeoutError):
        print("============================= read problem =============================")

    time.sleep(1)