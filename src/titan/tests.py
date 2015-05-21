#encoding: utf-8  

from django.test import TestCase
#from contextlib import closing  

# Create your tests here.
#from . import stockCode,marketName
#from crawler import *
from .models import *
import utils
# Create your tests here.
#import django

class UtilsTests(TestCase):
    data = None
    stock = None
    
    def setUp(self):
        self.data = open("demo.txt")
        self.stock = Stock.objects.get(code = 600036)
        
    def tearDown(self):
        self.data.close()
        self.data = None
        self. stock     =   None
        
    def testPreProcess(self):
        cnt,lst_price = utils.preProcess(self.data)
        logger.debug(lst_price)
        self.assertEqual(cnt, 100, "preProcess 100 line")
        
    def testParse(self):
        #150417
        cnt ,lst_dp_line = utils.preProcess(self.data)
        ret = utils.parse(lst_dp_line,self.stock)
        #print self.stock
        self.assertEqual(0, ret, "Parse")
        
        
"""
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

class DailyPriceTests(TestCase):
    stock = None
    data = None
    
    def setUp(self):
        self.data = open("demo.txt")
        self.stock = Stock.objects.get(code = 600036)
        print self.stock
    def tearDown(self):
        self.data.close()
        self.data = None
        self. stock     =   None

    def testSaveToDB(self):
        dp = DailyPrice(day = 141125,open =10.85,close = 11.11,high = 11.21, low = 10.81,stock = self.stock)
        #dp.save()
        dp.saveToDB()
        self.assertEqual(1, 1, "testSaveToDB")
        
        
        