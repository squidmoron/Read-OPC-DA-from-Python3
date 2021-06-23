# Read-OPC-DA-from-Python3
Read OPC DA from Python3

If you need to Read variable data from OPC DA used python3 and Windows 10
You can follow the instruction below:

1) Install Python3.9 32bit i used Python3.9.5 32bit https://www.python.org/ftp/python/3.9.5/python-3.9.5.exe

2) Add Path of Python3.9 and pip in folder /Script

3) INSTALL PYWIN32 : https://github.com/mhammond/pywin32/releases

4) DOWNLOAD AND REGISTER THE DLL:  http://www.gray-box.net/download_daawrapper.php
   Command: regsvr32 gbda_aut.dll  (OPC DA Auto Wrapper)

5) INSTALL OPENOPC: pip3 install OpenOPC-Python3x
   if pip need to upgrade : pip install --upgrade pip


Install Matrikon OPC Simulator
Install Matrikon OPC Explorer

To communication from python to SQL Server you need to install PyODBC library

1) copy file "pyodbc-4.0.30-cp39-cp39-win32.whl"

2) open shell and run : pip install <PATH>\pyodbc-4.0.30-cp39-cp39-win32.whl

3) After shell shown :
	Installing collected packages: pyodbc
	Successfully installed pyodbc-4.0.30

4) You got your library for pyodbc
