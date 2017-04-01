#encoding: utf-8

from django.db import models
from django.core import serializers
# from .utils import preProcess
from django.db.models import Min, Max
from django.contrib import admin
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
hdlr = logging.FileHandler("%s.log" % __name__)
logger.addHandler(hdlr)


# Create your models here.
# dailyAPI="http://data.gtimg.cn/flashdata/hushen/latest/daily/sh601288.js"

class Stock(models.Model):
    seq = models.AutoField(primary_key=True)
    market = models.CharField(max_length=50, default="None")
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="NO NAME!")

    # shortName = models.CharField(max_length = 50,default = "-" )


    def saveIfNotExisted(self):
        try:
            Stock.objects.filter(market=self.market).filter(code=self.code).get()
            print "Not saved, alread Existed."
        except:
            self.save()
            print "Saved!"

    def saveIfNotExist(self):
        self.saveIfNotExisted()

    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "Stock :" + self.market
        return s

    # for sh/sz only
    def getAPI(self):

        code = self.code

        if self.market == "sh":
            code = str("%06d" % code)
        if self.market == "sz":
            # 000002
            code = "%06d" % code
        s = "http://data.gtimg.cn/flashdata/hushen/latest/daily/%s%s.js" % (self.market, code)
        if self.market == "hk":
            code = "%05d" % code
            # http://data.gtimg.cn/flashdata/hk/daily/15/hk01299.js
            # s= "http://data.gtimg.cn/flashdata/hk/daily/15/%s%s.js"%(self.market,code)
            # 2016
            s = "http://data.gtimg.cn/flashdata/hk/daily/17/%s%s.js" % (self.market, code)

        """
        if self.market == "NYSE":
            #http://data.gtimg.cn/flashdata/us/weekly/usBABA.N.js
            s="http://data.gtimg.cn/flashdata/us/weekly/us"+self.name+".N.js"
            
        if self.market =="NASDAQ":
            #http://data.gtimg.cn/flashdata/us/weekly/usMSFT.OQ.js
            s="http://data.gtimg.cn/flashdata/us/weekly/us"+self.name+".OQ.js"
        """

        # HSI
        if self.code == 99999999:
            #############99999999
            s = "http://data.gtimg.cn/flashdata/hk/weekly/hkHSI.js"

        # logger.info("API:"+s)
        # http://data.gtimg.cn/flashdata/hk/latest/daily/hkHSI.js
        if self.code == 88888888:
            #############99999999
            s = "http://data.gtimg.cn/flashdata/hk/latest/daily/hkHSI.js"

        logger.info("API:" + s)

        return s

    def getDelta(self):

        # if self.market =="sh":
        #    lastest_dailyprice = s.dailyprice_set.order_by("-day").all()[:1]

        return 0.01

    def createRiseTrack(self, day):
        beginVal = 0
        dp = DailyPrice.objects.all().get(day=day, stock=self)
        if dp.onClose == OnClose.RISE:
            beginVal = 1

        rt = RiseTrack(beginDay=day, beginValue=beginVal, stock=self)

        rt.saveIfNotExist()

    def createDropTrack(self, day):
        beginVal = 0
        dp = DailyPrice.objects.all().get(day=day, stock=self)
        if dp.onClose == OnClose.DROP:
            beginVal = 1

        dt = DropTrack(beginDay=day, beginValue=beginVal, stock=self)

        dt.saveIfNotExist()

    def parse(self, lst_price):
        lst_daily_price = []

        # (ret,lst_price)=preProcess(data)
        for daily in lst_price:
            lst_p = daily.split(" ")
            day = int(lst_p[0])
            openprice = float(lst_p[1])
            closeprice = float(lst_p[2])
            high = float(lst_p[3])
            low = float(lst_p[4])

            d = DailyPrice(day=day, open=openprice, close=closeprice, high=high, low=low, stock=self)
            lst_daily_price.append(d)

        cnt = 0

        # 20150627 test daily price from tail ,to decrease time cost.
        # literally, each day only test once ,instead of handred of daily price
        # by rand

        while len(lst_daily_price) > 0:
            d = lst_daily_price.pop()
            try:
                if d.close < d.open:
                    d.onClose = OnClose.DROP
                if d.close == d.open:
                    d.onClose = OnClose.EQUAL

                if d.close > d.open:
                    d.onClose = OnClose.RISE
                existed = d.testExistInDB()
                if not existed:
                    d.save()
                    cnt = cnt + 1
                    logger.debug("add daily %s" % str(d))
                else:
                    print "daily price existed %s . BREAK!" % str(d.day)
                    break

            except Exception:
                print "daily price existed %s .STOP!" % str(d)
                # return -1
                # continue

        """
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
                    cnt = cnt+1
                    logger.debug( "add daily %s"% str(d))
            
            except Exception :
                print "daily price existed %s " %str(d)
                #return -1
                continue
            
            #print ret
        """

        return cnt

    def scanPeakPoint(self):
        # lst_dp = DailyPrice.objects.all().order_by("seq")
        # seq__min= DailyPrice.objects.all().aggregate(Min("seq"))['seq__min']
        # firstDP = DailyPrice.objects.all().get(seq=seq__min)
        firstDay = self.dailyprice_set.all().aggregate(Min("day"))['day__min']
        try:
            firstDP = self.dailyprice_set.get(day=firstDay)
        except Exception, e:
            print e
            print "Stock :%s" % str(self)
        dp = firstDP.d(1)

        previous = firstDP
        next_dp = dp.d(1)

        while next_dp is not None:

            if dp.high > previous.high and dp.high > next_dp.high:
                if max(dp.open, dp.close) > max(previous.close, previous.open) and max(dp.open, dp.close) > max(
                        next_dp.close, next_dp.open):
                    pp = PeakPoint(day=dp.day, stock=self)
                    pp.saveIfNotExist()

            previous = dp
            dp = next_dp
            next_dp = dp.d(1)

    def scanTroughPoint(self):
        # seq__min= DailyPrice.objects.all().aggregate(Min("seq"))['seq__min']
        # firstDP = DailyPrice.objects.all().get(seq=seq__min)
        firstDay = self.dailyprice_set.all().aggregate(Min("day"))['day__min']
        firstDP = self.dailyprice_set.get(day=firstDay)

        dp = firstDP.d(1)

        previous = firstDP
        next_dp = dp.d(1)

        while next_dp is not None:

            if dp.low < previous.low and dp.low < next_dp.low:
                if min(dp.open, dp.close) < min(previous.close, previous.open) and min(dp.open, dp.close) < min(
                        next_dp.close, next_dp.open):
                    tp = TroughPoint(day=dp.day, stock=self)
                    tp.saveIfNotExist()
            previous = dp
            dp = next_dp
            next_dp = dp.d(1)

    def scanRiseTrack(self):
        lst_troughPoint = TroughPoint.objects.all().filter(stock=self).order_by("day")
        for tp in lst_troughPoint:
            day = tp.day
            self.createRiseTrack(day)

        pass

    def scanDropTrack(self):
        lst_peakPoint = PeakPoint.objects.all().filter(stock=self).order_by("day")
        for pp in lst_peakPoint:
            day = pp.day
            # DropTrack.create(day)
            self.createDropTrack(day)

    def runRiseTrack(self):
        for rt in self.risetrack_set.filter(status=TRACKSTATUS.RUN).all():
            rt.run()

    def runDropTrack(self):
        for dt in self.droptrack_set.filter(status=TRACKSTATUS.RUN).all():
            dt.run()

    def scanLadder(self):
        # ?lst_dp = DailyPrice.objects.all().order_by("seq")
        lst_dp = self.dailyprice_set.all().order_by("day")

        isFirst = True
        last_dp = None
        value = 0
        cnt = 0
        for dp in lst_dp:
            value = 0
            if isFirst:
                isFirst = False
                last_dp = dp
                continue

            if dp.close > last_dp.close:
                if dp.isInterWith(last_dp):
                    value = 1
                else:
                    value = 2

            if dp.close == last_dp.close:
                value = 0

            if dp.close < last_dp.close:
                if dp.isInterWith(last_dp):
                    value = -1
                else:
                    value = -2
            last_dp = dp
            ladder = Ladder(day=dp.day, ladder=value, stock=self)
            ret = ladder.saveIfNotExist()
            if ret:
                cnt = cnt + 1

        return cnt

    def get_dailypirce_set(self):
        # lst_dp = self.stock.dailyprice_set.filter(day__lt = self.day).order_by("-day").all()[0:1-offset]

        # return self.droptrack_set.filter(status="RUN").all()
        return "<table> <tr><td>A</td><td>b</td></tr></table>"


class StockAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'market', 'seq', 'get_dailypirce_set')


# admin.site.register(DailyPrice,DailyPriceAdmin)

admin.site.register(Stock, StockAdmin)


class OnClose:
    RISE = "RISE"
    EQUAL = "EQUAL"
    DROP = "DROP"

# Create your models here.


class DailyPrice(models.Model):
    seq = models.AutoField(primary_key=True)
    day = models.IntegerField(default=0)
    open = models.FloatField(default=0)
    close = models.FloatField(default=0)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    onClose = models.CharField(max_length=50, default=OnClose.RISE)
    # stockSeq =   models.IntegerField(default = 0)
    stock = models.ForeignKey(Stock)

    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "DailyPrice:" + str(data)
        logger.debug(s)
        return s

    def testExistInDB(self):
        try:
            o = DailyPrice.objects.all().filter(day=self.day).filter(stock__market=self.stock.market)
            o = o.filter(stock__code=self.stock.code)
            o = o.filter(stock__name=self.stock.name)
            o = o.get()
            logger.info("%s  exist in db" % str(self))
            # print "%s  exist in db" % str(self)
            return True
        except Exception, e:
            logger.info("%s  not exist in db" % str(self))

            logger.debug(e)
            return False

    def d(self, offset):

        if offset == 0:
            return self

        if offset > 0:
            try:
                # dp = self.stock.DailyPrice__set.get(day = self.day)
                # lst_ladder = Ladder.objects.all().filter(day__gt =  self.beginDay).order_by("seq")

                lst_dp = self.stock.dailyprice_set.filter(day__gt=self.day).order_by("day").all()[0:offset + 1]
                # lst_dp = DailyPrice.objects.raw("select * from titan_dailyprice where stock_id = %d limit %d order by day"%(self.stock))
                dp = lst_dp[offset - 1]
                return dp
            except:
                return None

        if offset < 0:
            try:
                # dp = self.stock.DailyPrice__set.get(day = self.day)
                # lst_ladder = Ladder.objects.all().filter(day__gt =  self.beginDay).order_by("seq")

                lst_dp = self.stock.dailyprice_set.filter(day__lt=self.day).order_by("-day").all()[0:1 - offset]
                dp = lst_dp[-offset - 1]
                return dp
            except:
                return None

    def saveToDB(self):
        # first test if that day's stock price exist
        existed = self.testExistInDB()
        if (not existed):
            print "Saving DailyPrice %s" % str(self)
            self.save()
            # print "ret
        else:
            pass
        return

    def saveIfNotExist(self):
        self.saveToDB()

    def isInterWith(self, dp):
        if self.stock.market == "hk":
            return True

        delta = self.stock.getDelta()
        if self.stock.market == "NASDAQ" or self.stock.market == "NYSE":
            delta = max(delta, self.open / 1000.0 * 2)
        # sp1=    (self.low - delta,  self.high + delta)
        # print "[%f,%f],[%f,%f]"%(dp.high,dp.low,self.high+delta,self.low+delta)
        if dp.high < self.low - delta:
            return False

        if dp.low > self.high + delta:
            return False

        return True


class DailyPriceAdmin(admin.ModelAdmin):
    list_display = ('day', 'stock', 'onClose')


admin.site.register(DailyPrice, DailyPriceAdmin)


class Ladder(models.Model):
    seq = models.AutoField(primary_key=True)
    day = models.IntegerField(default=0)
    ladder = models.IntegerField(default=0)
    stock = models.ForeignKey(Stock)

    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "Ladder :" + str(data)
        return s

    def saveIfNotExist(self):
        existed = True

        try:
            self.stock.ladder_set.filter(day=self.day).get()
            # print ladder
        except:
            existed = False

        if not existed:
            print "Save Ladder:%s" % str(self)
            self.save()

        return not existed


class PeakPoint(models.Model):
    seq = models.AutoField(primary_key=True)
    day = models.IntegerField(default=0)
    stock = models.ForeignKey(Stock)

    # value   =   models.IntegerField(default = 0)
    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "PeakPoint :" + str(data)
        return s

    def saveIfNotExist(self):
        existed = True

        try:
            self.stock.peakpoint_set.filter(day=self.day).get()
            # print pp
        except:
            existed = False

        if not existed:
            print "Save PeakPoint:%s" % str(self)
            self.save()

        return not existed


class TroughPoint(models.Model):
    seq = models.AutoField(primary_key=True)
    day = models.IntegerField(default=0)
    stock = models.ForeignKey(Stock)

    # value   =   models.IntegerField(default = 0)
    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "TroughPoint:" + str(data)
        return s

    def saveIfNotExist(self):
        existed = True

        try:
            tp = self.stock.troughpoint_set.filter(day=self.day).get()
            # print "!%s"%str(tp)
        except:
            existed = False

        if not existed:
            self.save()
            print "-  TroughPoint saved! %s" % str(self)

        return not existed


class TRACKSTATUS:
    # BEGIN   =   "BEGIN"
    BUY = "BUY"
    SELL = "SELL"
    TRIGGER = "TRIGGER"
    VIRGIN = "VIRGIN"
    FADE = "FADE"
    RUN = "RUN"


class DropTrack(models.Model):
    seq = models.AutoField(primary_key=True)
    beginDay = models.IntegerField(default=0)
    beginValue = models.IntegerField(default=0)

    lastDay = models.IntegerField(default=0)
    lastValue = models.IntegerField(default=0)

    status = models.CharField(max_length=50, default=TRACKSTATUS.RUN)
    stock = models.ForeignKey(Stock)
    count = models.IntegerField(default=0)

    def countLadderValue(self, ladder):
        # before = self.value
        # self.lastValue = self.beginValue
        self.lastDay = ladder.day
        self.count = self.count + 1
        if ladder.ladder == 0 or ladder.ladder == -2:
            pass
        else:
            self.lastValue = self.lastValue - ladder.ladder

        # self.save()
        # after = self.value
        # print "track: %d count ladder : {befor %d,after %d}"%(self.beginDay,before,after)
        return self.lastValue

    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "DropTrack :" + str(data)

        return s

    def toStr(self):
        s = self.stock
        last_price = s.dailyprice_set.get(day=self.lastDay).close
        first_price = s.dailyprice_set.get(day=self.beginDay).close
        ret = "[%s]  [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tvalue:%d\tcount:%3d" % (
        self.status, self.beginDay, first_price, self.lastDay, last_price, s.code, s.market, s.name,
        (last_price - first_price) / first_price * 100.0, self.lastValue, self.count)
        return ret

    def saveIfNotExist(self):
        existed = True

        try:
            DropTrack.objects.all().filter(beginDay=self.beginDay, stock=self.stock).get()
            # print rt
        except:
            existed = False

        if not existed:
            self.save()
            print "    -  DropTrack saved %s" % str(self)

        return not existed

    def run(self):
        lst_ladder = Ladder.objects.all().filter(stock=self.stock).filter(day__gt=self.beginDay).order_by("day")
        # lst_ladder = Ladder.objects.all().filter(day__gt =  self.beginDay).order_by("seq")
        self.lastValue = self.beginValue
        self.count = 0
        mark = 8
        # if self.stock.market=="hk":
        #    mark = 6

        for ladder in lst_ladder:

            self.countLadderValue(ladder)

            if self.lastValue <= -1:
                self.status = TRACKSTATUS.FADE
                # self.endDay = ladder.day
                # self.save()
                break
            if self.lastValue >= mark:
                self.status = TRACKSTATUS.BUY
                # self.endDay = ladder.day

                print "[%d:%s]buy  at %d, triger by %d" % (self.stock.code, self.stock.name, ladder.day, self.beginDay)
                # self.save()
                break

        self.save()
        # beginLadderSeq


admin.site.register(DropTrack)


class RiseTrack(models.Model):
    seq = models.AutoField(primary_key=True)
    beginDay = models.IntegerField(default=0)
    beginValue = models.IntegerField(default=0)

    lastDay = models.IntegerField(default=0)
    lastValue = models.IntegerField(default=0)

    status = models.CharField(max_length=50, default=TRACKSTATUS.RUN)
    stock = models.ForeignKey(Stock)
    count = models.IntegerField(default=0)

    def __str__(self):
        data = serializers.serialize("json", [self])
        s = "RiseTrack :" + str(data)
        return s

    def toStr(self):
        s = self.stock
        last_price = s.dailyprice_set.get(day=self.lastDay).close
        first_price = s.dailyprice_set.get(day=self.beginDay).close
        ret = "[%s]  [%d @ %3.2f\t-\t%d @ %3.2f]\t[%06d %s.%s]\t%3.3f\tvalue:%d\tcount:%3d" % (
        self.status, self.beginDay, first_price, self.lastDay, last_price, s.code, s.market, s.name,
        (last_price - first_price) / first_price * 100.0, self.lastValue, self.count)
        return ret

    def saveIfNotExist(self):
        existed = True

        try:
            self.stock.risetrack_set.filter(beginDay=self.beginDay, stock=self.stock).get()
            # print rt
        except:
            existed = False

        if not existed:
            self.save()
            print "    -  RiseTrack saved %s" % str(self)

        return not existed

    # only call by track saved in db

    def run(self):
        # lst_ladder = Ladder.objects.all().filter(day = self.beginDay,stock = self.stock).order_by("seq")
        # print lst_ladder

        lst_ladder = Ladder.objects.all().filter(stock=self.stock).filter(day__gt=self.beginDay).order_by("day")
        self.lastValue = self.beginValue
        self.count = 0
        mark = 7
        # if self.stock.market =="hk":
        #    mark = 6
        for ladder in lst_ladder:
            self.countLadderValue(ladder)
            if self.lastValue <= -1:
                self.status = TRACKSTATUS.FADE
                # self.lastDay = ladder.day
                # self.save()
                break
            if self.lastValue >= mark:
                self.status = TRACKSTATUS.SELL
                # self.endDay = ladder.day

                print "[%d:%s]sell at %d, triger by %d" % (self.stock.code, self.stock.name, ladder.day, self.beginDay)
                # self.save()
                break

        self.save()
        # beginLadderSeq

    """
    def __init__(self):
        raise Exception("Do not create RiseTrack in this way")
    """

    def countLadderValue(self, ladder):
        # self.lastValue = self.beginValue
        self.lastDay = ladder.day
        self.count = self.count + 1
        if ladder.ladder == 0 or ladder.ladder == 2:
            pass
        else:
            self.lastValue = self.lastValue + ladder.ladder

        # self.save()
        return self.lastValue


admin.site.register(RiseTrack)

"""
class DailyPrice(models.Model):
    seq = models.AutoField(primary_key = True)
    day = models.IntegerField(default = 0)
    open = models.FloatField(default = 0)
    close = models.FloatField(default = 0)
    high = models.FloatField(default = 0)
    low = models.FloatField(default = 0)
    onClose = models.CharField(max_length=50,default = OnClose.RISE)
    #stockSeq =   models.IntegerField(default = 0)
    stock   =   models.ForeignKey(Stock)   

"""


# added 20150615 by rand
# modified 20170129 by rand
# combine 一直没有使用,直到最近才明白

class Combine(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="NEW COMBINE")


class StockTrait(models.Model):
    seq = models.AutoField(primary_key=True);
    #stock = models.ForeignKey(Stock)
    combine = models.ForeignKey(Combine)
    stock = models.OneToOneField(Stock)
    #s = models.OneToOneRel()
