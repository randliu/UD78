#encoding: utf-8  

from django.test import TestCase

# Create your tests here.
from . import stockCode,marketName
from crawler import *
from .models import *
# Create your tests here.
#社会
class StockTests(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testStockCode(self):
        self.assertEqual(stockCode, "600036", "stock code OK!")
    
    def testMarketName(self):
        self.assertEqual(marketName, "sh", "market name  OK!")
    
    def testUnquie(self):
        s=DailyPrice(day=12,high=12,low=18,open =32,close=90)
        s.save()
        ret = 0
        s2=DailyPrice(day=12,high=12,low=18,open =32,close=90)
        try : 
            s2.save()
        except Exception :
            ret =-1
            pass
        self.assertEqual(ret, -1, "unique")
        
        
        
        
class CrawlerTests(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testGet_lastest_prices(self):
        (ret,a) = get_lastest_prices()
        print ret
        print len(a)
        self.assertEqual(100, ret, "get_lastest_prices")
        
    #def testParse(self):
    #    ret = parse()
    #    self.assertEqual(ret , -1, "parse")
        
    def testSeqAndDayInc(self):
        lst_dp=DailyPrice.objects.all().order_by("seq")
        isFirst=True
        last_seq=0
        last_day = 0
        
        OK =True
        for dp in lst_dp:
            if isFirst:
                last_seq    = dp.seq
                last_day    = dp.day
                isFirst     =   False
                continue
            if dp.seq>last_seq and dp.day >last_day:
                last_seq    = dp.seq
                last_day    = dp.day
                continue
            else:
                OK  = False
                self.fail("day:"%dp.seq)
                break
        
        self.assertTrue(OK, "day & seq OK")
        
        
    def testscanPeakPoint(self):
        scanPeakPoint()
        
    def testIsInterWith1(self):
        dp = DailyPrice(day= 150423, open=18,close =21, high = 22,low  = 12)
        dp1 = DailyPrice(day= 150423, open=18,close =22, high = 28,low  = 12)
        
        ret1 = dp.isInterWith(dp1)
        self.assertTrue(ret1, "inter")

    def testIsInterWith2(self):
        dp = DailyPrice(day= 150423, open=32,close =21, high = 32,low  = 21)
        dp1 = DailyPrice(day= 150423, open=13,close =20, high = 20.5,low  = 12)
        
        ret1 = dp.isInterWith(dp1)
        self.assertFalse(ret1, "inter2")
        
    def testmin_val(self):
        a=min_val(1,2.0)
        self.assertEqual(a, 1, "min_val")
        
    def testD(self):
        dp1 = DailyPrice.objects.get(day = 141219)
        dp2 =dp1.d(1)
        self.assertEqual(dp2.day,141222,"D+1")
        
    def testD2(self):
        dp1 = DailyPrice.objects.get(day = 141219)
        dp2 =dp1.d(-3)
        print "d-3 seq:%d"%dp2.seq
        self.assertEqual(dp2.day,141216,"D-3")
    
    