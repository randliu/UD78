import urllib

from . import dailyAPI

from contextlib import closing  
from django.db.models import Min

#print info
from .models import *

    
def get_lastest_prices():
    """
    handler=urllib.urlopen(dailyAPI)
    info    =   handler.read()

    handler.close()
    """
    lst_price=[]
    cnt =0
    with  closing(urllib.urlopen(dailyAPI)) as info:
        for line in info:
            #cnt =cnt +1
            if line.startswith("1"):
                line=line.replace(u"\\n\\","")
                cnt=cnt+1
                line =line.replace('\n',"")
                #print line
                lst_price.append(line)
    return (cnt,lst_price)

def parse():
    lst_daily_price=[]
    
    (ret,lst_price)=get_lastest_prices()
    for daily in lst_price:
        lst_p = daily.split(" ")
        #print lst_p
        #print "ff"
        day = int(lst_p[0])
        openprice = float(lst_p[1])
        closeprice =   float(lst_p[2])
        high =   float(lst_p[3])
        low =   float(lst_p[4])
 
        d=DailyPrice(day=day,open=openprice,close = closeprice , high=high,low=low)
        lst_daily_price.append(d)
    
        
    for d in lst_daily_price:
        try:
            #d=lst_daily_price.pop()
            if d.close < d.open:
                d.onClose =  OnClose.DROP
            if d.close  == d.open:
                d.onClose = OnClose.EQUAL
            
            if d.close  > d.open:
                d.onClose = OnClose.RISE
            
            d.save()
            print "add daily %s"% str(d)
            
        except Exception :
            print "daily price existed %s " %str(d)
            #return -1
            continue
            pass 
        
    print ret
    return 0 

def scanLadder():
    lst_dp = DailyPrice.objects.all().order_by("seq")
    
    isFirst =   True
    last_dp  =   None
    value = 0

    for dp in lst_dp:
        value = 0
        if isFirst :
            isFirst = False
            last_dp=dp
            continue
        
            
        if dp.close > last_dp.close:
            if dp.isInterWith(last_dp)  :
                value = 1
            else:
                value = 2
        
        if dp.close == last_dp.close :
            value =0
            
        if dp.close < last_dp.close:
            if dp.isInterWith(last_dp):
                value =-1
            else:
                value = -2
        last_dp=dp
        ladder  =   Ladder(day = dp.day, ladder =value)
        try:
            
            ladder.save()
            print str(ladder)
        except Exception:
            print "ladder exist!%s"%str(ladder)
            pass
        

def scanPeakPoint():
    #lst_dp = DailyPrice.objects.all().order_by("seq")
    seq__min= DailyPrice.objects.all().aggregate(Min("seq"))['seq__min']
    firstDP = DailyPrice.objects.all().get(seq=seq__min)
    
    dp = firstDP.d(1)
    
    previous = firstDP
    next_dp = dp.d(1)
    
    while next_dp is not None :
        
        if dp.high > previous.high and dp.high >next_dp.high:
            if max_val(dp.open,dp.close) > max_val (previous.close,previous.open ) and  max_val(dp.open,dp.close) > max_val(next_dp.close,next_dp.open):
                pp = PeakPoint(day = dp.day)
                try:
                    pp.save()
                except Exception :
                    print "PeakPoint existed! :%s "%str(pp)
                
        previous = dp
        dp = next_dp
        next_dp = dp.d(1)
    

def scanTroughPoint():
    seq__min= DailyPrice.objects.all().aggregate(Min("seq"))['seq__min']
    firstDP = DailyPrice.objects.all().get(seq=seq__min)
    
    dp = firstDP.d(1)
    
    previous = firstDP
    next_dp = dp.d(1)
    
    while next_dp is not None :
        
        if dp.low < previous.low and dp.low <next_dp.low:
            if min(dp.open,dp.close) < min (previous.close,previous.open ) and  min(dp.open,dp.close) < min(next_dp.close,next_dp.open):
                tp = TroughPoint(day = dp.day)
                try:
                    tp.save()
                except Exception :
                    print "TroughPoint existed! :%s "%str(tp)
                
        previous = dp
        dp = next_dp
        next_dp = dp.d(1)

def scanRiseTrack():
    lst_troughPoint = TroughPoint.objects.all().order_by("seq")
    for tp in lst_troughPoint:
        day = tp.day
        RiseTrack.create(day)
        
        
    pass
def scanDropTrack():
    lst_peakPoint = PeakPoint.objects.all().order_by("seq")
    for pp in lst_peakPoint:
        day = pp.day
        DropTrack.create(day)
    
    

def runRiseTrack():
    lst_runingRiseTrack = RiseTrack.objects.all().filter(status = TRACKSTATUS.RUN)
    print lst_runingRiseTrack
    for rt in lst_runingRiseTrack:
        #day = rt.beginDay
        #dp = DailyPrice.objects.all().get(day)
        #next_dp = dp.d(1)
        lst_ladder = Ladder.objects.all().filter(day__gt =  rt.beginDay).order_by("seq")
        for ladder in lst_ladder:
            rt.countLadderValue(ladder)
            if rt.value <=  -1:
                rt.status = TRACKSTATUS.FADE
                rt.endDay = ladder.day 
                rt.save()
                break
            if rt.value >=7:
                rt.status = TRACKSTATUS.SELL
                rt.endDay = ladder.day 

                print "sell at %d, triger by %d"%(ladder.day,rt.beginDay)
                rt.save()
                break
        print "RiseTrack %d current value :%d"%(rt.beginDay,rt.value)
   
        

def runDropTrack():
    lst_runingDropTrack = DropTrack.objects.all().filter(status = TRACKSTATUS.RUN)
    print lst_runingDropTrack
    for dt in lst_runingDropTrack:
        #day = rt.beginDay
        #dp = DailyPrice.objects.all().get(day)
        #next_dp = dp.d(1)
        lst_ladder = Ladder.objects.all().filter(day__gt =  dt.beginDay).order_by("seq")
        for ladder in lst_ladder:
            dt.countLadderValue(ladder)
            if dt.value <=  -1:
                dt.status = TRACKSTATUS.FADE
                dt.endDay = ladder.day 
                dt.save()
                break
            if dt.value >=8:
                dt.status = TRACKSTATUS.BUY
                dt.endDay = ladder.day 

                print "sell at %d, triger by %d"%(ladder.day,dt.beginDay)
                dt.save()
                break
        print "DropTrack %d current value :%d"%(dt.beginDay,dt.value)


def dailyRun():
    parse()
    scanPeakPoint()
    scanTroughPoint()
    scanLadder()
    scanRiseTrack()
    scanDropTrack()
    runRiseTrack()
    runDropTrack()

