# Read-OPC-DA-from-Python3
<img src=opclogo.png></img>

### If you need to Read variable data from OPC DA used python3 and Windows 10
### You can follow the instruction below:

1) Install Python3.9 32bit i used Python3.9.5 32bit [Download Here](https://www.python.org/ftp/python/3.9.5/python-3.9.5.exe)

2) Add Path of Python3.9 and pip in folder /Script

3) INSTALL PYWIN32 : [Download Here](https://github.com/mhammond/pywin32/releases)

4) DOWNLOAD AND REGISTER THE DLL:  [Download Here](http://www.gray-box.net/download_daawrapper.php) or you can Download from my repository [Here](https://github.com/squidmoron/Read-OPC-DA-from-Python3/tree/main/OPC%20DA%20Wrapper)
   
   Then Write a Command: regsvr32 gbda_aut.dll  [From OPC DA Auto Wrapper](https://github.com/squidmoron/Read-OPC-DA-from-Python3/tree/main/OPC%20DA%20Wrapper)

5) INSTALL OPENOPC: pip3 install OpenOPC-Python3x
   if pip need to upgrade : pip install --upgrade pip


	Install Matrikon OPC Simulator [Download Here](https://1drv.ms/u/s!Au49EKCDWwgSb1MOkwD6pWZKtjQ?e=lgd0dd)

	Install Matrikon OPC Explorer [Download Here](https://1drv.ms/u/s!Au49EKCDWwgScCkR-iZEVmW8I5I?e=fpWImH)

### If you wanna try to read an OPC DA variables with python, you can use a Matrikon OPC Simulator and try with "opcsimulation.py" script [Here](https://github.com/squidmoron/Read-OPC-DA-from-Python3/blob/main/Mattel%20OPC%20DA%20Read%20Torso%20Assembly/opcsimulation.py)


### To communication from python to SQL Server you need to install PyODBC library

1) copy file "pyodbc-4.0.30-cp39-cp39-win32.whl" you can find on repo [Python odbc library](https://github.com/squidmoron/Read-OPC-DA-from-Python3/tree/main/Python%20odbc%20library)

2) open shell and run : pip install <PATH>\pyodbc-4.0.30-cp39-cp39-win32.whl

3) After shell shown :
	Installing collected packages: pyodbc
	Successfully installed pyodbc-4.0.30

4) You got your library for pyodbc
	
### For python script to Insert, Update, and Select Database from MS SQL, you can find script [Here](https://github.com/squidmoron/Read-OPC-DA-from-Python3/tree/main/Python%20odbc%20library)
