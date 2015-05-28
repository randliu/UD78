'''
Created on 2015-5-20

@author: user
'''

from .models import Stock,TRACKSTATUS
from .utils import preProcess
from datetime import timedelta

import urllib
import contextlib
import datetime

"""
def runStock(market = None ,code =None ):
    if not code :
        return None
    set = Stock.objects

    if market:
"""
import time
def dailyRun(market = None,code = None):
    lst_stock = Stock.objects.all()
    
    if market is not None:
        lst_stock = lst_stock.filter(market = market )
    if code is not None:
        lst_stock = lst_stock.filter(code = code )
        
    for s in lst_stock:
        print time.time
        print "\n$$$$$$$$$$$$$$$$$$$$$$$$$\n"
        print "scaning [%06d.%s %s]"%(s.code,s.market,s.name)
        api = s.getAPI()
        print "fetching daily price from %s"%api
        #print "begin:"+str(time.time())
        begin =time.time()
        with contextlib.closing(urllib.urlopen(api)) as x:
            #print time.time()
            print "Parsing"
            n,prices = preProcess(x)
            #print time.time()
            s.parse(prices)
            #print time.time()
            s.scanPeakPoint()
            #print time.time()
            s.scanTroughPoint()
            #print time.time()
            s.scanLadder()
            #print time.time()
            s.scanRiseTrack()
            #print time.time()
            s.scanDropTrack()
            #print time.time()
            s.runDropTrack()
            #print time.time()
            s.runRiseTrack()
            #print time.time()
            end = time.time()
            print "time cost:"+str(end-begin)
def reportTrack(code,market = None):  
    s=Stock.objects.filter(code = code)
    if market:
        s=s.filter(market=market)
    s=s.get()
    d=datetime.datetime.now()
    str_now=datetimeToTitanDatestr(d)
    r = int(str_now)
    lst_riseTrack=s.risetrack_set.filter(lastDay__gt=r).order_by("lastDay").all()
    
    for dt in lst_riseTrack:
        print "[%s] [%d - %d]    [%06d %s.%s] value :%2d count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.lastValue,dt.count)
    #print s
def datetimeToTitanDatestr(d):
    str_now=str(d.year-2000)+str("%02d"%d.month)+str("%02d"%d.day)
    return str_now
 
def report_hk(day =7,code =None):
    report(day =day ,code=code ,market="hk")

def report_sh(day =7,code =None):
    report(day =day ,code=code ,market="sh")

def report_sz(day =7,code =None):
    report(day =day ,code=code ,market="sz")

def report(day = 7,code=None,market = None):
    d=datetime.datetime.now()
    #str(d.year-2000)+str("%02d"%d.month)+str("%02d"%d.day)
    offsetDays = timedelta(day)
    targetDay =d - offsetDays
    str_now=datetimeToTitanDatestr(targetDay)
    int_now = int(str_now)
    #in 1 month
    r=int_now
    print "r=%d"%r
    
    #print "SELL:"
    set = Stock.objects.all()
    if code:
        set = set.filter(code = code)
    if market :
        set =set.filter(market = market)
        
    print "\n"+"\nRISE TRACK\n"+"----------"*6
    
    for s in set:
        lst_riseTrack = s.risetrack_set.filter(status = TRACKSTATUS.SELL).filter(lastDay__gt=r).order_by("lastDay").all()
        for dt in lst_riseTrack:
            print "[%s] [%d - %d]    [%06d %s.%s] count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.count)
        #print "" 
    
    print "\n"+"\nDROP TRACK\n"+"----------"*6

    #print "BUY:"

    for s in set:
        lst_dropTrack = s.droptrack_set.filter(status = TRACKSTATUS.BUY).filter(lastDay__gt=r).order_by("lastDay").all()
        for dt in lst_dropTrack:
            print "[%4s] [%d - %d]    [%06d %s.%s] count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.count)
        #print ""

            