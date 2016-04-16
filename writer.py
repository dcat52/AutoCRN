"""AutoCRN
dcat52 Software
"""

from _ast import arguments
from pykeyboard import PyKeyboard
from pymouse import PyMouseEvent
import time

__author__ = 'dcat52 (Davis Catherman)'

def crnWriter(crns):
    """crnWriter
    Args:
        crns: array of CRNs to be entered

    Returns:
    """

    #Hack to make input work for both Python 2 and Python 3
    try:
        input = raw_input
    except NameError:
        pass

    k = PyKeyboard()

    k.press_key(k.alt_key)
    time.sleep(0.20)
    k.tap_key(k.tab_key)
    k.release_key(k.alt_key)
    time.sleep(0.20)
    
    for x in crns:
        time.sleep(0.20)
        k.type_string(x)
        k.tap_key(k.tab_key)
