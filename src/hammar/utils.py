#encoding: utf-8
from contextlib import closing  
import urllib
from .models import DailyPrice,Stock,OnClose
import logging
logger = logging.getLogger(__name__)

def preProcess(data):
    """
    handler=urllib.urlopen(dailyAPI)
    info    =   handler.read()

    handler.close()
    """
    lst_price=[]
    cnt =0
    #dailyAPI    =   stock.getAPI()
    #with  closing(urllib.urlopen(dailyAPI)) as info:
    info =data
    #print data
    for line in info:
            if line.startswith("1"):
                line=line.replace(u"\\n\\","")
                cnt=cnt+1
                line =line.replace('\n',"")
                lst_price.append(line)
                
    logger.info("read %d prices lines"%cnt)
    logger.debug("prices :%s \n"%(lst_price))
    return (cnt,lst_price)


  
def parse(lst_price,stock):
    lst_daily_price=[]
    
    #(ret,lst_price)=preProcess(data)
    for daily in lst_price:
        lst_p = daily.split(" ")
        #print lst_p
        #print "ff"
        day = int(lst_p[0])
        openprice = float(lst_p[1])
        closeprice =   float(lst_p[2])
        high =   float(lst_p[3])
        low =   float(lst_p[4])
 
        d=DailyPrice(day=day,open=openprice,close = closeprice , high=high,low=low,stock = stock)
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
            
            #d.saveToDP()
            existed =   d.testExistInDB()
            if not existed :
                d.save()
            logger.debug( "add daily %s"% str(d))
            
        except Exception :
            print "daily price existed %s " %str(d)
            #return -1
            continue
            pass 
        
    #print ret
    return 0 

def scanPeakPoint(stock):
    pass
def scanTroughPoint(stock):
    pass

def scanRiseTrack(stock):
    pass

def scanDropTrack(stock):
    pass

def runRiseTrack(stock):
    pass

def runDropTrack(stock):
    pass    
