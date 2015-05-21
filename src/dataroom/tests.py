#encoding: utf-8  

from django.test import TestCase

from .models import Stock
# Create your tests here.
#社会
class QuestionMethodTests(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testStockSeq(self):
        cnt=Stock.objects.count()
        s=Stock(marketName="sh",stockCode=6000362)
        s.save(force_insert=True)
        self.assertEqual(s.seq, cnt+1, "OK! current seq:"+str(s.seq))
        
        