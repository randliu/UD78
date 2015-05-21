from django.db import models

class Record:
    marketName = None
    stockCode = 0
    day = 0
    #price info
    open = 0
    close=0
    high = 0
    low = 0
    
class Stock(models.Model):
    seq = models.AutoField(primary_key=True)
    marketName = models.CharField(max_length=200)
    stockCode = models.IntegerField(default = 0)

        
# Create your models here.
class DailyPrice(models.Model):
    """
    seq = models.AutoField(primary_key=True)
    marketName = models.CharField(max_length=200)
    stockCode = models.IntegerField(default = 0)
    """
    #stockSeq = Stock.seq
    stockSeq = models.IntegerField(default=0)
    day = models.IntegerField(default = 0)
    openPrice = models.FloatField(default = 0)
    closePrice = models.FloatField(default = 0)
    high = models.FloatField(default = 0)
    low = models.FloatField(default = 0)
    
    
class Ladder(models.Model):
    seq     = models.AutoField(primary_key = True)
    stockID = models.IntegerField(default = 0)
    day     = models.IntegerField(default = 0)
    ladder  = models.IntegerField(default = 0)
    
class PeekPoint(models.Model):
    seq     = models.AutoField(primary_key = True)
    stockID = models.IntegerField(default = 0)
    day     = models.IntegerField(default = 0)
    count   = models.IntegerField(default = 0)
    
class TroughPoint(models.Model):
    seq     = models.AutoField(primary_key = True)
    stockID = models.IntegerField(default = 0)
    day     = models.IntegerField(default = 0)
    count   = models.IntegerField(default = 0)


class TrackStatus:
    RUN =   "TrackStatus.RUN"
    FAD =   "TrackStatus.FAD"
    BOOM    =   "TrackStatus.BOOM"

class RiseTrack(models.Model):
    seq     = models.AutoField(primary_key = True)
    stockID = models.IntegerField(default = 0)
    dDay  = models.IntegerField(default = 0)
    value   = models.IntegerField(default = 0)
    
    #TrackStatus.RUN/FAD/BONE/BOOM
    status  = models.CharField(max_length=200)

class TRACKRAIL(models.Model):
    seq =     models.AutoField(primary_key = True)
    stockID =   models.IntegerField(default=0)
    day =   models.IntegerField(default=0)
    

    
    