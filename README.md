# AutoCRN

Program to auto enter CRN numbers for Registration of Classes.

## Standalone Program ##
For those that just wish to use this and be done.

```
Coming Soon!
Primarily to Windows (other OS's: unknown)
```

## Dependencies ##

### Linux Development ###
```
Python
Xlib (for PyUserInput)
PyUserInput
```

### Windows Development ###
```
Python
pywin32 (for PyUserInput)
pyHook (for PyUserInput)
PyUserInput
```

### Mac Development ###
People develop on Macs?
Figure it out, or use Linux.
```
Current listed dependencies for PyUserInput:
Quartz, AppKit
```

NOTICE: If other dependencies needed, check out PyUserInput. Requirements might change.

## Installation ##

### Linux ###
Development and Use.

Download Xlib

Goto directory to hold the temp files.

```
wget https://sourceforge.net/projects/python-xlib/files/latest/download
```
Unpack and enter directory

```
sudo python ./setup.py build
sudo python ./setup.py install
```

In home directory

```
git clone https://github.com/PyUserInput/PyUserInput
cd PyUserInput
sudo python ./setup.py build
sudo python ./setup.py install
```

Back to Home directory

```
git clone https://github.com/dcat52/AutoCRN
cd AutoCRN
```
