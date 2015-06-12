# -*- coding:utf-8 -*-
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
        
    start = None
    end = None
    
    for s in lst_stock:
        print time.time
        print "\n"+"$$$$$$$$$$$$$$$$$$$$$$$$$"*2+"\n"
        print "scanning [%06d.%s %s] [seq:%d] "%(s.code,s.market,s.name,s.seq)
        api = s.getAPI()
        print "fetching daily price from %s"%api
        #print "begin:"+str(time.time())
        begin =time.time()
        if not start:
            start = begin
        prices = None
        with contextlib.closing(urllib.urlopen(api)) as x:
            #print time.time()
            print "Parsing"
            n,prices = preProcess(x)
            if n<0:
                print n
                
        s.parse(prices)
        s.scanPeakPoint()
        s.scanTroughPoint()
        s.scanLadder()
        s.scanRiseTrack()
        s.scanDropTrack()
        s.runDropTrack()
        s.runRiseTrack()
        end = time.time()
        print "time cost:"+str(end-begin)
        
    print "\nTOTAL TIME COST:"+str(end - start)+"\n"
    
    
def track(code=None,market = None,v =5,day =7):  
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
    stock_set = Stock.objects.all()
    if code:
        stock_set = stock_set.filter(code = code)
    if market :
        stock_set =stock_set.filter(market = market)
        
    print "\n"+"#######"*6+"\nRUN\n"+"#######"*6

        
    print "\n"+"\nRISE TRACK\n"+"----------"*6
    
    for s in stock_set:
        lst_riseTrack = s.risetrack_set.filter(status = TRACKSTATUS.RUN).filter(lastDay__gt=r).filter(lastValue__gt=v).order_by("lastDay").all()
        for dt in lst_riseTrack:
            print "[%s] [%d - %d]    [%06d %s.%s] value:%d count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.lastValue,dt.count)
        #print "" 
    
    print "\n"+"\nDROP TRACK\n"+"----------"*6

    #print "BUY:"

    for s in stock_set:
        lst_dropTrack = s.droptrack_set.filter(status = TRACKSTATUS.RUN).filter(lastDay__gt=r).filter(lastValue__gt=v).order_by("lastDay").all()
        for dt in lst_dropTrack:
            print "[%s] [%d - %d]    [%06d %s.%s] value:%d count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.lastValue,dt.count)
        #print ""
    print "\n"    
    print "\n"+"#######"*6+"\nFADED\n"+"#######"*6
    
    print "\n"+"\nRISE TRACK\n"+"----------"*6
    
    for s in stock_set:
        lst_riseTrack = s.risetrack_set.filter(status = TRACKSTATUS.FADE).filter(lastDay__gt=r).order_by("lastDay").all()
        for dt in lst_riseTrack:
            print "[%s] [%d - %d]    [%06d %s.%s] count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.count)
        #print "" 
    
    print "\n"+"\nDROP TRACK\n"+"----------"*6

    #print "BUY:"

    for s in stock_set:
        lst_dropTrack = s.droptrack_set.filter(status = TRACKSTATUS.FADE).filter(lastDay__gt=r).order_by("lastDay").all()
        for dt in lst_dropTrack:
            print "[%s] [%d - %d]    [%06d %s.%s] count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.count)
    
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
    stock_set = Stock.objects.all()
    if code:
        stock_set = stock_set.filter(code = code)
    if market :
        stock_set =stock_set.filter(market = market)
        
    print "\n"+"\nRISE TRACK\n"+"----------"*6
    
    for s in stock_set:
        lst_riseTrack = s.risetrack_set.filter(status = TRACKSTATUS.SELL).filter(lastDay__gt=r).order_by("lastDay").all()
        
        for dt in lst_riseTrack:
            last_price = s.dailyprice_set.get(day = dt.lastDay ).close
            first_price =s.dailyprice_set.get(day = dt.beginDay).close
            print "[%s] [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tcount:%3d"%(dt.status,dt.beginDay,first_price,dt.lastDay,last_price,s.code,s.market,s.name,(last_price - first_price)/first_price * 100.0,dt.count)
        #print "" 
    
    print "\n"+"\nDROP TRACK\n"+"----------"*6

    #print "BUY:"

    for s in stock_set:
        lst_dropTrack = s.droptrack_set.filter(status = TRACKSTATUS.BUY).filter(lastDay__gt=r).order_by("lastDay").all()
        for dt in lst_dropTrack:
            last_price = s.dailyprice_set.get(day = dt.lastDay ).close
            first_price =s.dailyprice_set.get(day = dt.beginDay).close

            print "[%s]  [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tcount:%3d"%(dt.status,dt.beginDay,first_price,dt.lastDay,last_price,s.code,s.market,s.name,(last_price - first_price)/first_price * 100.0,dt.count)
        #print ""

            