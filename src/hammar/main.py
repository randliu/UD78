# -*- coding:utf-8 -*-
'''
Created on 2015-5-20

@author: user
'''

from .models import Stock, TRACKSTATUS
from .utils import preProcess
from datetime import timedelta
import urllib
import contextlib
import datetime

sh = "sh"
sz = "sz"
hk = "hk"

"""
def runStock(market = None ,code =None ):
    if not code :
        return None
    set = Stock.objects

    if market:
"""

import time


def dailyRun(market=None, code=None, startSeq=0):
    lst_stock = Stock.objects.all().order_by("seq")

    if market is not None:
        lst_stock = lst_stock.filter(market=market)
    if code is not None:
        lst_stock = lst_stock.filter(code=code)

    start = None
    end = None

    for s in lst_stock:
        print s.seq
        if startSeq > 0:
            if s.seq < startSeq:
                continue

        else:
            pass

        print time.time
        print "\n" + "$$$$$$$$$$$$$$$$$$$$$$$$$" * 3 + "\n"
        print "scanning [%06d.%s %s] [seq:%d] " % (s.code, s.market, s.name, s.seq)
        api = s.getAPI()
        print "fetching daily price from %s" % api
        # print "begin:"+str(time.time())
        begin = time.time()
        if not start:
            start = begin
        prices = None
        with contextlib.closing(urllib.urlopen(api)) as x:
            # print time.time()
            print "Parsing"
            n, prices = preProcess(x)
            if n < 0:
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
        print "time cost:" + str(end - begin)

    print "\nTOTAL TIME COST:" + str(end - start) + "\n"


def track(code=None, market=None, v=6, day=7, showFade=False):
    d = datetime.datetime.now()
    # str(d.year-2000)+str("%02d"%d.month)+str("%02d"%d.day)
    offsetDays = timedelta(day)
    targetDay = d - offsetDays
    str_now = datetimeToTitanDatestr(targetDay)
    int_now = int(str_now)
    # in 1 month
    r = int_now
    # print "r=%d"%r

    # print "SELL:"
    stock_set = Stock.objects.all()
    if code:
        stock_set = stock_set.filter(code=code)
    if market:
        stock_set = stock_set.filter(market=market)

    print "\n" + "#######" * 6 + "\nRUN\n" + "#######" * 6

    print "\n" + "\nRISE TRACK\n" + "----------" * 6

    for s in stock_set:
        lst_riseTrack = s.risetrack_set.filter(status=TRACKSTATUS.RUN).filter(lastDay__gt=r).filter(
            lastValue__gt=v).order_by("lastDay").all()
        for rt in lst_riseTrack:
            # print "[%s] [%d - %d]    [%06d %s.%s] value:%d count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.lastValue,dt.count)
            # print "[%s]  [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tcount:%3d"%(dt.status,dt.beginDay,first_price,dt.lastDay,last_price,s.code,s.market,s.name,(last_price - first_price)/first_price * 100.0,dt.count)
            # print dt.toStr()
            print rt.toStr()
            # print ""

    print "\n" + "\nDROP TRACK\n" + "----------" * 6

    # print "BUY:"

    for s in stock_set:
        lst_dropTrack = s.droptrack_set.filter(status=TRACKSTATUS.RUN).filter(lastDay__gt=r).filter(
            lastValue__gt=v).order_by("lastDay").all()
        for dt in lst_dropTrack:
            # print "[%s] [%d - %d]    [%06d %s.%s] value:%d count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.lastValue,dt.count)
            print dt.toStr()

            # print ""
    print "\n"
    if not showFade:
        return

    print "\n" + "#######" * 6 + "\nFADED\n" + "#######" * 6

    print "\n" + "\nRISE TRACK\n" + "----------" * 6

    for s in stock_set:
        lst_riseTrack = s.risetrack_set.filter(status=TRACKSTATUS.FADE).filter(lastDay__gt=r).order_by("lastDay").all()
        for rt in lst_riseTrack:
            # print "[%s] [%d - %d]    [%06d %s.%s] count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.count)
            print rt.toStr()
            # print ""

    print "\n" + "\nDROP TRACK\n" + "----------" * 6

    # print "BUY:"

    for s in stock_set:
        lst_dropTrack = s.droptrack_set.filter(status=TRACKSTATUS.FADE).filter(lastDay__gt=r).order_by("lastDay").all()
        for dt in lst_dropTrack:
            # print "[%s] [%d - %d]    [%06d %s.%s] count:%3d"%(dt.status,dt.beginDay,dt.lastDay,s.code,s.market,s.name,dt.count)
            print dt.toStr()


def datetimeToTitanDatestr(d):
    str_now = str(d.year - 2000) + str("%02d" % d.month) + str("%02d" % d.day)
    return str_now


def report_hk(day=1, code=None):
    report(day=day, code=code, market="hk")


def report_sh(day=1, code=None):
    report(day=day, code=code, market="sh")


def report_sz(day=1, code=None):
    report(day=day, code=code, market="sz")


def report(day=1, code=None, market=None):
    d = datetime.datetime.now()
    # str(d.year-2000)+str("%02d"%d.month)+str("%02d"%d.day)
    offsetDays = timedelta(day)
    targetDay = d - offsetDays
    str_now = datetimeToTitanDatestr(targetDay)
    int_now = int(str_now)
    # in 1 month
    r = int_now
    #print "r=%d" % r

    # print "SELL:"
    stock_set = Stock.objects.all()
    if code:
        stock_set = stock_set.filter(code=code)
    if market:
        stock_set = stock_set.filter(market=market)
    print "\n" + "\nRISE TRACK\n" + "----------" * 6

    for s in stock_set:
        # print "[%06d %s.%s]"%(s.code,s.name,s.market)
        #注销.因为不希望空的股票做无效的显示,用i来判断

        i =0
        lst_riseTrack = s.risetrack_set.filter(status=TRACKSTATUS.SELL).filter(lastDay__gt=r).order_by("lastDay").all()

        for dt in lst_riseTrack:
            if i==0:
                #print "\n" + "\nRISE TRACK\n" + "----------" * 6
                pass

            last_price = s.dailyprice_set.get(day=dt.lastDay).close
            first_price = s.dailyprice_set.get(day=dt.beginDay).close
            print "[%s] [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tcount:%3d" % (
            dt.status, dt.beginDay, first_price, dt.lastDay, last_price, s.code, s.market, s.name,
            (last_price - first_price) / first_price * 100.0, dt.count)
            # print ""
            i=i+1

    print "\n" + "\nDROP TRACK\n" + "----------" * 6

    # print "BUY:"

    for s in stock_set:
        # print "[%06d %s.%s]"%(s.code,s.name,s.market)

        lst_dropTrack = s.droptrack_set.filter(status=TRACKSTATUS.BUY).filter(lastDay__gt=r).order_by("lastDay").all()
        i=0
        for dt in lst_dropTrack:
            if i==0:
                #print "\n" + "\nDROP TRACK\n" + "----------" * 6
                pass
            last_price = s.dailyprice_set.get(day=dt.lastDay).close
            first_price = s.dailyprice_set.get(day=dt.beginDay).close

            print "[%s]  [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tcount:%3d" % (
            dt.status, dt.beginDay, first_price, dt.lastDay, last_price, s.code, s.market, s.name,
            (last_price - first_price) / first_price * 100.0, dt.count)
            # print ""
            i==i+1


"""
def report_index(day=10,code = None,market=None):
    report(day=day,code = 99999999)
    report(day=day,code = 1,market="sh")
    report(day=day,code = 399001,market="sz")
    #report(day=day,)

"""

my = [(600363, "sh"), \
      (875, "sz"), \
      (601766, "sh"), \
      (777, "sz"), \
      (601169, "sh"), \
      (600030, "sh"), \
      (603169, "sh"), \
      (600585, "sh"), \
      (60638, "sh"), \
      (601628, "sh"), \
      (601818, "sh"), \
      (600299, "sh"), \
      (600255, "sh"), \
      ]

index = [ \
    (99999999, "hk"), \
    (1, "sh"), \
    (10, "sh"), \
    (16, "sh"), \
    (399001, "sz"), \
    (300, "sh"), \
    (132, "sh"), \
    (9, "sh"), \
    (88888888, "hk"), \
    (133,"sh"),\
    (903,"sh"),\
    (904,"sh"),\

    ]

my_hk = [ \
    (6136, "hk"), \
    (1776, "hk"), \
    (1613, "hk"), \
    (1330, "hk"), \
    (1299, "hk"), \
    (1164, "hk"), \
    (510, "hk"), \
    (392, "hk"), \
    (384, "hk"), \
    (154, "hk"), \
    (124, "hk"), \
    (5, "hk"), \
    (388, "hk"), \
    (656, "hk"), \
    (700, "hk"), \
    (337, "hk"), \
    (6886, "hk"), \
    ]


def report_my(day=3):
    for (c, m) in my:
        report(day=day, code=c, market=m)


def track_my(day=3, showFade=False, v=4):
    for (c, m) in my:
        track(showFade=showFade, code=c, market=m, v=v)


def report_index(day=3):
    for (c, m) in index:
        report(day=day, code=c, market=m)


def track_index(day=3, showFade=False, v=4):
    for (c, m) in index:
        track(showFade=showFade, code=c, market=m, v=v)


def report_myhk(day=3):
    for (c, m) in my_hk:
        report(day=day, code=c, market=m)


def track_myhk(day=3, showFade=False, v=4):
    for (c, m) in my_hk:
        track(showFade=showFade, code=c, market=m, v=v)
