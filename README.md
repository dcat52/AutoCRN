# AutoCRN

Program to auto enter CRN numbers for Registration of Classes.

How to use: enter your alt-pin before registration time. press submit when time opens, select 1st open slot then double click program.

I strongly reccommend testing this by opening an excel sheet and selecting a field and then run program as if it is the registration page.  

Note: More wait statements may need to be added if sporadic results. Depending on OS and how it was run, you may need 2 tabs or only 1 tab for changing windows; again important to test with excel.

## Standalone Program ##
For those that just wish to use this and be done
```
Coming Soon!
Primarily to Windows (other OS's: unknown)
```

## Dependencies ##

### Linux Development ###
```
Python
  docopt
PyUserInput
  Xlib
```

### Windows Development ###
```
Python
  docopt
PyUserInput
  pywin32
  pyHook
```

### Mac Development ###
People develop on Macs?
Figure it out, or use Linux.
```
Python
  Docopt
PyUserInput
  Quartz
  AppKit
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

One minor dependency:
```
pip install docopt
```

Back to Home directory
```
git clone https://github.com/dcat52/AutoCRN
cd AutoCRN
```
