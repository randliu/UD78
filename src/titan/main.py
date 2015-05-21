'''
Created on 2015-5-20

@author: user
'''

from .models import *
from .utils import *

import urllib
import contextlib

def dailyRun():
    lst_stock = Stock.objects.all()
    for s in lst_stock:
        api = s.getAPI()
        
        with contextlib.closing(urllib.urlopen(api)) as x:
            n,prices = preProcess(x)
            s.parse(prices)
            s.scanPeakPoint()
            s.scanTroughPoint()
            s.scanLadder()
            s.scanRiseTrack()
            s.scanDropTrack()
            s.runDropTrack()
            s.runRiseTrack()
            
            