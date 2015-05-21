#encoding: utf-8  

from django.db import models

#close status
class OnClose:
    RISE    =   "RISE"
    EQUAL   =   "EQUAL"
    DROP    =   "DROP"
    
    
# Create your models here.
class DailyPrice(models.Model):
    seq = models.AutoField(primary_key = True)
    day = models.IntegerField(default = 0,unique = True)
    open = models.FloatField(default = 0)
    close = models.FloatField(default = 0)
    high = models.FloatField(default = 0)
    low = models.FloatField(default = 0)
    onClose = models.CharField(max_length=50,default = OnClose.RISE)
    
    
    #suppuse that today is d-day
    #d(0) is today;d(1)is next market day ,such as tomorrow, if the market open
    #d(-1) is the previous market day ,such as ,yesterday,if the market open
    #so on
    def d(self,offset):
        cur_seq = 0
        try:
            if self.seq == 0:
                d=DailyPrice.objects.get(day = self.day)
                cur_seq = d.seq
            else:
                cur_seq = self.seq
        
                targetSeq = cur_seq +offset
                targetDP = DailyPrice.objects.get(seq = targetSeq)
            return targetDP
        except Exception:
            return None
    
    
    def __str__(self):
        if self.seq is None:
            return "{day:%d,open:%f,close:%f,high:%f,low:%f}"%(self.day,self.open,self.close,self.high,self.low)
        else:
            return "{seq:%d,day:%d,open:%f,close:%f,high:%f,low:%f}"%(self.seq,self.day,self.open,self.close,self.high,self.low)
    
    def getDelta(self):
        return 0.01
        
        q1  =   0.01
        q2  =   self.close / 1000.0
        
        
        delta = min(q1,q2)
        #delta = 0.015*2
        #delta
        return delta
    
    def isInterWith(self,dp):
        delta   =   self.getDelta()
        #sp1=    (self.low - delta,  self.high + delta)
        #print "[%f,%f],[%f,%f]"%(dp.high,dp.low,self.high+delta,self.low+delta)
        if dp.high <    self.low - delta:
            return False
        
        if dp.low > self.high + delta :
            return False
        
        return True
    

#compare the close price
class Ladder(models.Model):
    seq = models.AutoField(primary_key = True)
    day = models.IntegerField(default = 0,unique = True)
    ladder  =   models.IntegerField(default = 0)
    
    def __str__(self):
        if self.seq is None:
            return ("{day:%d,ladder：%d}"%(self.day,self.ladder))
        else:
            return ("{seq:%d,day:%d,ladder：%d}"%(self.seq,self.day,self.ladder))
        
"""
1|141211
2|141222
3|141229
4|150116
5|150130
6|150205
7|150217
8|150309
9|150331
10|150417
11|150423
"""        

class PeakPoint(models.Model):
    seq = models.AutoField(primary_key = True)
    day = models.IntegerField(default = 0,unique = True)
    #value   =   models.IntegerField(default = 0)
    def __str__(self):
        return "PeakPoint:{day:%d}"%(self.day)
    
class TroughPoint(models.Model):
    seq = models.AutoField(primary_key = True)
    day = models.IntegerField(default = 0,unique = True)
    #value   =   models.IntegerField(default = 0)
    def __str__(self):
        return "TroughPoint:{day:%d}"%(self.day)

class TRACKSTATUS:
    #BEGIN   =   "BEGIN"
    BUY     =   "BUY"
    SELL    =   "SELL"
    TRIGGER =   "TRIGGER"
    VIRGIN   =   "VIRGIN"
    FADE    =   "FADE"
    RUN =   "RUN"
    
class DropTrack(models.Model):
    seq     =   models.AutoField(primary_key    =   True)
    beginDay   =   models.IntegerField(default = 0,unique = True)
    endDay   =   models.IntegerField(default = 0)

    value   =   models.IntegerField(default = 0)
    status  =   models.CharField(max_length=50,default =TRACKSTATUS.RUN )
    current   =   models.IntegerField(default = 0)
    
    
    @classmethod
    def create(cls,day):
        beginVal = 0 
        dp  =   DailyPrice.objects.all().get(day=day)
        if dp.onClose   ==  OnClose.DROP:
            beginVal    =   1
        
        rt  =   DropTrack (beginDay = day, value = beginVal)
        
        try:
            rt.save()
        except:
            print "DropTrack %d existed"%day
            return None
        

            
        print "create DropTrack %d"%day
        return rt
    
    def countLadderValue(self,ladder):
        #before = self.value 
        
        if ladder.ladder == 0 or ladder.ladder == -2:
            pass
        else:
            self.value = self.value - ladder.ladder
        self.current = self.value 

        #self.save()
        #after = self.value
        #print "track: %d count ladder : {befor %d,after %d}"%(self.beginDay,before,after)
        return self.value
    
    def run(self):
        #lst_ladder = Ladder.objects.all().filter(day = self.beginDay).order_by("seq")
        #print lst_ladder
        pass
        lst_ladder = Ladder.objects.all().filter(day__gt =  self.beginDay).order_by("seq")
        for ladder in lst_ladder:
            self.countLadderValue(ladder)
            
            if self.value <=  -1:
                self.status = TRACKSTATUS.FADE
                self.endDay = ladder.day 
                self.save()
                break
            if self.value >=8:
                self.status = TRACKSTATUS.BUY
                self.endDay = ladder.day 

                print "sell at %d, triger by %d"%(ladder.day,self.beginDay)
                self.save()
                break
            
    
class RiseTrack(models.Model):
    seq     =   models.AutoField(primary_key    =   True)
    beginDay   =   models.IntegerField(default = 0,unique = True)
    endDay = models.IntegerField(default = 0)
    value   =   models.IntegerField(default = 0)
    status  =   models.CharField(max_length=50,default =TRACKSTATUS.RUN )
    
    #cur for running only
    cur  =0
    @classmethod
    def create(cls,day):
        beginVal = 0 
        dp  =   DailyPrice.objects.all().get(day=day)
        if dp.onClose   ==  OnClose.RISE:
            beginVal    =   1
        
        rt  =   RiseTrack(beginDay = day, value = beginVal)
        
        try:
            rt.save()
            return rt
        except Exception ,e:
            print e
            print "RiseTrack %d existed"%day
            return None
        
    @classmethod
    def load(cls,beginDay):
        rt  = None
        try:
            rt  =   RiseTrack.objects.all().get(beginDay=beginDay)
        except Exception:
            pass
        
        return rt
    
    def __str__(self):
        #str=  "RiseTrack:{%s,beginDay %d,current:%d"}%(self.status)
        pass
    

    """
    def __init__(self):
        raise Exception("Do not create RiseTrack in this way")
    """
    def countLadderValue(self,ladder):
        
        if ladder.ladder == 0 or ladder.ladder == 2:
            pass
        else:
            self.value = self.value +ladder.ladder
        
        #self.save()
        self.current = self.value 

        return self.value
    
        """
        if ladder.ladder == 1:
            self.value = self.value +1
            pass
        
        if ladder.ladder == -2:
            self.value  =   self.value -2
        
        if ladder.ladder == -1:
            self.value  =   self.value -2
        """
    def run(self):
        lst_ladder = Ladder.objects.all().filter(day__gt =  self.beginDay).order_by("seq")
        for ladder in lst_ladder:
            self.countLadderValue(ladder)
            if self.value <=  -1:
                self.status = TRACKSTATUS.FADE
                self.endDay = ladder.day 
                self.save()
                break
            if self.value >=7:
                self.status = TRACKSTATUS.SELL
                self.endDay = ladder.day 

                print "sell at %d, triger by %d"%(ladder.day,self.beginDay)
                self.save()
                break


        
        
        
        